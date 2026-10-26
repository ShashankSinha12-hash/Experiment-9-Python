import csv
import json
from pathlib import Path


def convert_csv_to_json(csv_file_path: str, json_file_path: str) -> None:
    """Reads a CSV file and converts it into a formatted JSON output file."""
    csv_path = Path(csv_file_path)
    json_path = Path(json_file_path)

    # 1. Verify the source file exists
    if not csv_path.is_file():
        raise FileNotFoundError(f"The source file '{csv_file_path}' does not exist.")

    # 2. Read CSV data and parse rows into dictionaries using the header row
    # 'newline=""' is recommended by the csv module documentation to manage line endings properly.
    with csv_path.open(mode="r", newline="", encoding="utf-8") as csv_file:
        # csv.DictReader maps the header row fields to values in each subsequent row
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    # 3. Write the parsed array of dictionaries to a JSON file
    with json_path.open(mode="w", encoding="utf-8") as json_file:
        # indent=4 formats the output neatly for human readability
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"Success: Converted '{csv_file_path}' to '{json_file_path}'.")


if __name__ == "__main__":
    # Define file paths
    input_csv = "data.csv"
    output_json = "data.json"

    # Run the conversion
    try:
        convert_csv_to_json(input_csv, output_json)
    except Exception as e:
        print(f"Error during conversion: {e}")
