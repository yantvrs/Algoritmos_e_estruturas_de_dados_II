# Complexidade Algorítmica

Neste projeto, implementamos várias funções para consulta de inventário de laptops. Abaixo, analisamos a complexidade de tempo de algumas dessas funções em relação aos aspectos de Big O, Big Theta (Θ) e Big Omega (Ω):

## 1) `get_laptop_from_id`:

- **Big O (O(n))**: A complexidade deste método é linear, onde "n" representa o número de laptops no inventário (ou o tamanho da lista `self.rows`). Isso ocorre porque o algoritmo percorre todas as linhas da lista uma vez para procurar um laptop com um ID correspondente. No pior caso, ele pode precisar percorrer todas as linhas antes de encontrar o laptop desejado.
- **Big Theta (Θ(n))**: A complexidade é linear porque, no melhor e no pior caso, o algoritmo sempre percorre todas as linhas da lista.
- **Big Omega (Ω(1))**: No melhor caso, se o laptop desejado estiver na primeira linha da lista, o algoritmo terminará imediatamente, o que seria uma complexidade constante.

## 2) `get_laptop_from_id_fast`:

- **Big O (O(1))**: A complexidade deste método é constante, ou seja, independente do tamanho da lista `self.rows` ou do número de laptops no inventário. Isso ocorre porque o acesso a um valor em um dicionário (usando a chave) é uma operação de tempo constante.
- **Big Theta (Θ(1))**: A complexidade é constante, pois a operação de acesso ao dicionário é sempre executada em tempo constante.
- **Big Omega (Ω(1))**: No melhor caso, quando o laptop desejado está no dicionário na primeira tentativa, o algoritmo terminará imediatamente, o que é uma complexidade constante.

## 3) `check_promotion_dollars`:

- **Big O (O(n^2))**: A complexidade deste método é quadrática, onde "n" representa o número de laptops no inventário. Isso ocorre porque ele possui um loop dentro de outro loop, verificando todas as combinações possíveis de preços. No pior caso, ele precisará verificar todas as combinações, resultando em uma complexidade quadrática.
- **Big Theta (Θ(n^2))**: A complexidade é quadrática, pois, no melhor e no pior caso, o algoritmo precisa verificar todas as combinações possíveis de preços.
- **Big Omega (Ω(n))**: No melhor caso, se houver uma correspondência direta com um laptop, o algoritmo terminará imediatamente, o que seria uma complexidade linear.

## 4) `check_promotion_dollars_fast`:

- **Big O (O(1))**: A complexidade deste método é constante, pois a verificação da existência de um preço em um conjunto (set) é uma operação de tempo constante.
- **Big Theta (Θ(1))**: A complexidade é constante, pois a operação de verificação no conjunto é sempre executada em tempo constante.
- **Big Omega (Ω(1))**: No melhor caso, quando o preço desejado já existe no conjunto, o algoritmo terminará imediatamente, o que é uma complexidade constante.


## 5) `find_laptops_in_price_range`

- **Big O (O(n))**: A complexidade deste algoritmo é linear, onde "n" representa o número de laptops no inventário (ou o tamanho da lista `self.rows`). Isso ocorre porque o algoritmo percorre cada linha da lista uma vez, verificando se o preço está dentro da faixa especificada. No pior caso, ele pode precisar percorrer todas as linhas da lista.

- **Big Theta (Θ(n))**: A complexidade é linear porque, no melhor e no pior caso, o algoritmo sempre percorre todas as linhas da lista.

- **Big Omega (Ω(1))**: No melhor caso, se o primeiro laptop na lista estiver dentro da faixa de preço especificada, o algoritmo terminará imediatamente, o que seria uma complexidade constante. No entanto, isso é improvável na prática, e o caso médio e o pior caso têm complexidade linear.

## 6) `find_cheapest_laptop_with_specifications`

- **Big O (O(n))**: A complexidade deste algoritmo é linear, onde "n" representa o número de laptops no inventário (ou o tamanho da lista `self.rows`). Isso ocorre porque o algoritmo percorre cada linha da lista uma vez, verificando as especificações de RAM e armazenamento.

- **Big Theta (Θ(n))**: A complexidade é linear porque, no melhor e no pior caso, o algoritmo sempre percorre todas as linhas da lista.

- **Big Omega (Ω(1))**: No melhor caso, se o primeiro laptop na lista atender às especificações, o algoritmo terminará imediatamente, o que seria uma complexidade constante. No entanto, isso é improvável na prática, e o caso médio e o pior caso têm complexidade linear.

Essas análises de complexidade nos ajudam a entender o desempenho das funções e a escolher a implementação mais eficiente, dependendo dos requisitos do projeto.