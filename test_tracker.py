import unittest
from reports import show_balance
from validation import valid_amount, valid_choice


class TestStudentMoneyTracker(unittest.TestCase):

    def test_positive_amount(self):
        self.assertTrue(valid_amount(100))

    def test_negative_amount(self):
        self.assertFalse(valid_amount(-50))

    def test_menu_choice(self):
        self.assertTrue(valid_choice("5", 1, 12))

    def test_invalid_menu_choice(self):
        self.assertFalse(valid_choice("20", 1, 12))


if __name__ == "__main__":
    unittest.main()
