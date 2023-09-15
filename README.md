# CSV-based File Copier

This script allows users to search for and copy files specified in a CSV to another directory.

## Features

- Searches a given directory (and its subdirectories) for files.
- Takes file names from a CSV and looks for them.
- Copies found files to another directory.

## Prerequisites

- Python 3.x
- pandas (`pip install pandas`)

## How to Use

1. **Run the script:**
    ```bash
    python csv-file-search-and-copy
    ```

2. **Input the directory to search in:**
    ```
    Enter the directory to search in: /path/to/search/directory
    ```

3. **Input the directory to copy the files to:**
    ```
    Enter the directory to copy the files to: /path/to/copy/directory
    ```

4. **Input the location of the CSV file:**
    ```
    Enter the location of the CSV file: /path/to/csv_file.csv
    ```

    The CSV should have a column named "File name" containing the names of the files to be searched.

5. The script will then search for the files in the specified directory (and its subdirectories). If found, it will copy each file to the destination directory and notify you with a message:
    ```
    Copied file example.txt to /path/to/copy/directory
    ```

## Error Handling

If the specified CSV file is not found, the script will notify you with:
```
CSV file not found. Please check the file path and try again.
```

## Support the Developer

If you found this helpful, please consider:

- **Buymeacoffee:** [Link](http://buymeacoffee.com/alteredadmin)
