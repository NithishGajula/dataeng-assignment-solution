import unittest
import os
from src.file_generator import generate_fixed_width_file, FileGeneratorError

class TestFileGenerator(unittest.TestCase):
    def setUp(self):
        self.output_file = 'test_output.txt'
        self.spec = {
            "ColumnNames": ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
            "Offsets": [5, 12, 3, 2, 13, 7, 10, 13, 20, 13],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }
        self.data = [
            ["123", "abcdefghij", "1", "x", "y"*10, "z", "12345", "a"*5, "b"*15, "c"*10],
            ["4567", "klmnopqrstuv", "23", "yz", "a"*11, "b"*2, "67890", "c"*6, "d"*10, "e"*9],
        ]

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_fixed_width_file_valid(self):
        generate_fixed_width_file(self.spec, self.data, self.output_file)

        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r', encoding=self.spec['FixedWidthEncoding']) as file:
            lines = file.readlines()

        expected_lines = [
            "f1   f2          f3 f4f5           f6     f7        f8           f9                  f10          \n",
            "123  abcdefghij  1  x yyyyyyyyyy   z      12345     aaaaa        bbbbbbbbbbbbbbb     cccccccccc   \n",
            "4567 klmnopqrstuv23 yzaaaaaaaaaaa  bb     67890     cccccc       dddddddddd          eeeeeeeee    \n"
        ]

        self.assertEqual(lines, expected_lines)

    def test_empty_data(self):
        empty_data = []
        with self.assertRaises(FileGeneratorError):
            generate_fixed_width_file(self.spec, empty_data, self.output_file)

    def test_large_data(self):
        large_data = [["1", "a"*12, "1", "a"*2, "a"*13, "a"*7, "a"*10, "a"*13, "a"*20, "a"*13] for _ in range(1000)]

        generate_fixed_width_file(self.spec, large_data, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r', encoding=self.spec['FixedWidthEncoding']) as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 1001)
        self.assertEqual(lines[1], "1    aaaaaaaaaaaa1  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")

    def test_invalid_output_path(self):
        invalid_path = '/invalid/path/test_output.txt'
        with self.assertRaises(FileGeneratorError):
            generate_fixed_width_file(self.spec, self.data, invalid_path)

if __name__ == '__main__':
    unittest.main()
