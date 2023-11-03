# Requisito 2

Abaixo estão os resultados da análise para cada rede, acompanhados de gráficos representativos.

## Resultados

### Rede 1: Amazon Product Co-purchasing Network

![Gráfico rede 1](https://github.com/yantvrs/Data_structure_2/blob/main/smallWorlds/Requisito_02/sources/imagens/degree_assortativity_rede_01.png)

Os resultados encontrados sugerem que os produtos no site MathOverflow e as interações dos clientes seguem um padrão de dissortatividade, onde produtos populares (com graus maiores) estão mais propensos a se conectar a produtos menos populares (com graus menores) na rede. Isso pode ter implicações interessantes para entender como os clientes interagem e tomam decisões de compra nesse ambiente online.


### Rede 2: Gnutella Peer-to-peer Network

![Gráfico rede 2](https://github.com/yantvrs/Data_structure_2/blob/main/smallWorlds/Requisito_02/sources/imagens/degree_assortativity_rede_02.png)

Uma análise da rede de compartilhamento de arquivos peer-to-peer Gnutella de agosto de 2002 revelou um padrão de regressão linear decrescente, indicando um coeficiente de assortatividade negativo. Isso significa que os nós com graus menores têm uma tendência a se conectar com nós de graus maiores na rede, tornando-a dissortativa. Essa característica sugere que hosts com menos conexões diretas preferem se conectar com hosts que possuem um maior número de conexões, o que pode influenciar a dinâmica, a eficiência e a robustez da rede de compartilhamento de arquivos peer-to-peer Gnutella.

### Rede 3: Slashdot Signed Social Network

![Gráfico rede 3](https://github.com/yantvrs/Data_structure_2/blob/main/smallWorlds/Requisito_02/sources/imagens/degree_assortativity_rede_03.png)

A análise da rede de amizades e inimizades entre os usuários do Slashdot, coletada em novembro de 2008, revelou um padrão de regressão linear suavemente decrescente no gráfico, indicando que não há uma relação clara entre os nós. Nesse contexto, a presença de uma regressão linear suavemente decrescente no gráfico sugere que não existe uma relação clara entre as pessoas que têm mais amigos ou mais inimigos na rede.

### Rede 4: CollegeMsg Temporal Network

![Gráfico rede 4](https://github.com/yantvrs/Data_structure_2/blob/main/smallWorlds/Requisito_02/sources/imagens/degree_assortativity_rede_04.png)

A análise das mensagens privadas trocadas em uma rede social online da Universidade da Califórnia, Irvine, representadas no conjunto de dados como arestas (u, v, t), indicou um padrão de regressão linear decrescente. Isso significa que, ao longo do tempo, há uma tendência de os usuários com menor atividade de envio de mensagens privadas se conectarem com aqueles que têm maior atividade. Em outras palavras, os usuários mais ativos tendem a receber mensagens de outros usuários com menor atividade. Essa dinâmica pode ter implicações interessantes para entender como a comunicação evolui dentro dessa rede social específica da Universidade da Califórnia, Irvine

### Rede 5: Email-EU-Core Network

![Gráfico rede 5](https://github.com/yantvrs/Data_structure_2/blob/main/smallWorlds/Requisito_02/sources/imagens/degree_assortativity_rede_05.png)


O padrão de regressão linear suavemente crescente na rede de comunicação da instituição de pesquisa europeia sugere que a rede é assortativa. Isso significa que os membros da instituição tendem a se conectar com outros membros que estão em situações similares em termos de comunicação por e-mail.

## Conclusões

Em resumo, essas redes exibem diferentes padrões de conexão e assortatividade, o que pode fornecer informações valiosas sobre como as interações ocorrem em cada contexto específico. Cada rede tem suas características distintas que afetam a dinâmica das conexões e as relações entre os nós.