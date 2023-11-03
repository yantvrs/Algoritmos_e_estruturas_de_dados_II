# Requisito 2

Abaixo estão os resultados da análise para cada rede, acompanhados de gráficos representativos.

Para visualizar os códigos que geraram os gráficos das Redes, [clique aqui](https://github.com/yantvrs/Data_structure_2/tree/main/smallWorlds/Requisito_02/sources).

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

A análise das mensagens privadas trocadas em uma rede social online da Universidade da Califórnia, Irvine, representadas no conjunto de dados como arestas (u, v, t), indicou um padrão de regressão linear decrescente. Isso significa que, ao longo do tempo, há uma tendência de os usuários com menor atividade de envio de mensagens privadas se conectarem com aqueles que têm maior atividade. Em outras palavras, os usuários mais ativos tendem a receber mensagens de outros usuários com menor atividade. 

### Rede 5: Email-EU-Core Network

![Gráfico rede 5](https://github.com/yantvrs/Data_structure_2/blob/main/smallWorlds/Requisito_02/sources/imagens/degree_assortativity_rede_05.png)


O padrão de regressão linear suavemente crescente na rede de comunicação da instituição de pesquisa europeia sugere que a rede é assortativa. Isso significa que os membros da instituição tendem a se conectar com outros membros que estão em situações similares em termos de comunicação por e-mail.

## Conclusões

Com base nas análises realizadas em diversas redes e ambientes online, fica evidente que a estrutura de conexões entre elementos, seja em sites de perguntas e respostas como o MathOverflow, em redes de compartilhamento de arquivos peer-to-peer, em comunidades de discussão como o Slashdot, ou em redes sociais acadêmicas, pode variar significativamente. A observação de padrões de dissortatividade, como a tendência de produtos populares se conectarem a produtos menos populares, ou de assortatividade, onde indivíduos interagem mais frequentemente com outros em situações semelhantes, oferece insights valiosos sobre o comportamento dessas redes.

Essas descobertas destacam a importância de considerar a natureza específica de cada ambiente e a dinâmica subjacente que influencia as conexões entre os elementos. Essas análises também têm implicações significativas para entender como as pessoas interagem, tomam decisões e se relacionam em contextos online. Por exemplo, a dissortatividade em redes de compartilhamento de arquivos pode indicar estratégias de preferência por nós com mais conexões, afetando a eficiência da rede. Em contraste, a assortatividade em redes de comunicação institucional pode refletir a afinidade natural entre membros em situações semelhantes.

Portanto, o estudo desses padrões de conectividade é crucial para uma compreensão mais profunda da dinâmica das redes online, fornecendo informações valiosas para otimizar a eficiência, a resiliência e a experiência dos usuários em diferentes contextos virtuais. É importante ressaltar que a análise desses padrões deve ser adaptada às peculiaridades de cada rede e considerar fatores contextuais para uma compreensão completa das interações e comportamentos observados.