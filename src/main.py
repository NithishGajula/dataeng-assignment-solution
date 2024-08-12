import os
from spec_loader import load_spec
from file_generator import generate_fixed_width_file
from file_parser import parse_fixed_width_to_csv

def main():
    spec_file = os.path.join(os.path.dirname(__file__), '..', 'spec.json')
    spec = load_spec(spec_file)

    fixed_width_file = "fixed_width_file.txt"
    csv_file = "output.csv"

    data = [
        ["12345", "abcdefghijk", "123", "12", "abcdefghijklm", "1234567", "abcdefghij", "abcdefghijklm", "abcdefghijklmnopqrst", "abcdefghijklm"],
        ["12345", "abcdefghijk", "123", "12", "abcdefghijklm", "1234567", "abcdefghij", "abcdefghijklm", "abcdefghijklmnopqrst", "abcdefghijklm"],
        ["12345", "abcdefghijk", "123", "12", "abcdefghijklm", "1234", "abcdefghij", "abcdefghijklm", "abcdefghijklmnopqrst", "abcdefghijklm"],
        ["12345", "abcdefghijk", "123", "12", "abcdefghi", "1234567", "abcdefghij", "abcdefghijklm", "abcdefghijklmnopqrst", "abcdefghijklm"],
        ["12345", "abcdefghijk", "123", "12", "abcdefghijklm", "1234567", "abcdefghij", "abcdefghijklm", "abcdefghijklmn", "abcdefghijklm"],
        ["12345", "abcdefghijk", "123", "12", "abcdefghi", "1234567", "abcdefghij", "abcdefghijklm", "abcdefghijklmnopqrst", "abcdefghijklm"]
    ]

    generate_fixed_width_file(spec, data, fixed_width_file)

    parse_fixed_width_to_csv(spec, fixed_width_file, csv_file)

if __name__ == "__main__":
    main()
