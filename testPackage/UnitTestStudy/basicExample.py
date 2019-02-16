import unittest

class TestStringMethods(unittest.TestCase):
    # 在每个测试方法前执行
    # 测试运行过程中，假如setUp()抛出异常，则测试框架认为测试失败，且后面的具体测试方法不会被执行
    # If the setUp() method raises an exception while the test is running,
    # the framework will consider the test to have suffered an error,
    # and the test method will not be executed.
    def setUp(self):
         print("-----setup method>>>")

    # 在每个测试方法后执行
    # 假如setUp()执行正常，则tearDown()会被执行；测试方法的结果跟tearDown()执行成功或失败无关
    # If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.
    def tearDown(self):
        print("<<<teardown method")

    def test_upper(self):
        print("test_upper(self)")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper(self)")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    # 假如修改test_split为tes_split，则该方法不会被执行
    def test_split(self):
        print("test_split(self)")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_qs1(self):
        print("test_qs1(self)")
        self.assertEqual(1,1,"msg: 1!=2")

if __name__ == '__main__':
    unittest.main()