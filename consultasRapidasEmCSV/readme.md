# Projeto de Inventário de Laptops

Este projeto envolve a criação de uma classe chamada `Inventory` para representar um inventário de laptops em uma loja online. A classe implementa métodos para responder a várias perguntas comerciais sobre o estoque de laptops. Os dados do inventário são armazenados em um arquivo CSV chamado `laptops.csv`.

## Vídeo explicativo

Assista ao vídeo explicativo [aqui](https://www.loom.com/share/cde99f21e8d04f1c8d04f3ace932095a?sid=183ea0e4-e5c6-43a5-8577-47e26a7d131c).

## Estrutura do Projeto

O projeto é organizado em várias etapas, cada uma adicionando funcionalidades à classe `Inventory`:

### Etapa 1: Leitura dos Dados

Nesta etapa, os dados do arquivo CSV são lidos e armazenados em uma lista.

### Etapa 2: Consulta por ID

Foi implementado o método `get_laptop_from_id` para encontrar os dados de um laptop com base em seu ID.

### Etapa 3: Otimização de Consulta por ID

Para melhorar a eficiência da consulta por ID, foi adicionado um dicionário `id_to_row` que mapeia IDs de laptop para suas linhas correspondentes no CSV. Isso acelera a pesquisa de laptops por ID.

### Etapa 4: Verificação de Promoção

Foi criado o método `check_promotion_dollars` para verificar se é possível encontrar um laptop ou uma combinação de laptops cujo preço total seja igual a uma quantia em dinheiro especificada.

### Etapa 5: Otimização da Verificação de Promoção

Para otimizar a verificação de promoção, foi adicionado um conjunto `prices` que armazena os preços únicos de laptops. Isso permite verificar se um preço específico existe no conjunto em tempo constante, acelerando a verificação.

### Etapa 6: Pesquisa por Faixa de Preço

Foi implementado o método `find_laptops_in_price_range` para encontrar todos os laptops cujos preços estejam dentro de uma determinada faixa.

### Etapa 7: Encontrar o Laptop Mais Barato com Especificações

Foi criado o método `find_cheapest_laptop_with_specifications` para encontrar o laptop mais barato que atenda a determinados critérios de RAM e armazenamento.

## Uso da Classe

A classe `Inventory` pode ser usada para consultar informações sobre laptops no inventário, verificar promoções e encontrar laptops dentro de faixas de preço específicas. Abaixo estão alguns exemplos de uso:

```python
# Criar uma instância do inventário
inventory = Inventory('laptops.csv')

# Consultar informações de um laptop por ID
laptop_info = inventory.get_laptop_from_id('3362737')

# Verificar promoções
promotion_result = inventory.check_promotion_dollars(1000)

# Encontrar laptops dentro de uma faixa de preço
laptops_in_range = inventory.find_laptops_in_price_range(500, 1000)

# Encontrar o laptop mais barato com especificações desejadas
cheapest_laptop = inventory.find_cheapest_laptop_with_specifications(8, 256)
```
# Desenvolvedores

 - [Emanoel Batista](https://github.com/EmanoelBatista)
 - [Yan Tavares](https://github.com/yantvrs)
