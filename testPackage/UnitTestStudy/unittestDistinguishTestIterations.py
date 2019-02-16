import unittest

class NumbersTest(unittest.TestCase):
    def test_even(self):
        """
        判断[0, 5]是否不是偶数
        """
        for i in range(0, 6):
            strI = str(i)
            print("i = " + strI + ", " + strI +"%2 = " + str(i%2) )
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0, strI+"不是偶数")