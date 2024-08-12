import unittest
from unittest.mock import mock_open, patch
from src.file_generator import generate_fixed_width_file

class TestFileGenerator(unittest.TestCase):
    def setUp(self):
        self.spec = {
            "ColumnNames": ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
            "Offsets": [5, 12, 3, 2, 13, 7, 10, 13, 20, 13],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }
        self.data = [
            ["12345", "abcdefghijk", "123", "12", "abcdefghijklm", "1234567", "abcdefghij", "abcdefghijklm", "abcdefghijklmnopqrst", "abcdefghijklm"]
        ]

    @patch("builtins.open", new_callable=mock_open)
    def test_generate_fixed_width_file(self, mock_file):
        generate_fixed_width_file(self.spec, self.data, "test_fixed_width.txt")
        mock_file.assert_called_once_with("test_fixed_width.txt", 'w', encoding="windows-1252")
        mock_file().write.assert_called()

if __name__ == '__main__':
    unittest.main()
