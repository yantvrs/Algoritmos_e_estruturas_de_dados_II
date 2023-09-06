# Autocompleting Words using AVL Tree 🌳

This repository contains a Python implementation of a word autocompletion system using an AVL Tree.

## Prerequisites 📋

Before running the code, make sure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

## Corpus Preprocessing 🔍

- The text corpus is loaded and preprocessed for preparation.

### Conversion to Lowercase

- All text is converted to lowercase to ensure consistency.

### Removal of Punctuation and Special Characters

- Punctuation and special characters are removed to extract only words.

### Word Tokenization

- The text is split into individual words to build the corpus.

### Removal of Stopwords (Optional)

- Stopwords such as "and," "or," "but," "the," "a," "an," etc., can be removed, depending on your needs.

## Construction of AVL Tree 🌳

- All unique words from the corpus are inserted into an AVL Tree for efficient word lookup.

## Autocompleting Words 🚀

- A function is implemented to find complete words that start with a given prefix.

## Performance Analysis ⏱️

### Comparison with Simple Data Structures

- We compare the performance of the AVL Tree with simpler data structures, such as an unordered list and an unbalanced binary search tree.

### Impact of Corpus Size

- We analyze how the size of the corpus affects the performance of the AVL Tree.

## How to Run the Code ▶️

- Instructions on how to run the code in your environment are available in the `main.py` file.

## Usage Examples 💡

- Provide examples of how to use the word autocompletion system with text samples or a corpus.

## Authors 👨‍💻👩‍💻

- [Yan Tavares](https://github.com/yantvrs)
- [Emanoel Batista](https://github.com/EmanoelBatista)

## Explainer Video 📹

- Watch the explanatory video [here](https://www.loom.com/share/8ad76d9bef3d4986992ab2d3bb1abe56?sid=d0bcd515-0ba4-4769-9407-339271528f16).

## Contributions 🤝

- If you wish to contribute to this project, please open a pull request and describe your changes.

## Issues and Suggestions 🐛

- If you encounter any issues or have suggestions, please open an issue.

## License 📜

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
