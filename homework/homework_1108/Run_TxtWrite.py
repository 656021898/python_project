# -*_ coding:utf-8 _*-
from homework.homework_1108.TestHttpRequest import TestHttpRequest
from homework.homework_1108.DoExcel import DoExcel
import datetime


# 执行用例并写入txt_report.txt
excel_list = DoExcel().read_excel("test_data/testCaseRead.xlsx", "testCaseRead")
with open("test_result/txt_report.txt", "a+", encoding="utf-8") as fb:
    fb.write("当前时间为：" + str(datetime.datetime.today()) + "\n")
    for item in excel_list:
        try:
            res = TestHttpRequest(url=(item["host"] + item["url"]), data=eval(item["data"]), method=item["method"],
                                  code=item["code"]).HttpRequest()
            assert str(item["code"]) == res.json()["code"]
            # 执行结果写入TXT文件
            fb.write("用例编号：{id}，结果：测试通过\n".format(id=item["id"]))
        except (AssertionError, Exception) as e:
            print("测试未通过的用例id为：{id}，描述为：{description}".format(id=item["id"], description=item["description"]))
            print("预期结果是：{anticipate}，实际结果是：{real},接口返回的错误是：{msg}".format(anticipate=item["code"],
                                                                          real=res.json()["code"],
                                                                          msg=res.json()["msg"]))
            # 执行结果写入TXT文件
            fb.write("用例编号：{id}，结果：测试未通过，描述为：{description},预期结果是：{anticipate}，实际结果是：{real},接口返回的错误是：{msg}\n".format(
                id=item["id"], description=item["description"], anticipate=item["code"],
                real=res.json()["code"], msg=res.json()["msg"]))




