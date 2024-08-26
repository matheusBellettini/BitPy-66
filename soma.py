import hashlib
import multiprocessing
import os
import random
import time
import signal
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from bloom_filter import BloomFilter
from collections import deque
from multiprocessing import Value, Lock

# Configurações da chave
KEY_BITS = 66
TOTAL_KEYS = 2 ** KEY_BITS

# Endereço específico a ser encontrado
TARGET_ADDRESS = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'

# Função para perguntar ao usuário quantos GB de RAM e quantos threads usar
def get_user_input():
    while True:
        try:
            ram_gb = int(input("Quantos GB de RAM você deseja usar (Máximo 16 GB): "))
            if 0 < ram_gb <= 16:
                break
            else:
                print("Por favor, insira um valor entre 1 e 16.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    while True:
        try:
            num_threads = int(input(f"Quantos threads (núcleos de CPU) você deseja usar (Máximo {multiprocessing.cpu_count()}): "))
            if 0 < num_threads <= multiprocessing.cpu_count():
                break
            else:
                print(f"Por favor, insira um valor entre 1 e {multiprocessing.cpu_count()}.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    return ram_gb, num_threads

# Configurações do Bloom Filter para evitar chaves duplicadas
ram_gb, num_threads = get_user_input()  # Solicitar entrada do usuário
estimated_elements = ram_gb * 10**7  # Estimar elementos com base no RAM disponível
false_positive_rate = 0.001  # 0,1% de taxa de erro
bloom_filter = BloomFilter(max_elements=estimated_elements, error_rate=false_positive_rate)

# Configurações do Reservoir Sampling
RESERVOIR_SIZE = 100000  # Tamanho do reservatório para amostragem
reservoir = deque(maxlen=RESERVOIR_SIZE)

# Variável global para contar chaves processadas
key_count_global = Value('i', 0)
lock = Lock()

# Função para gerar chaves privadas a partir de um número inteiro
def generate_key_from_int(n):
    key = ECC.construct(d=n, curve='P-256')
    private_key = key.export_key(format='DER')
    public_key = key.public_key().export_key(format='DER')
    return private_key, public_key

# Função para converter chave pública em endereço Bitcoin
def public_key_to_address(public_key):
    sha256 = SHA256.new(public_key)
    ripemd160 = hashlib.new('ripemd160', sha256.digest()).digest()
    return ripemd160.hex()

# Função para verificar se o endereço é o alvo
def is_target_address(address):
    return address == TARGET_ADDRESS

# Função para adicionar chave ao reservatório
def add_to_reservoir(key):
    if len(reservoir) < RESERVOIR_SIZE:
        reservoir.append(key)
    else:
        # Substitui aleatoriamente uma chave no reservatório
        index = random.randint(0, RESERVOIR_SIZE - 1)
        reservoir[index] = key

# Função principal de busca aleatória com heurísticas e contador
def search_wallet_randomly(start, end, key_count_global):
    try:
        while True:
            # Aplicação de heurísticas para gerar uma chave
            random_key = start + random.getrandbits(KEY_BITS // 2) * random.choice([1, 2, 4, 8, 16])
            random_key = random_key % TOTAL_KEYS
            
            # Verifica se a chave já foi utilizada usando o Bloom Filter
            if random_key in bloom_filter:
                continue
            
            private_key, public_key = generate_key_from_int(random_key)
            address = public_key_to_address(public_key)

            # Marca a chave como utilizada
            bloom_filter.add(random_key)
            add_to_reservoir(random_key)

            with lock:
                key_count_global.value += 1

            # Verificar se o endereço é o alvo
            if is_target_address(address):
                with open("wallet_found.txt", "w") as f:
                    f.write(f"Private Key: {private_key.hex()}\n")
                    f.write(f"Public Key: {public_key.hex()}\n")
                    f.write(f"Address: {address}\n")
                print(f"Endereço encontrado: {address}")
                os._exit(0)  # Para imediatamente o script quando a carteira for encontrada
    except Exception as e:
        print(f"Erro no processo: {e}")

# Função para mostrar o progresso total a cada 60 segundos
def log_progress(key_count_global, start_time):
    try:
        while True:
            time.sleep(60)
            elapsed_time = time.time() - start_time
            with lock:
                keys_processed = key_count_global.value
            keys_per_second = keys_processed / elapsed_time
            print(f"Total de chaves processadas: {keys_processed}, {keys_per_second:.2f} chaves/segundo")
    except Exception as e:
        print(f"Erro no log: {e}")

# Função para gerenciar o pool de processos
def parallel_search(num_processes):
    processes = []

    def start_processes():
        chunk_size = TOTAL_KEYS // num_processes
        for i in range(num_processes):
            start = i * chunk_size
            end = (i + 1) * chunk_size - 1
            if i == num_processes - 1:
                end = TOTAL_KEYS - 1  # Garantir que o último processo vá até o final

            process = multiprocessing.Process(target=search_wallet_randomly, args=(start, end, key_count_global))
            processes.append(process)
            process.start()

    # Iniciar o processo de logging
    start_time = time.time()
    log_process = multiprocessing.Process(target=log_progress, args=(key_count_global, start_time))
    log_process.start()

    start_processes()

    def shutdown(sig, frame):
        print("Encerrando todos os processos...")
        for process in processes:
            process.terminate()
        log_process.terminate()
        print("Todos os processos foram encerrados.")
        os._exit(0)

    signal.signal(signal.SIGINT, shutdown)

    while True:
        for process in processes:
            if not process.is_alive():
                processes.remove(process)
                print("Reiniciando processo que falhou...")
                start_processes()

if __name__ == "__main__":
    parallel_search(num_threads)  # Usar o número de threads especificado pelo usuário
