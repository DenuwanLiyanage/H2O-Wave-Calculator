import unittest
import Cal


class TestCalc(unittest.TestCase):

    def test_perform_calculator_simple(self):
        self.assertEqual(Cal.perform_calculator("10+5"), 15)
        self.assertEqual(Cal.perform_calculator("10-5"), 5)
        self.assertEqual(Cal.perform_calculator("10*5"), 50)
        self.assertEqual(Cal.perform_calculator("10/5"), 2)


if __name__ == '__main__':
    unittest.main()
