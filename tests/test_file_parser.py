import unittest
import os
import csv
from io import StringIO
from src.file_parser import parse_fixed_width_to_csv, FileParserError

class TestFileParser(unittest.TestCase):

    def setUp(self):
        self.input_file = 'test_input.txt'
        self.output_file = 'test_output.csv'

        self.spec = {
            "Offsets": [5, 12, 3, 2, 13, 7, 10, 13, 20, 13],
            "FixedWidthEncoding": "windows-1252",
            "DelimitedEncoding": "utf-8"
        }

        self.data = [
            "123  abcdefghij  1  x  yyyyyyyyyy   z      12345     aaaaa        bbbbbbbbbbbbbbb     cccccccccc  ",
            "4567 klmnopqrstuv23 yz aaaaaaaaaaa  bb     67890     cccccc       dddddddddd          eeeeeeeee   ",
        ]

        with open(self.input_file, 'w', encoding=self.spec['FixedWidthEncoding']) as f:
            for line in self.data:
                f.write(line + '\n')

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_parse_fixed_width_to_csv_valid(self):
        parse_fixed_width_to_csv(self.spec, self.input_file, self.output_file)

        self.assertTrue(os.path.exists(self.output_file))

        expected_rows = [
            ["123", "abcdefghij", "1", "x", "yyyyyyyyyy", "z", "12345", "aaaaa", "bbbbbbbbbbbbbbb", "cccccccccc"],
            ["4567", "klmnopqrstuv", "23", "yz", "aaaaaaaaaaa", "bb", "67890", "cccccc", "dddddddddd", "eeeeeeeee"],
        ]

        with open(self.output_file, 'r', encoding=self.spec['DelimitedEncoding']) as csv_file:
            reader = csv.reader(csv_file)
            for i, row in enumerate(reader):
                self.assertEqual(row, expected_rows[i])

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            parse_fixed_width_to_csv(self.spec, 'non_existent_file.txt', self.output_file)

    def test_invalid_output_path(self):
        invalid_path = '/invalid/path/output.csv'
        with self.assertRaises(FileParserError):
            parse_fixed_width_to_csv(self.spec, self.input_file, invalid_path)

    def test_empty_file(self):
        empty_file = 'empty_input.txt'
        with open(empty_file, 'w', encoding=self.spec['FixedWidthEncoding']) as f:
            f.write('')

        try:
            parse_fixed_width_to_csv(self.spec, empty_file, self.output_file)

            self.assertTrue(os.path.exists(self.output_file))
            with open(self.output_file, 'r', encoding=self.spec['DelimitedEncoding']) as csv_file:
                reader = csv.reader(csv_file)
                rows = list(reader)
                self.assertEqual(len(rows), 0)
        finally:
            os.remove(empty_file)

