# Requisito #01 - Geração da Rede a partir de SEEDs 📊🌐

## Descrição

Neste requisito, o objetivo é gerar uma rede (grafo) dirigida a partir dos links das páginas da Wikipedia. Foram escolhidas quatro SEEDs (páginas iniciais), cada uma representando um ponto de partida distinto para a construção da rede.

### SEEDs Escolhidas:

1. [SEED 1: Federative units of Brazil](https://en.wikipedia.org/wiki/Federative_units_of_Brazil#List) - Nós: 4792, Arestas: 85218
2. [SEED 2: Demographcs of Brazil](https://en.wikipedia.org/wiki/Demographics_of_Brazil) - Nós: 8574, Arestas: 136461
3. [SEED 3: List of Olympic Games host cities](https://en.wikipedia.org/wiki/List_of_Olympic_Games_host_cities) - Nós: 4084 , Arestas: 53981
4. [SEED 4: FIFA World Cup hosts](https://en.wikipedia.org/wiki/FIFA_World_Cup_hosts) - Nós: 4640, 94985 Arestas: 

## Código

O código para este requisito está disponível em [código/requisito_01.py](https://github.com/yantvrs/Data_structure_2/blob/main/U2T3/Requisito_1/requisito_1.ipynb).

## Rede Final

A rede final foi construída utilizando o método `compose` da biblioteca NetworkX, que permite a fusão das quatro redes geradas a partir das SEEDs escolhidas. Este processo uniu as informações das diferentes páginas iniciais, proporcionando uma visão consolidada do grafo resultante.

- Nós na Rede Final: 16816
- Arestas na Rede Final: 320507

### Tratamento da Rede

Antes de compor a rede final, algumas etapas de pré-processamento foram realizadas:

- Remoção de palavras duplicadas que continham cifrão.
- Remoção de palavras duplicadas no plural.
- Truncamento da rede com base no histograma dos graus de cada nó.
