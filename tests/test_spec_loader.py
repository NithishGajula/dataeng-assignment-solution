import unittest
from src.spec_loader import load_spec, SpecLoaderError

class TestSpecLoader(unittest.TestCase):
    def test_load_spec(self):
        spec = load_spec('spec.json')
        self.assertIn('ColumnNames', spec)
        self.assertIn('Offsets', spec)

    def test_load_spec_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_spec('non_existent_file.json')

    def test_load_invalid_spec(self):
        with self.assertRaises(SpecLoaderError):
            load_spec('tests/resources/invalid_spec.json')

    def test_load_missing_required_spec(self):
        with self.assertRaises(SpecLoaderError):
            load_spec('tests/resources/missing_required_spec.json')

if __name__ == '__main__':
    unittest.main()
