Aqui está o `README.md` no formato para o GitHub para o programa **bitpy 66**:

```markdown
# bitpy 66

**bitpy 66** é um programa desenvolvido em Python para realizar uma busca por uma chave privada específica em um espaço de chaves de 66 bits. Ele utiliza diversas técnicas avançadas de busca e otimização para maximizar a eficiência da busca, mesmo em um espaço de busca extremamente vasto. O objetivo final do programa é encontrar uma chave privada que corresponda a um endereço Bitcoin específico, permitindo o acesso a fundos associados a esse endereço.

## Funcionalidades

- **Busca Aleatória Otimizada:** Utiliza heurísticas para gerar chaves privadas de forma mais eficiente.
- **Filtro Bloom:** Implementado para evitar tentativas redundantes, reduzindo a chance de verificar chaves já processadas.
- **Reservoir Sampling:** Implementado para manter um subconjunto das chaves geradas, permitindo uma análise posterior ou um reprocessamento seletivo.
- **Processamento Paralelo:** Utiliza todos os núcleos da CPU disponíveis para maximizar a performance da busca.
- **Personalização de Recursos:** O usuário pode especificar a quantidade de memória RAM e o número de threads (núcleos de CPU) que deseja utilizar.
- **Monitoramento de Progresso:** Mostra o progresso total da busca a cada 60 segundos, incluindo o número total de chaves processadas e a taxa de processamento.
- **Interrupção Controlada:** Permite que o usuário interrompa o programa de forma segura com `Ctrl+C`, garantindo que todos os processos sejam encerrados corretamente.

## Como Funciona

O programa realiza a busca por uma chave privada que gera um endereço Bitcoin correspondente ao endereço alvo especificado. A busca é feita de forma otimizada, utilizando técnicas como:

1. **Busca Direcionada com Heurísticas:** A geração de chaves é feita de forma inteligente, priorizando áreas do espaço de busca mais promissoras.
2. **Filtro Bloom:** Evita a repetição de chaves processadas, economizando tempo e recursos.
3. **Reservoir Sampling:** Mantém uma amostra das chaves geradas para possível reanálise.
4. **Processamento Paralelo:** Divide o espaço de busca entre múltiplos processos, utilizando todos os núcleos de CPU disponíveis.
5. **Distribuição Dinâmica de Tarefas:** O espaço de busca pode ser redistribuído conforme o progresso, evitando processos estagnados.

## Requisitos

- Python 3.x
- Bibliotecas necessárias (instaláveis via `pip`):
  - `pycryptodome`
  - `bloom_filter`
- Hardware:
  - CPU com múltiplos núcleos.
  - Memória RAM (mínimo 4 GB, recomendável 16 GB ou mais).

## Uso

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/bitpy66.git
   cd bitpy66
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:
   ```bash
   python bitpy66.py
   ```

4. Ao iniciar, o programa perguntará quantos GB de RAM e quantos threads você deseja utilizar. Insira os valores conforme desejado.

5. O programa então iniciará a busca pela chave privada correspondente ao endereço alvo especificado no script.

## Interrompendo o Programa

Você pode interromper o programa a qualquer momento pressionando `Ctrl+C`. Isso garantirá que todos os processos em execução sejam encerrados corretamente.

## Contribuições

Contribuições são bem-vindas! Se você tem alguma sugestão ou melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

Este `README.md` é detalhado e segue o formato comum do GitHub. Ele inclui informações sobre o que o programa faz, como ele funciona, requisitos, instruções de uso, e como interromper o programa. Além disso, ele também oferece direções para contribuir com o projeto e menciona a licença, que você pode adaptar conforme necessário.
