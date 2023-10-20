# Projeto de Análise de Dados - Jogo F1 Clash

O F1 Clash é um jogo móvel emocionante que oferece uma experiência única de gerenciamento de uma equipe de automobilismo de Fórmula 1. Desenvolvido com base no emocionante mundo da FIA Formula One World Championship, o jogo oferece aos jogadores a oportunidade de entrar no mundo da Fórmula 1, assumindo o papel de gerente de equipe.

Este repositório contém o código e os resultados de um projeto de análise de dados que utiliza o jogo móvel F1 Clash como contexto. O projeto envolve a aplicação de conceitos de grafos e redes nas tarefas 1, 2 e 3. O objetivo principal é analisar as configurações de veículo, componentes e garrafinhas no jogo e criar visualizações informativas.

## Tarefas


### Tarefa 1 (Histograma das Configurações)

Nesta tarefa, nosso objetivo era criar um histograma para a métrica "Team Score" com base nas 262.144 possíveis combinações de configurações de veículo no jogo F1 Clash. Além disso, estabelecemos um limite no histograma para filtrar as configurações viáveis, a fim de identificar configurações com maior potencial no jogo.

![Histograma Team Score](https://github.com/yantvrs/Data_structure_2/blob/main/configuringASetup/images/limite_0_task_1.png)

**Processo:**

- **Geração de Combinações de Configurações:** Começamos gerando todas as combinações possíveis de configurações de veículo no jogo, considerando as opções disponíveis para freios, caixa de câmbio, asas dianteiras e traseiras, suspensão e motor. Isso resultou em um grande número de configurações diferentes (262.144 no total).

- **Cálculo do "Team Score":** Para cada configuração, calculamos o "Team Score" com base nas contribuições de diferentes elementos, como velocidade, capacidade de curva, unidade de potência e confiabilidade. O "Team Score" é uma métrica que representa o desempenho geral da configuração.

- **Criação do Histograma:** Com os "Team Scores" calculados, criamos um histograma para visualizar a distribuição dessas pontuações. O histograma nos permitiu ver como os "Team Scores" estavam distribuídos entre todas as configurações.

- **Estabelecimento de um Limite no Histograma:** Para identificar configurações viáveis e com alto potencial de desempenho, estabelecemos um limite no histograma. O limite foi definido com base em nossos critérios e objetivos específicos para o jogo.

**Lógica para Definir o Limite:**

A lógica para definir o limite no histograma foi baseada em vários fatores:

1. **Objetivos de Desempenho:** Consideramos nossos objetivos específicos em relação ao desempenho da equipe no jogo. Quais pontuações de "Team Score" consideraríamos aceitáveis e bem-sucedidas no contexto do jogo?

2. **Comparação com Média:** Comparamos a distribuição dos "Team Scores" com uma média de desempenho. O limite foi definido de modo a incluir configurações que superassem significativamente essa média.

3. **Equilíbrio entre Desafio e Sucesso:** Equilibramos o desafio do jogo com a busca por configurações que oferecessem um bom desempenho. O limite foi estabelecido de forma a não tornar o jogo muito fácil, mas também não muito difícil.

**Conclusões:**

Com o limite definido no histograma, identificamos configurações que possuem um potencial considerável no jogo. Essas configurações têm "Team Scores" que atendem aos nossos critérios de desempenho desejados. Isso nos permitiu concentrar nossos esforços e recursos nas configurações mais promissoras, otimizando a experiência de gerenciamento da equipe no F1 Clash.



### Tarefa 2 (Grafo das Configurações e Componentes)


Na Tarefa 2, criamos um grafo direcionado que nos permitiu visualizar as relações entre as configurações de veículo e os componentes no jogo F1 Clash. Duas abordagens foram adotadas para determinar o tamanho dos nós de configuração no grafo: "Team Score" ou "Out Degree" dos cards. As arestas representam as conexões entre as configurações e os componentes.

- **Tamanho dos Nós:** A representação visual dos nós de configuração com base no "Team Score" destacou as configurações com alto potencial de desempenho no jogo. Configurações com "Team Scores" mais elevados são exibidas com nós maiores, facilitando a identificação das configurações mais promissoras.

- **Relações entre Configurações e Componentes:** O grafo revelou as relações entre as configurações e os componentes. A presença de arestas indicou quais componentes estão presentes em cada configuração. Isso é valioso para estratégias de configuração de veículo.

![Imagem do grafo](https://github.com/yantvrs/Data_structure_2/blob/main/configuringASetup/images/task_2_part_1.png)
**PDF do "Out Degree" dos Vértices de Configuração:**

Além disso, geramos um gráfico para a Função de Densidade de Probabilidade (PDF) do "Out Degree" dos vértices de configuração no grafo. O gráfico de PDF nos ajuda a entender como as configurações se relacionam com os componentes em termos de conexões.

![Gráfico PDF](https://github.com/yantvrs/Data_structure_2/blob/main/configuringASetup/images/task_2_part_2.png)

A análise do gráfico PDF revelou informações sobre a distribuição das conexões entre as configurações e os componentes. Isso pode ser útil para otimizar as configurações de veículo e tomar decisões estratégicas com base na presença de componentes específicos.

### Tarefa 3 (Grafo Bipartido das Garrafinhas)

A Tarefa 3 envolve a criação de um grafo bipartido que representa as garrafinhas do jogo F1 Clash e suas propriedades correspondentes. Os nós de garrafinhas são posicionados em um layout elíptico, enquanto os nós de propriedades são posicionados mais próximos das garrafinhas. As arestas representam a relação entre as garrafinhas e suas propriedades.

![Grafo Bipartido das Garrafinhas](https://github.com/yantvrs/Data_structure_2/blob/main/configuringASetup/images/task_3.png)

O código para a Tarefa 3 está contido no arquivo `tarefa3.py`.

## Como Executar o Código

Para executar o código, siga estas etapas:

1. Instale as bibliotecas necessárias: `networkx`, `matplotlib`, e `seaborn`.

2. Execute cada arquivo de tarefa separadamente, por exemplo, `python tarefa1.py`.

3. Os gráficos resultantes serão gerados e exibidos na tela.

## Contribuição

Sinta-se à vontade para contribuir para este projeto abrindo problemas, propondo melhorias ou adicionando novas funcionalidades.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

**Equipe do Projeto**:

- [Emanoel Batista](https://github.com/EmanoelBatista) 
- [Yan Tavares](https://github.com/yantvrs) 

