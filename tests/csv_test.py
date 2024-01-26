from main import is_non_empty_string
from main import datetime_valid
import unittest


def test_nonempty_string():
    empty_string = "   "
    normal_string = " hello   "
    newline_string = "\n   "
    assert is_non_empty_string(empty_string) == False
    assert is_non_empty_string(normal_string) == True
    assert is_non_empty_string(newline_string) == False


class TestDatetimeValid(unittest.TestCase):
    def test_single_valid_date(self):
        self.assertTrue(datetime_valid("2024-01-18"))

    def test_single_invalid_date(self):
        self.assertFalse(datetime_valid("2024-13-18"))  # Invalid month

    def test_valid_date_range(self):
        self.assertTrue(datetime_valid("2021-01-01/2021-12-31"))

    def test_invalid_date_range(self):
        self.assertFalse(datetime_valid("2021-01-01/2021-13-31"))  # Invalid second date

    def test_valid_duration(self):
        self.assertTrue(datetime_valid("P3Y6M4DT12H30M5S"))  # Valid duration

    def test_invalid_format(self):
        self.assertFalse(datetime_valid("2024/01/18"))  # Non-ISO format

    def test_empty_string(self):
        self.assertFalse(datetime_valid(""))  # Empty string


# Run the tests
if __name__ == "__main__":
    unittest.main()
