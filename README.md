# JSON Compare and Translate

## Overview

**JSON Compare and Translate** is a Python tool designed to compare two JSON files, identify differences in their keys and values, and automatically translate missing entries using the DeepL API. This is especially useful for maintaining multilingual resource files in software projects.

## Features

- **Compare JSON Files:** Check if two JSON files are identical or different.
- **Find Differences:** List keys and values that differ between two files.
- **Identify Missing Keys:** Detect keys present in one file but missing in the other.
- **Translate Missing Entries:** Automatically translate missing values from one file to another using DeepL, with the target language inferred from the filename.
- **Fast Comparison:** Efficient algorithms for large, sorted files.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/samulen/json-compare-and-translate.git
    ```
2. Install dependencies:
The project uses pipenv for package management.
    ```
    pip install pipenv
    pipenv install
    ```
3. Create a `.env` file in the project root and add your DeepL API key:
    ```
    YOUR_DEEPL_API_KEY=your_deepl_api_key_here
    ```

## Usage

### Compare Files

```python
from comparer import comparer

result = comparer('en.json', 'de.json').compare()
print(result)
```

### Find Differences

```python
diffs = comparer('en.json', 'de.json').diffs()
print(diffs)
```

### Find Missing Keys

```python
missing_in_de, missing_in_en = comparer('en.json', 'de.json').missing()
print("Missing in de.json:", missing_in_de)
print("Missing in en.json:", missing_in_en)
```

### Translate Missing Entries

```python
from translator import translator

translations = translator('en.json', 'de.json').translate_diffs()
print(translations)
```

## Configuration

- The target language for translation is automatically determined from the first two characters of the second file's name (e.g., `de.json` → `DE`).
- Ensure your JSON files are UTF-8 encoded.

## License

This project is licensed under the MIT License.

## Contributing

Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.

## Contact

For questions or support, please contact [your.email@example.com](mailto:your.email@example.com)