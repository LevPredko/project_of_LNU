import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(1, 3), 4)
        self.assertEqual(main.add(-5, -7), -12)
        self.assertEqual(main.add(-6, 14), 8)

    def test_smallest_factor(self):
        self.assertEqual(main.smallest_factor(1), 1)
        self.assertEqual(main.smallest_factor(2), 2)
        self.assertEqual(main.smallest_factor(10), 2)
        self.assertEqual(main.smallest_factor(13), 13)

    def test_month_length(self):
        self.assertEqual(main.month_length("January"), 31)
        self.assertEqual(main.month_length("February"), 28)
        self.assertEqual(main.month_length("February", leap_year=True), 29)
        self.assertEqual(main.month_length("April"), 30)
        self.assertEqual(main.month_length("June"), 30)
        self.assertEqual(main.month_length("September"), 30)
        self.assertEqual(main.month_length("November"), 30)
        self.assertIsNone(main.month_length("InvalidMonth"))

    def test_operate(self):
        self.assertEqual(main.operate(1, 2, "+"), 3)
        self.assertEqual(main.operate(5, 6, "+"), 11)
        self.assertEqual(main.operate(-7, 17, "+"), 10)
        self.assertEqual(main.operate(0, 5, "+"), 5)

        with self.assertRaises(ZeroDivisionError):
            main.operate(5, 0, "/")

        with self.assertRaises(TypeError):
            main.operate(5, 2, 3)

        with self.assertRaises(ValueError):
            main.operate(5, 2, "^")


if __name__ == '__main__':
    unittest.main()
