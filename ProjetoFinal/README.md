# Comparação de Infraestrutura Ciclística em Diferentes Cidades 🚴

## Vídeo explicativo 

Para acessar a o vídeo, basta clicar [aqui](https://drive.google.com/file/d/1NTE0BD7zcpurdmelEv9UJvdwMKmtRaCs/view?usp=sharing)

## Descrição do Projeto

O projeto final da disciplina de Estrutura de Dados 2 tem como objetivo realizar uma análise comparativa da
infraestrutura ciclística em diferentes cidades, utilizando técnicas de extração de dados, construção de grafos de
ciclovias,
análise comparativa, identificação de áreas críticas, propostas de melhoria e visualização de dados geoespaciais.

### 1. Cidades Analisadas

#### 1.1 São Paulo

São Paulo, a maior cidade do Brasil, enfrenta desafios significativos relacionados ao trânsito e à mobilidade.
A escolha de São Paulo se deve à sua vasta extensão, diversidade urbana e à busca por compreender como uma metrópole
de grandes proporções lida com a infraestrutura ciclística.

#### 1.2 Amsterdam

Amsterdam é conhecida mundialmente por sua cultura ciclística avançada. A cidade é famosa por suas ciclovias bem
planejadas e pela alta participação de ciclistas em seu sistema de transporte. A escolha de Amsterdam visa entender
como uma cidade com uma tradição ciclística consolidada aborda o planejamento urbano voltado para bicicletas.

#### 1.3 Berlin

A capital da Alemanha, Berlin, tem experimentado mudanças significativas em sua infraestrutura ciclística nas
últimas décadas. A escolha de Berlin permite explorar os esforços de uma cidade europeia em desenvolvimento contínuo,
buscando adaptar sua infraestrutura para promover uma mobilidade mais sustentável.

### 2. Extração de Dados e Construção de Grafos

#### 2.1 Amsterdam

- **Análise do Grafo**: A rede de ciclovias de Amsterdam é densamente entrelaçada, com numerosas interconexões entre os
  nós, indicando uma vasta rede de ciclovias bem conectadas. Isso sugere alta acessibilidade e opções de rotas para
  ciclistas. Além disso, a complexidade do grafo reflete o planejamento urbano centrado no ciclista, com uma
  infraestrutura que apoia não apenas o lazer, mas também o ciclismo como um modo de transporte diário, revelando como a
  política e cultura holandesas favorecem o ciclismo.

![Ciclovias Amsterdã](https://github.com/yantvrs/Data_structure_2/blob/main/ProjetoFinal/images/ciclovias_Amsterdam.png)

#### 2.2 São Paulo

- **Análise do Grafo**: O grafo de São Paulo mostra uma rede de ciclovias menos densa e mais fragmentada, com menos
  conexões, e nós isolados. Esse cenário indica uma cobertura menor e menos continuidade nas rotas de ciclovias.
  A estrutura do grafo sugere que, embora haja esforços para desenvolver a infraestrutura de ciclovias, a cidade ainda
  pode ter áreas significativas não atendidas por ciclovias seguras e conectadas, demonstrando a existência das reais
  prioridades de mobilidade urbana e dos desafios de planejamento na cidade.

![Ciclovias São Paulo](https://github.com/yantvrs/Data_structure_2/blob/main/ProjetoFinal/images/ciclovias_Sao_Paulo.png)

#### 2.3 Berlim

- **Análise do Grafo**: O grafo de Berlim apresenta uma rede intermediária, mais conectada que São Paulo, mas não tão
  densamente entrelaçada como Amsterdam. Há uma boa quantidade de nós e conexões, mas com algumas áreas menos servidas.
  A configuração da rede de ciclovias de Berlim sugere um compromisso com o ciclismo, ainda que o grafo
  mostre que a cobertura pode não ser tão extensa quanto em Amsterdam. A distribuição das ciclovias pode ser
  influenciada pelo layout histórico da cidade e pelas políticas de mobilidade.

![Ciclovias Berlim](https://github.com/yantvrs/Data_structure_2/blob/main/ProjetoFinal/images/ciclovias_Berlin.png)

### 3. Análise Comparativa

#### 3.1 São Paulo:
- **Número de Nós (n):** 1509
- **Número de Arestas (m):** 1881
- **Grau Médio (k_avg):** 2.493042
- **Comprimento Total das Arestas:** 726266.943 metros
- **Comprimento Médio das Arestas:** 386.106828 metros
- **Média de Ruas por Nó:** 3.056329
- **Contagem de Ruas por Nó:** {0: 0, 1: 136, 2: 73, 3: 943, 4: 287, 5: 68, 6...}
- **Proporção de Ruas por Nó:** {0: 0.0, 1: 0.09012591119946985, 2: 0.04837640...}
- **Número de Interseções:** 1373
- **Comprimento Total das Ruas:** 441314.035 metros
- **Contagem de Segmentos de Ruas:** 1194
- **Comprimento Médio das Ruas:** 369.609745 metros
- **Média de Circularidade (circuity_avg):** 1.085556
- **Proporção de Loops (self_loop_proportion):** 0.005025
- **Densidade de Nós por km²:** 0.991115
- **Densidade de Interseções por km²:** 0.90179
- **Densidade de Arestas por km²:** 477.014106
- **Densidade de Ruas por km²:** 289.85626

Com um número relativamente baixo de nós (1509) e arestas (1881), a densidade de ciclovias em São Paulo é modesta, algo explícito ao analisar a menor densidade de nó e aresta entre as três cidades. Além disso, por ser uma cidade extremamente populosa, São Paulo também apresenta menor extensão de ciclovia por habitante, com uma taxa de 0.03853 metros de ciclovia por habitante. Por fim, tratando de área, São Paulo possui cerca de 289.85 metros de ciclovia por quilômetro quadrado.

#### 3.2 Amsterdam:
- **Número de Nós (n):** 6307
- **Número de Arestas (m):** 11454
- **Grau Médio (k_avg):** 3.632155
- **Comprimento Total das Arestas:** 1406328.214 metros
- **Comprimento Médio das Arestas:** 122.780532 metros
- **Média de Ruas por Nó:** 3.152846
- **Contagem de Ruas por Nó:** {0: 0, 1: 167, 2: 544, 3: 3923, 4: 1539, 5: 10...}
- **Proporção de Ruas por Nó:** {0: 0.0, 1: 0.026478515934675758, 2: 0.0862533...}
- **Número de Interseções:** 6140
- **Comprimento Total das Ruas:** 871651.738 metros
- **Contagem de Segmentos de Ruas:** 7240
- **Comprimento Médio das Ruas:** 120.393886 metros
- **Média de Circularidade (circuity_avg):** 1.044301
- **Proporção de Loops (self_loop_proportion):** 0.000691
- **Densidade de Nós por km²:** 28.744173
- **Densidade de Interseções por km²:** 27.983069
- **Densidade de Arestas por km²:** 6409.345297
- **Densidade de Ruas por km²:** 3972.555561

Com um número mais significativo de nós e arestas em Amsterdã, a densidade de ciclovias é notavelmente mais alta do que em São Paulo, evidenciando uma infraestrutura mais densa para ciclistas na cidade holandesa. A extensão de ciclovia por habitante em Amsterdã é notavelmente superior, alcançando 0.54358 metros por habitante, além disso, a densidade de ciclovias por quilômetro quadrado em Amsterdã atinge 3972.56 metros por quilômetro quadrado. Esses dados ressaltam a diferença substancial na infraestrutura ciclística entre as duas cidades já apresentadas, com Amsterdã apresentando uma cobertura mais ampla e densa para os ciclistas.

#### 3.3 Berlim:
- **Número de Nós (n):** 6437
- **Número de Arestas (m):** 8087
- **Grau Médio (k_avg):** 2.512661
- **Comprimento Total das Arestas:** 1650591.237 metros
- **Comprimento Médio das Arestas:** 204.104271 metros
- **Média de Ruas por Nó:** 2.93149
- **Contagem de Ruas por Nó:** {0: 0, 1: 804, 2: 905, 3: 2955, 4: 1511, 5: 23...}
- **Proporção de Ruas por Nó:** {0: 0.0, 1: 0.12490290508000622, 2: 0.14059344...}
- **Número de Interseções:** 5633
- **Comprimento Total das Ruas:** 1063514.305 metros
- **Contagem de Segmentos de Ruas:** 5555
- **Comprimento Médio das Ruas:** 191.45172 metros
- **Média de Circularidade (circuity_avg):** 1.054404
- **Proporção de Loops (self_loop_proportion):** 0.00126
- **Densidade de Nós por km²:** 7.226978
- **Densidade de Interseções por km²:** 6.324308
- **Densidade de Arestas por km²:** 1853.159436
- **Densidade de Ruas por km²:** 1194.033705

Berlim possui uma densidade intermediária de ciclovias, com 6437 nós e 8087 arestas. As densidades de nós e arestas são maiores que São Paulo, mas menores que Amsterdam. Além das taxas de ciclovia por habitante e por área, 0.28651 metros por habitante e 1194.0337 metros por quilômetro quadrado, respectivamente.

#### 3.4 Conclusão da análise

As três cidades ilustram abordagens distintas na integração de ciclovias urbanas. São Paulo está em fase inicial de
adaptação, tentando conciliar o desenvolvimento sustentável com a predominância de veículos motorizados e desafios
socioeconômicos. Amsterdam, por sua vez, com sua cultura ciclística histórica e topografia plana, destaca-se como um
exemplo de infraestrutura que promove ativamente o ciclismo, impactando positivamente a qualidade de vida e a
sustentabilidade. Já Berlim, encontra-se em transição, buscando harmonizar seu patrimônio histórico com o avanço de
uma infraestrutura ciclística mais sustentável. Coletivamente, essas cidades refletem a interação entre políticas
públicas e cultura de transporte, deixando explícita a necessidade de planejamento que respeite as características
únicas de cada localidade na promoção de um transporte mais verde e acessível.

### 4. Identificação de Áreas Críticas

#### 4.1 São Paulo

A análise visual e quantitativa do grafo de São Paulo revela uma rede com conectividade limitada e segmentos de
ciclovias isolados. Com 0.0385 metros de ciclovias por habitante e uma densidade de 289.86 metros por quilômetro
quadrado, áreas críticas provavelmente incluiriam regiões suburbanas e distritos industriais, bairros com alta densidade
populacional mas pouca infraestrutura, onde as ciclovias parecem terminar abruptamente ou estão desconectadas da rede
central.

#### 4.2 Amsterdam

O grafo de Amsterdam mostra uma rede densa e bem conectada, com uma alta quantidade de ciclovias por habitante (0.5436
metros) e a maior densidade de ciclovias (3972.56 metros por quilômetro quadrado). Áreas críticas podem não ser tão
evidentes quanto em outras cidades, mas podem existir onde o crescimento urbano superou a infraestrutura existente,
ou onde há lacunas na rede central, em novos desenvolvimentos urbanos que ainda não estão totalmente integrados.

#### 4.3 Berlim

Em Berlim, o grafo sugere uma boa conectividade, uma medida intermediária de ciclovias por habitante (0.2865 metros) e
uma densidade de 1194.03 metros por quilômetro quadrado, mas com alguns pontos onde a rede é menos densa.
Áreas críticas podem incluir regiões periféricas e áreas com planejamento urbano histórico que dificultam a introdução
de novas ciclovias.

#### 4.4 Comparação de Áreas Críticas

Ao comparar as três cidades, São Paulo apresenta a maior necessidade de expansão de sua rede ciclística, com foco em
regiões de alta densidade populacional e bairros periféricos. Amsterdam pode ter poucas áreas críticas, focando na
manutenção da infraestrutura existente e na integração de novos desenvolvimentos urbanos, enquanto Berlim parece estar
em um caminho de melhoria contínua, precisando de atenção nas áreas de expansão urbana.

### 5. Propostas de Melhorias

#### 5.1 São Paulo

Para São Paulo, a expansão da rede ciclística deve possuir foco em conectar bairros populosos ao centro da cidade para
criar uma malha mais coesa. A integração de ciclovias com o transporte público pode ser fortalecida através de estações
de bicicletas próximas a terminais de ônibus e metrô, incentivando as diversas possibilidades. Além disso, a promoção do
ciclismo através de campanhas de conscientização e políticas de incentivo, como a redução de impostos na compra de
bicicletas e equipamentos de segurança, pode acelerar a adoção dessa prática pela população.

#### 5.2 Amsterdã

Em Amsterdam, onde a infraestrutura ciclística já é exemplar, a manutenção e atualização contínuas são essenciais para
preservar a alta qualidade das vias existentes, principalmente em face do desenvolvimento urbano acelerado. A inovação
também deve ser uma constante, com a adoção de tecnologias avançadas para melhorar a segurança e a experiência dos
ciclistas, como sistemas de iluminação e sinalização inteligentes, assegurando que a cidade continue a ser uma
referência mundial em mobilidade ciclística.

#### 5.3 Berlim

Berlim enfrenta o desafio de adaptar uma infraestrutura histórica para acomodar as necessidades modernas de ciclismo.
Como melhorias, investimentos em zonas de baixa emissão podem promover a utilização de bicicletas, enquanto a criação
de 'ciclovias expressas' pode encorajar os ciclistas a optarem por percursos mais longos, aliviando assim a pressão
sobre outros meios de transporte. A colaboração entre planejadores urbanos e a comunidade ciclística será crucial para
identificar e superar os obstáculos à construção de novas ciclovias.


**Autores:**

- [Jordan Marques de Almeida Ramos](https://github.com/jordanmaramos)
- [Pedro Rego Vilar Neto](https://github.com/pedrorvn)
- [Vinícius Yan Tavares Nascimento](https://github.com/yantvrs)

https://drive.google.com/drive/folders/19XuXnEDAyT_7T_dYFCt_2Vhf2CVDecEb
