from homework.homework_1108.TestHttpRequest import TestHttpRequest
from homework.homework_1108.DoExcel import DoExcel


class running:
    def __init__(self, excelname, sheetname):
        self.excelname = excelname
        self.sheetname = sheetname

    def running(self):
        excel_list = DoExcel(self.excelname, self.sheetname).read_excel()
        for item in excel_list:
            try:
                res = TestHttpRequest(url=(item["host"] + item["url"]), data=eval(item["data"]), method=item["method"],
                                      code=item["code"]).HttpRequest()
                assert str(item["code"]) == res.json()["code"]
            except (AssertionError, Exception) as e:
                print(type(item["code"]), type(res.json()["code"]))
                print("测试未通过的用例id为：{id}，描述为：{description}".format(id=item["id"], description=item["description"]))
                print("预期结果是：{anticipate}，实际结果是：{real},接口返回的错误是：{msg}".format(anticipate=item["code"],
                                                                              real=res.json()["code"],

                                                                              msg=res.json()["msg"]))


if __name__ == "__main__":
    running("test_data/testCaseRead.xlsx", "testCaseRead").running()
