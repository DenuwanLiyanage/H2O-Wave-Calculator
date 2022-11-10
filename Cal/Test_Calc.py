import unittest
import Cal


class TestCalc(unittest.TestCase):

    def test_perform_calculator(self):
        self.assertEqual(Cal.perform_calculator("10+5"), 15)


if __name__ == '__main__':
    unittest.main()
