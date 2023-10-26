import unittest
import main


class TestMain(unittest.TestCase):
    def test_addOne(self):
        self.assertEqual(main.addOne(1), 2)
        self.assertEqual(main.addOne(-1), 0)


if __name__ == '__main__':
    unittest.main()
