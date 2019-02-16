import unittest
import sys,random


# 模块级setUp和tearDown跟class类同一级别
def setUpModule():
    print("module comes setup")

def tearDownModule():
    print("module comes tearDown")


class TestCaseClass(unittest.TestCase):
    def setUp(self):
        print("before testCase Function")

    def tearDown(self):
        print("after testCase Function")

    @classmethod
    def setUpClass(cls):
        print("......before class, executed once\n")

    @classmethod
    def tearDownClass(cls):
        print("......after class, executed once")

    def testAssertEqual(self):
        self.assertEqual(100, 100)
        # print(str(self.__class__) + " " + sys._getframe().f_code.co_name)

    def testAssertNotEqual(self):
        self.assertNotEqual(100, 200)

    def testAssertTrue(self):
        self.assertTrue(False, "assertTrue()断言失败")

    def testAssertFalse(self):
        self.assertFalse(False, "你不会看见我的")

    def testAssertIs(self):
        a = 1
        b = a
        self.assertIs(a, b, "testAssertIs(self)")

    def testAssertIsNot(self):
        self.assertIsNot(1, 2)


    def testAssertIsNone(self):
        temp = None
        self.assertIsNone(temp)

    def testAssertIsNotNone(self):
        temp = 1233
        self.assertIsNotNone(temp)

    def testAssertIn(self):
        a = 1
        b = [1,23,4,5,6]
        self.assertIn(a, b)

    def testAssertIsInstance(self):
        """
        isinstance()与type()区别：
            type()不会认为子类是一种父类类型，不考虑继承关系。
            isinstance()会认为子类是一种父类类型，考虑继承关系。
        如果要判断两个类型是否相同推荐使用isinstance()。
        """
        self.assertIsInstance(1, int)
        self.assertIsInstance(1, str)

    def testAssertNotIsInstance(self):
        temp = (1,3)
        self.assertNotIsInstance(temp, str)



class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


if __name__ == '__main__':
    unittest.main()
