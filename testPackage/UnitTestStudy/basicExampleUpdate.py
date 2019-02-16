import unittest
from basicExample import TestStringMethods

def suiteTest():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods("test_isupper"))
    suite.addTest(TestStringMethods("test_qs1"))
    suite.addTest(TestStringMethods("test_split"))
    suite.addTest(TestStringMethods("test_upper"))
    return suite


if __name__ == '__main__':
    # 设置日志信息级别
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = unittest.TextTestRunner()
    runner.run(suiteTest())
