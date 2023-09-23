# Complexidade Algorítmica

Neste projeto, as funções `find_laptops_in_price_range` e `find_cheapest_laptop_with_specifications` são essenciais para realizar consultas específicas no inventário de laptops. Abaixo, explicamos a complexidade algorítmica dessas funções:

## 1) find_laptops_in_price_range

- **Big O (O(n))**: A complexidade deste algoritmo é linear, onde "n" representa o número de laptops no inventário (ou o tamanho da lista `self.rows`). Isso ocorre porque o algoritmo percorre cada linha da lista uma vez, verificando se o preço está dentro da faixa especificada. No pior caso, ele pode precisar percorrer todas as linhas da lista.

- **Big Theta (Θ(n))**: A complexidade é linear porque, no melhor e no pior caso, o algoritmo sempre percorre todas as linhas da lista.

- **Big Omega (Ω(1))**: No melhor caso, se o primeiro laptop na lista estiver dentro da faixa de preço especificada, o algoritmo terminará imediatamente, o que seria uma complexidade constante. No entanto, isso é improvável na prática, e o caso médio e o pior caso têm complexidade linear.

## 2) find_cheapest_laptop_with_specifications

- **Big O (O(n))**: A complexidade deste algoritmo é linear, onde "n" representa o número de laptops no inventário (ou o tamanho da lista `self.rows`). Isso ocorre porque o algoritmo percorre cada linha da lista uma vez, verificando as especificações de RAM e armazenamento.

- **Big Theta (Θ(n))**: A complexidade é linear porque, no melhor e no pior caso, o algoritmo sempre percorre todas as linhas da lista.

- **Big Omega (Ω(1))**: No melhor caso, se o primeiro laptop na lista atender às especificações, o algoritmo terminará imediatamente, o que seria uma complexidade constante. No entanto, isso é improvável na prática, e o caso médio e o pior caso têm complexidade linear.

Ambas as funções têm uma complexidade de tempo linear (O(n)) porque percorrem a lista de laptops uma vez. Elas têm a mesma complexidade de melhor caso (Ω(1)), que é muito raro na prática, e a complexidade média e de pior caso é linear devido à necessidade de percorrer todas as linhas da lista em busca de correspondências.