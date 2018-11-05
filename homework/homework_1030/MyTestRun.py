import unittest
from homework.homework_1030.MyTest import MyTest
from homework.homework_1030 import MyTest
import HTMLTestRunnerNew

suite = unittest.TestSuite()#存储用例
#方法1：
# suite.addTest(MyTest("test_login_normal"))
#方法2：
loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(MyTest))
suite.addTest(loader.loadTestsFromModule(MyTest))

#执行
# with open("TestResult.txt","w+") as file:
#     runner = unittest.TextTestRunner(stream=file,verbosity=2)
#     runner.run(suite)

with open("test_report.html","wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title="MyHttpRequest的单元测试报告",description="哈哈哈哈哈",tester="江江")
    runner.run(suite)