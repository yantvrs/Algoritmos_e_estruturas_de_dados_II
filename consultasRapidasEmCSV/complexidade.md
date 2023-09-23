# Algorithmic Complexity

In this project, we have implemented various functions for querying laptop inventory. Below, we analyze the time complexity of some of these functions in terms of Big O, Big Theta (Θ), and Big Omega (Ω):

## 1) `__init__(self, csv_filename)`:

- **Big O (O(n))**: The complexity of this constructor is linear with respect to the number of lines in the CSV file, where "n" represents the number of lines. This is because it reads each line of the file and performs constant-time operations to create data structures like self.rows, self.id_to_row, and self.prices.
- **Big Theta (Θ(n))**: The complexity is linear since the constructor traverses all lines of the file and performs constant-time operations for each line.
- **Big Omega (Ω(n))**: The complexity is linear in the best case, which occurs when the CSV file contains only one line. Even in this case, all reading and data structure creation operations still need to be executed.

## 2) `get_laptop_from_id`:

- **Big O (O(n))**: The complexity of this method is linear, where "n" represents the number of laptops in the inventory (or the size of the `self.rows` list). This is because the algorithm traverses all lines of the list once to search for a laptop with a matching ID. In the worst case, it may need to traverse all lines before finding the desired laptop.
- **Big Theta (Θ(n))**: The complexity is linear because, in both the best and worst cases, the algorithm always traverses all lines of the list.
- **Big Omega (Ω(1))**: In the best case, if the desired laptop is in the first line of the list, the algorithm will finish immediately, which would be constant complexity.

## 3) `get_laptop_from_id_fast`:

- **Big O (O(1))**: The complexity of this method is constant, i.e., independent of the size of the `self.rows` list or the number of laptops in the inventory. This is because accessing a value in a dictionary (using the key) is a constant-time operation.
- **Big Theta (Θ(1))**: The complexity is constant because the dictionary access operation is always executed in constant time.
- **Big Omega (Ω(1))**: In the best case, when the desired laptop is already in the dictionary, the algorithm will finish immediately, which is constant complexity.

## 4) `check_promotion_dollars`:

- **Big O (O(n^2))**: The complexity of this method is quadratic, where "n" represents the number of laptops in the inventory. This is because it has one loop inside another loop, checking all possible combinations of prices. In the worst case, it needs to check all combinations, resulting in quadratic complexity.
- **Big Theta (Θ(n^2))**: The complexity is quadratic because, in both the best and worst cases, the algorithm needs to check all possible combinations of prices.
- **Big Omega (Ω(n))**: In the best case, if there is a direct match with a laptop, the algorithm will finish immediately, which is linear complexity.

## 5) `check_promotion_dollars_fast`:

- **Big O (O(1))**: The complexity of this method is constant because checking for the existence of a price in a set is a constant-time operation.
- **Big Theta (Θ(1))**: The complexity is constant because the set checking operation is always executed in constant time.
- **Big Omega (Ω(1))**: In the best case, when the desired price already exists in the set, the algorithm will finish immediately, which is constant complexity.

## 6) `find_laptops_in_price_range`

- **Big O (O(n))**: The complexity of this algorithm is linear, where "n" represents the number of laptops in the inventory (or the size of the `self.rows` list). This is because the algorithm traverses each line of the list once, checking if the price is within the specified range. In the worst case, it may need to traverse all lines of the list.
- **Big Theta (Θ(n))**: The complexity is linear because, in both the best and worst cases, the algorithm always traverses all lines of the list.
- **Big Omega (Ω(1))**: In the best case, if the first laptop in the list is within the specified price range, the algorithm will finish immediately, which would be constant complexity. However, this is unlikely in practice, and the average and worst cases have linear complexity.

## 7) `find_cheapest_laptop_with_specifications`

- **Big O (O(n))**: The complexity of this algorithm is linear, where "n" represents the number of laptops in the inventory (or the size of the `self.rows` list). This is because the algorithm traverses each line of the list once, checking RAM and storage specifications.
- **Big Theta (Θ(n))**: The complexity is linear because, in both the best and worst cases, the algorithm always traverses all lines of the list.
- **Big Omega (Ω(1))**: In the best case, if the first laptop in the list meets the specifications, the algorithm will finish immediately, which would be constant complexity. However, this is unlikely in practice, and the average and worst cases have linear complexity.

These complexity analyses help us understand the performance of the functions and choose the most efficient implementation depending on the project's requirements.
