# Laptop Inventory Project

This project involves creating a class called `Inventory` to represent an inventory of laptops in an online store. The class implements methods to answer various business questions about the laptop stock. Inventory data is stored in a CSV file called `laptops.csv`.

## 🎥 Video Explanation

Watch the explanatory video [here](https://www.loom.com/share/cde99f21e8d04f1c8d04f3ace932095a?sid=183ea0e4-e5c6-43a5-8577-47e26a7d131c).

## 📈 Algorithmic Complexity Analysis

To access the algorithmic complexity analysis, simply click [here](https://github.com/yantvrs/Data_structure_2/blob/main/consultasRapidasEmCSV/complexity.md).

## Project Structure

The project is organized into several stages, each adding functionality to the `Inventory` class:

### 🚀 Stage 1: Data Reading

In this stage, data from the CSV file is read and stored in a list.

### 🚀 Stage 2: Query by ID

The `get_laptop_from_id` method is implemented to find the data of a laptop based on its ID.

### 🚀 Stage 3: Query by ID Optimization

To improve the efficiency of querying by ID, an `id_to_row` dictionary has been added, mapping laptop IDs to their corresponding rows in the CSV. This speeds up laptop searches by ID.

### 🚀 Stage 4: Promotion Checking

The `check_promotion_dollars` method has been created to check if it is possible to find a laptop or a combination of laptops whose total price equals a specified amount of money.

### 🚀 Stage 5: Promotion Checking Optimization

To optimize promotion checking, a `prices` set has been added that stores unique laptop prices. This allows checking if a specific price exists in the set in constant time, speeding up the verification process.

### 🚀 Stage 6: Price Range Search

The `find_laptops_in_price_range` method has been implemented to find all laptops whose prices fall within a certain range.

### 🚀 Stage 7: Finding the Cheapest Laptop with Specifications

The `find_cheapest_laptop_with_specifications` method has been created to find the cheapest laptop that meets certain RAM and storage criteria.

## Using the Class

The `Inventory` class can be used to query information about laptops in the inventory, check promotions, and find laptops within specific price ranges. Below are some usage examples:

```python
# Create an inventory instance
inventory = Inventory('laptops.csv')

# Query laptop information by ID
laptop_info = inventory.get_laptop_from_id('3362737')

# Check promotions
promotion_result = inventory.check_promotion_dollars(1000)

# Find laptops within a price range
laptops_in_range = inventory.find_laptops_in_price_range(500, 1000)

# Find the cheapest laptop with desired specifications
cheapest_laptop = inventory.find_cheapest_laptop_with_specifications(8, 256)

```
# Developers

 - [Emanoel Batista](https://github.com/EmanoelBatista)
 - [Yan Tavares](https://github.com/yantvrs)
