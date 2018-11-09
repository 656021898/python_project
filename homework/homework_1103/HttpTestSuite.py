import unittest
from homework.homework_1103.TestCase import TestCaseSetup
import HTMLTestRunnerNew
from homework.homework_1103.GetExcel import GetExcel


test_data = GetExcel("testData.xlsx","data").get_all_row()
suite = unittest.TestSuite()
for item in test_data:
    suite.addTest(TestCaseSetup("test_case",item["url"],eval(item["data"]),item["method"],str(item["code"])))
    #excel读出的数据，数字为数字，其他均为字符串

with open('my_report.html', 'wb') as myfile:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=myfile,title='My unit test',description='hahah')
    runner.run(suite)

globals()

