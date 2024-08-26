

## Descrição

Este projeto é uma implementação avançada de uma busca em força bruta para encontrar uma chave privada de uma carteira de Bitcoin específica. A ideia central é utilizar técnicas avançadas de programação paralela e heurísticas para maximizar a eficiência da busca em um espaço de chaves extremamente vasto. Este código foi projetado para funcionar em hardware limitado, com ênfase em robustez e eficiência, permitindo que o programa rode por longos períodos sem intervenção.

## Funcionalidades Principais

### 1. **Busca em Força Bruta com Heurísticas**
   - Geração de chaves privadas aleatórias, priorizando áreas mais promissoras no espaço de chaves com base em heurísticas.
   - Uso de múltiplos processos para explorar diferentes partes do espaço de busca simultaneamente.

### 2. **Bloom Filter**
   - Implementação de um Bloom Filter para evitar a reutilização de chaves já testadas, economizando tempo e recursos.
   - Configurado para armazenar até 10 milhões de chaves com uma taxa de falsos positivos de 0,1%.

### 3. **Reservoir Sampling**
   - Uso de Reservoir Sampling para manter um cache eficiente de chaves “quentes” ou promissoras, permitindo um possível reuso dessas chaves em etapas futuras.

### 4. **Parallelismo Avançado**
   - Utilização de `multiprocessing.Pool` para gerenciar processos de forma eficiente, aproveitando todos os núcleos disponíveis na CPU.
   - Redistribuição dinâmica de tarefas entre os processos para evitar que algum processo fique estagnado ou pare de funcionar.

### 5. **Logging e Monitoramento**
   - Logging periódico do número total de chaves processadas e a taxa de processamento (chaves/segundo).
   - Implementação de um processo de logging separado para evitar sobrecarga na I/O.

### 6. **Gerenciamento de Memória**
   - Otimização do uso da memória RAM, utilizando até 12 GB dos 16 GB disponíveis, garantindo que o programa continue funcionando de forma eficiente por longos períodos.

### 7. **Resiliência e Manutenção de Processos**
   - Verificação contínua da saúde dos processos, com reinício automático de processos falhos para garantir que a busca continue de forma ininterrupta.
   - Tratamento avançado de exceções para lidar com erros inesperados, evitando falhas críticas no programa.

### 8. **Finalização Segura**
   - Suporte para interrupção manual através de `Ctrl+C`, garantindo que o programa seja encerrado de forma segura e os recursos sejam liberados corretamente.

## Requisitos

- **Python 3.7 ou superior**
- Bibliotecas necessárias:
  - `pycryptodome`
  - `bloom_filter`
  - `multiprocessing`
  - `hashlib`
  - `random`
  - `deque`
  - `signal`

Você pode instalar as dependências necessárias com o seguinte comando:

```bash
pip install pycryptodome bloom_filter
```

## Como Funciona

1. **Geração de Chaves Privadas**:
   - O programa gera chaves privadas usando uma combinação de números aleatórios e heurísticas, tentando focar em regiões do espaço de chaves que são mais prováveis de conter a chave alvo.

2. **Conversão para Endereço Bitcoin**:
   - Cada chave privada gerada é convertida para uma chave pública e, em seguida, para um endereço Bitcoin.

3. **Verificação de Alvo**:
   - O endereço gerado é comparado com o endereço alvo. Se houver uma correspondência, a chave privada correspondente é salva em um arquivo de texto.

4. **Parallelismo**:
   - O espaço de chaves é dividido entre vários processos que trabalham em paralelo, aumentando a taxa de processamento total.

5. **Bloom Filter**:
   - Utilizado para garantir que a mesma chave não seja testada mais de uma vez, evitando desperdício de tempo e recursos.

6. **Reservoir Sampling**:
   - Um cache de chaves promissoras é mantido em memória, permitindo uma exploração mais eficiente do espaço de busca.

7. **Logging**:
   - O progresso total é registrado periodicamente, permitindo o monitoramento contínuo do desempenho do programa.

## Uso

Execute o script principal para iniciar a busca:

```bash
python bitcoin_wallet_brute_force.py
```

O script utilizará automaticamente todos os núcleos da CPU disponíveis e até 12 GB de memória RAM. Você pode interromper a execução a qualquer momento pressionando `Ctrl+C`.

## Considerações Finais

Este código foi projetado para rodar por longos períodos e maximizar as chances de encontrar a chave privada correspondente ao endereço Bitcoin alvo. Ele é altamente configurável e pode ser ajustado para diferentes ambientes de hardware.
