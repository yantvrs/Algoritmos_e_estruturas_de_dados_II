# Autocompletar Palavras usando Árvore AVL 🌳

Este repositório contém uma implementação em Python de um sistema de autocompletar palavras utilizando uma Árvore AVL.

## Pré-requisitos 📋

Antes de executar o código, certifique-se de ter instalado o Python em sua máquina. Você pode fazer o download do Python em [python.org](https://www.python.org/downloads/).

## Pré-processamento do Corpus 🔍

- O corpus de texto é carregado e pré-processado para preparação.

### Conversão para Minúsculas

- Todo o texto é convertido para letras minúsculas para garantir consistência.

### Remoção de Pontuação e Caracteres Especiais

- Pontuações e caracteres especiais são removidos para extrair apenas palavras.

### Divisão em Palavras

- O texto é dividido em palavras individuais para construir o corpus.

### Remoção de Palavras de Parada (Opcional)

- Palavras de parada, como "e", "ou", "mas", "a", "o", etc., podem ser removidas, dependendo das necessidades.

## Construção da Árvore AVL 🌳

- Todas as palavras únicas do corpus são inseridas em uma Árvore AVL para facilitar a busca.

## Autocompletar Palavras 🚀

- Uma função é implementada para encontrar palavras completas que começam com um determinado prefixo.

## Análise de Desempenho ⏱️

### Comparação com Estruturas Simples

- Comparamos o desempenho da Árvore AVL com estruturas mais simples, como uma lista não ordenada e uma árvore binária de busca não balanceada.

### Impacto do Tamanho do Corpus

- Analisamos como o tamanho do corpus afeta o desempenho da Árvore AVL.

## Como Executar o Código ▶️

- Instruções sobre como executar o código em seu ambiente estão disponíveis no arquivo `main.py`.

## Exemplo de Uso 💡

- Mostre exemplos de como usar o sistema de autocompletar palavras com amostras de texto ou corpus.

## Autores 👨‍💻👩‍💻

- [Yan Tavares](https://github.com/yantvrs)
- [Emanoel Batista](https://github.com/EmanoelBatista)

## Vídeo Explicativo 📹

- Assista ao vídeo explicativo [aqui](link do vídeo no Loom).

## Contribuições 🤝

- Se você deseja contribuir para este projeto, por favor, abra uma _pull request_ e descreva suas alterações.

## Problemas e Sugestões 🐛

- Se encontrar algum problema ou tiver sugestões, por favor, abra uma _issue_.

## Licença 📜

Este projeto está sob a Licença MIT - consulte o arquivo [LICENSE.md](LICENSE.md) para detalhes.

