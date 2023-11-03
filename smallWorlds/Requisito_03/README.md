# Requisito 3

Neste requisito, realizamos uma análise das seguintes redes: Amazon Product Co-purchasing, Gnutella Peer-to-peer, Slashdot Signed Social, CollegeMsg Temporal e Email-EU-Core. As métricas selecionadas para a análise incluem Nodes, Edges, Degree Assortativity Coefficient, Connected Components, Tamanho do Componente Gigante (GCC) e Coeficiente de Clustering.

## Tabela
|                                  | Nodes  | Edges   | Degree Assort. Coeff. | Connected components | GCC    | Avg. Clust. Coeff      |
|----------------------------------|--------|---------|-----------------------|----------------------|--------|------------------------|
| **Amazon Product Co-purchasing** | 403394 | 2443408 | -0.01764727676699205  | 7                    | 403364 | 0.41768123430510284    |    
| **Gnutella Peer-to-peer**        | 10876  | 39994   | -0.013168574879827224 | 1                    | 10876  | 0.00621753327714660625 |
| **Slashdot Signed Social**       | 77351  | 524207  | -0.056463267200593845 | 1                    | 77351  | 0.2392426996348363     |
| **CollegeMsg Temporal**          | 60810  | 73499   | -0.28722758485316324  | 4                    | 60800  | 0.0033675006441922137  |
| **Email-EU-Core**                | 1005   | 16706   | -0.010990490627931076 | 20                   | 986    | 0.3993549664221539     |

## Resultados

### Amazon Product Co-purchasing
- **Nodes e Edges:** A rede "Amazon Product Co-purchasing" é substancial, com mais de 403 mil produtos (nós) e mais de 2,4 milhões de conexões entre eles (arestas). Essa rede representa a co-compra de produtos na Amazon.

- **Degree Assortativity Coefficient:** O coeficiente de assortatividade de grau próximo de zero (-0,0176) sugere que, em média, produtos não têm uma forte tendência de se conectar a outros produtos de graus semelhantes, indicando uma certa aleatoriedade na escolha de produtos pelos consumidores.

- **Connected Components:** A rede está dividida em 7 componentes conectados, o que significa que há várias sub-redes independentes dentro dela. A maior dessas sub-redes contém 403.364 nós.

- **Tamanho do Componente Gigante (GCC):** O componente gigante é a maior componente conectada na rede e, neste caso, consiste em 403.364 nós. Isso representa a parte mais significativa da rede, onde a maioria dos produtos está conectada.

- **Coeficiente de Clustering:** Com um coeficiente de agrupamento médio de aproximadamente 0,4177, a rede exibe uma alta densidade de agrupamento. Isso significa que produtos tendem a estar mais interconectados em grupos, refletindo possíveis comunidades de produtos ou categorias similares.

### Gnutella Peer-to-peer
- **Nodes e Edges:** A rede "Gnutella Peer-to-peer" é uma rede de compartilhamento de arquivos, com 10.876 nós e 39.994 arestas. É uma rede menor em comparação com outras redes estudadas.

- **Degree Assortativity Coefficient:** O coeficiente de assortatividade de grau próximo de zero (-0,0132) sugere que, em média, os pares de nós não têm uma forte tendência de se conectar com base em seus graus, indicando uma certa aleatoriedade nas conexões de pares de compartilhamento de arquivos.

- **Connected Components:** A rede é altamente conexa, com um único componente conectado, o que significa que todos os nós estão interligados.

- **Tamanho do Componente Gigante (GCC):** A rede é completamente conectada, e o componente gigante inclui todos os nós (10.876 nós).

- **Coeficiente de Clustering:** O coeficiente de agrupamento médio é muito baixo, aproximadamente 0,0062. Isso indica que os nós na rede têm relativamente poucas conexões em comparação com outras redes, resultando em uma baixa densidade de agrupamento.

### Slashdot Signed Social
- **Nodes e Edges:** A rede "Slashdot Signed Social" é uma rede social com 77.351 nós e 524.207 arestas.

- **Degree Assortativity Coefficient:** O coeficiente de assortatividade de grau (-0,0565) sugere que há uma tendência negativa na conexão de nós de graus semelhantes, ou seja, nós de graus diferentes tendem a se conectar mais.

- **Connected Components:** A rede possui apenas um grande componente conectado, significando que todos os usuários estão interligados.

- **Tamanho do Componente Gigante (GCC):** O componente gigante inclui todos os nós (77.351), representando a parte central da rede.

- **Coeficiente de Clustering:** O coeficiente de agrupamento médio é moderadamente alto, aproximadamente 0,2392, o que indica que os usuários da rede tendem a se agrupar em pequenos grupos ou comunidades com conexões densas.

### CollegeMsg Temporal
- **Nodes e Edges:** A rede "CollegeMsg Temporal" é uma rede de mensagens entre estudantes universitários com 60.810 nós e 73.499 arestas.

- **Degree Assortativity Coefficient:** O coeficiente de assortatividade de grau é notavelmente negativo (-0,2872), sugerindo que a rede tem uma tendência forte de conectar nós de graus diferentes.

- **Connected Components:** A rede está dividida em 4 componentes conectados, o que indica a presença de várias comunidades ou grupos de estudantes na rede.

- **Tamanho do Componente Gigante (GCC):** O componente gigante contém 60.800 nós, representando a maior parte da rede.

- **Coeficiente de Clustering:** O coeficiente de agrupamento médio é muito baixo, aproximadamente 0,0034, indicando que a rede tem uma baixa densidade de agrupamento, o que pode estar relacionado à natureza das mensagens entre estudantes.

### Email-EU-Core
- **Nodes e Edges:** A rede "Email-EU-Core" é uma rede de e-mails com 1.005 nós e 16.706 arestas.

- **Degree Assortativity Coefficient:** O coeficiente de assortatividade de grau é próximo de zero (-0,0110), indicando uma leve tendência negativa na conexão de nós de graus semelhantes.

- **Connected Components:** A rede é fragmentada em 20 componentes conectados, sugerindo que existem várias sub-redes de comunicação de e-mail na rede.

- **Tamanho do Componente Gigante (GCC):** O componente gigante consiste em 986 nós, representando a maior parte da rede de e-mail.

- **Coeficiente de Clustering:** O coeficiente de agrupamento médio é relativamente alto, aproximadamente 0,3994, indicando que a rede de e-mail possui uma alta densidade de agrupamento, refletindo a formação de grupos de contatos na troca de e-mails.

Estas análises oferecem uma visão mais detalhada das características de cada rede e das métricas utilizadas na análise. Cada rede apresenta sua própria estrutura e dinâmica, e as métricas fornecem informações valiosas para compreender essas diferenças.

## Conclusões

Com base na análise das métricas para as redes estudadas, pode-se concluir que cada rede possui características distintas em termos de assortatividade de grau, componentes conectados, tamanho do componente gigante e coeficiente de agrupamento. Essas métricas são importantes para compreender a estrutura e a dinâmica de cada rede e podem ser usadas para diferentes finalidades, como otimização de algoritmos ou estudos de propagação de informações.
