from main import file_exists
import unittest
import csv


class TestFileExists(unittest.TestCase):
    def setUp(self):
        with open("tests/test_data/test_csv.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            self.rows = [row for row in reader]

    # Valid Path, is readable, and not zero bytes
    def test_valid_path(self):
        self.assertTrue(file_exists(self.rows[0], 0, []))

    # File does not exist
    def test_invalid_path(self):
        self.assertFalse(file_exists(self.rows[2], 0, []))

    # File path exist but is zero bytes
    def test_zero_bytes(self):
        self.assertFalse(file_exists(self.rows[3], 0, []))


if __name__ == "__main__":
    unittest.main()
