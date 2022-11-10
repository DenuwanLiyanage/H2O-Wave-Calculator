import unittest
import Cal


class TestCalc(unittest.TestCase):

    def test_perform_calculator_simple(self):
        self.assertEqual(Cal.perform_calculator("10+5"), 15)
        self.assertEqual(Cal.perform_calculator("10-5"), 5)
        self.assertEqual(Cal.perform_calculator("10*5"), 50)
        self.assertEqual(Cal.perform_calculator("10/5"), 2)

    def test_perform_calculator_complex(self):
        self.assertEqual(Cal.perform_calculator("10+5*2+4/2"), 22)
        self.assertEqual(Cal.perform_calculator("10+16/4*2-3"), 15)

    def test_perform_calculator_divide_zero(self):
        self.assertEqual(Cal.perform_calculator("10/0"), "Divide Zero")
        self.assertEqual(Cal.perform_calculator("10+8-3*7/0+5"), "Divide Zero")


if __name__ == '__main__':
    unittest.main()
