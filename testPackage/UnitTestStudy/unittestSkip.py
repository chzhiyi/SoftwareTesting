import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("\n前置方法")

    def tearDown(self):
        print("清理方法")

    @unittest.skip("演示直接跳过")
    def testSkip(self):
        print("看到它，你就完了")
        self.fail("不会被执行")

    @unittest.skipIf(False, "skipIf条件成立时，就跳过")
    def testSkipIf(self):
        print("它出现了，是因为你的unittest.skipIf条件是False；把条件改为True看下")

    @unittest.skipUnless("除非你到天堂了，否则你是一定会喘气的".startswith('除非'), "skipUnless条件为True，就执行")
    def testSkipUnless(self):
        print("它出现了吗？出现了，表示你命中了unless的苛刻条件")

    yourAge = 59
    @unittest.skipUnless(yourAge<60, "你60多岁了，下面的代码不会执行的")
    def testSkipUnlessAgeLessThen60(self):
        print("原来你这么年轻，还没到60岁")

    @unittest.expectedFailure
    def testSkipExpectedFailure(self):
        # 我断言失败了，但不会计入失败的用例个数里的。不信就执行下看看
        # 前置、清理方法会正常执行
        self.assertTrue(False)

    def testOK(self):
        self.assertEqual(3>1, True)


@unittest.skip("唇亡则齿寒。整个类都被跳过了，你以为里面的测试方法还会被执行吗？当然不会！")
class MySkippedTestCase(unittest.TestCase):
    def testNotRunned(self):
        print("我不会被运行的，因为你把整个测试类都跳过了")

# 结个尾巴：
# Skipped tests will not have setUp() or tearDown() run around them.
# Skipped classes will not have setUpClass() or tearDownClass() run.
# Skipped modules will not have setUpModule() or tearDownModule() run.