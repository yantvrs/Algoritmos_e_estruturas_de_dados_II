# Small Worlds

## Visão Geral

O projeto Small Worlds é uma projeto acadêmico que se concentra na análise de cinco redes de grafos distintas, explorando suas características e, mais especificamente, investigando conceitos de assortatividade, distâncias, componentes conectados e Coeficiente de Clustering. Este projeto é parte de um esforço mais amplo para aprofundar nosso entendimento de redes complexas e contribuir para o campo da teoria dos grafos.

## Exploração de Conteúdos 📚

O projeto "Small Worlds" explora os seguintes conceitos-chave:

1. **Amazon Product Co-purchasing Network, June 01 2003**:
   - Esta rede foi coletada ao rastrear o site da Amazon. Ela se baseia na função "Customers Who Bought This Item Also Bought". Basicamente, se dois produtos (i e j) são frequentemente comprados juntos por clientes, há uma conexão direcionada de i para j no grafo. Os dados dessa rede foram coletados em junho de 2003.

2. **Gnutella Peer-to-peer Network, August 4 2002**:
   - Esta rede é uma coleção de instantâneos da rede de compartilhamento de arquivos peer-to-peer Gnutella de agosto de 2002. Cada instantâneo representa o estado da rede em um momento específico. Os nós representam hosts na rede Gnutella, e as arestas indicam as conexões entre esses hosts.

3. **Slashdot Signed Social Network, November 2008**:
   - O Slashdot é um site de notícias de tecnologia conhecido por sua comunidade de usuários ativos. Em 2002, o Slashdot introduziu o recurso "Slashdot Zoo", que permite que os usuários marquem outros usuários como amigos ou inimigos. Nessa rede, as conexões representam amizades ou inimizades entre os usuários do Slashdot. Os dados foram coletados em novembro de 2008.

4. **CollegeMsg Temporal Network**:
   - Este conjunto de dados consiste em mensagens privadas enviadas em uma rede social online da Universidade da Califórnia, Irvine. Cada mensagem é representada por uma aresta (u, v, t), indicando que o usuário u enviou uma mensagem privada para o usuário v em um momento específico. O conjunto de dados foi organizado para ser facilmente carregado em uma estrutura de rede temporal.

5. **Email-EU-Core Network**:
   - Essa rede é derivada de dados de e-mails de uma grande instituição de pesquisa europeia. Ela representa a comunicação entre membros da instituição, e uma aresta (u, v) indica que a pessoa u enviou pelo menos um e-mail para a pessoa v. Além disso, o conjunto de dados contém informações sobre a qual departamento da instituição cada indivíduo pertence, permitindo análises de comunidades.


## Requisitos do Projeto 📋

O projeto "Small Worlds" é composto por três requisitos principais:

### Requisito 1: Escolha de Redes 🌐

O primeiro requisito do projeto envolve a escolha de pelo menos 5 redes no site [Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/). Essas redes servirão como base para a análise de assortatividade e outros atributos.

As cinco redes selecionadas para análise no projeto "Small Worlds" incluem:


1. **Amazon Product Co-purchasing Network, June 01 2003**:
   - **Informações do Conjunto de Dados**: Esta rede foi coletada rastreando o site da Amazon e baseia-se na funcionalidade "Customers Who Bought This Item Also Bought" do site. Se um produto i for frequentemente coadquirido com o produto j, o grafo contém uma aresta direcionada de i para j. Os dados foram coletados em junho de 2003.

2. **Gnutella Peer-to-peer Network, August 4 2002**:
   - **Informações do Conjunto de Dados**: Esta rede consiste em uma sequência de instantâneos da rede de compartilhamento de arquivos peer-to-peer Gnutella a partir de agosto de 2002. Existem um total de 9 instantâneos da rede Gnutella coletados em agosto de 2002. Os nós representam hosts na topologia da rede Gnutella e as arestas representam conexões entre os hosts.

3. **Slashdot Signed Social Network, November 2008**:
   - **Informações do Conjunto de Dados**: O Slashdot é um site de notícias relacionadas à tecnologia conhecido por sua comunidade de usuários específica. Em 2002, o Slashdot introduziu o recurso Slashdot Zoo, que permite que os usuários marquem uns aos outros como amigos ou inimigos. A rede contém links de amigo/inimigo entre os usuários do Slashdot. Os dados foram obtidos em novembro de 2008.

4. **CollegeMsg Temporal Network**:
   - **Informações do Conjunto de Dados**: Este conjunto de dados é composto por mensagens privadas enviadas em uma rede social online na Universidade da Califórnia, Irvine. Os usuários podiam procurar outros na rede e, em seguida, iniciar conversas com base nas informações de perfil. Uma aresta (u, v, t) significa que o usuário u enviou uma mensagem privada para o usuário v no momento t. O conjunto de dados foi parseado para que possa ser carregado diretamente no SNAP como uma rede temporal.

5. **Email-EU-Core Network**:
   - **Informações do Conjunto de Dados**: Esta rede foi gerada usando dados de e-mail de uma grande instituição de pesquisa europeia. Os e-mails representam a comunicação entre membros da instituição (o núcleo) e a rede contém uma aresta (u, v) se a pessoa u enviou pelo menos um e-mail para a pessoa v. O conjunto de dados também contém associações de comunidade "ground-truth" dos nós, onde cada indivíduo pertence a exatamente um dos 42 departamentos da instituição de pesquisa.

Essas redes servirão como base para a análise de assortatividade, distâncias, componentes conectados e coeficiente de clustering no projeto "Small Worlds".

### [Requisito 2](https://github.com/yantvrs/Data_structure_2/tree/main/U2T2/Requisito_02): Análise de Assortatividade 📈

Para cada uma das redes escolhidas, o projeto realizará uma análise de assortatividade em relação ao grau dos nós da rede. Isso ajudará a compreender como os nós se associam com base em seu grau na rede.

### [Requisito 3](https://github.com/yantvrs/Data_structure_2/tree/main/U2T2/Requisito_03): Implementação da Tabela de Atributos 📊

O terceiro requisito envolve a implementação de uma tabela que descreve as relações dos atributos calculados, incluindo a assortatividade. Esta tabela será uma parte essencial da documentação do projeto.


## Tecnologias Utilizadas 💻

- **Python**: A linguagem de programação principal usada para desenvolver o projeto.

## Compilação do Código 🚀

Para compilar e executar o código Python do projeto Small Words, siga estas etapas:

1. **Instalação do Python**: Certifique-se de ter o Python instalado no seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

2. **Instalação das Bibliotecas**: Use o gerenciador de pacotes `pip` para instalar as bibliotecas necessárias. Por exemplo:

```bash
   pip install numpy matplotlib
```

3. **Execução do Código**: Use o interpretador Python para executar o código principal do projeto. Por exemplo:

```bash
   python main.py
```

## Desenvolvedor 👨‍💻

[Yan Tavares](https://github.com/yantvrs)
