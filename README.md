# Indic Unified Parser Dictionary Comparison

This script compares words in an old dictionary with the new Indic Unified Parser. It identifies errors in parsing and provides a total error rate.

## Instructions

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Update `checkdict.py`:

    - Modify the paths/imports for the old dictionary, new parser (if any), and the output file.
    - Save the changes.

3. Run the script:

    ```bash
    python checkdict.py
    ```

4. Check the output file for words with errors.

## Script Details

- `dict_location`: Path to the old dictionary file.
- `indic_unified_parser.uparser`: Import for the new Indic Unified Parser model.
- `output.txt`: Path to the output file that will store words with errors.

## Output

The script generates an output file with words that were parsed incorrectly and calculates the total error rate.

Feel free to customize the script as needed for your specific requirements.
