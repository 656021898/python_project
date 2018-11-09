# -*_ coding:utf-8 _*-
from homework.homework_1108.TestHttpRequest import TestHttpRequest
from homework.homework_1108.DoExcel import DoExcel


#执行结果写入excel
shili1 =DoExcel()
excel_list = shili1.read_excel("test_data/testCaseRead.xlsx", "testCaseRead")
Write_list = []
for item in excel_list:
    Excel_dict = {}
    try:
        res = TestHttpRequest(url=(item["host"] + item["url"]), data=eval(item["data"]), method=item["method"],
                              code=item["code"]).HttpRequest()
        assert str(item["code"]) == res.json()["code"]
        Excel_dict["TestResult"] = "通过"
        Excel_dict["res_json"] = res.json()
        Excel_dict["real_code"] = ""
    except (AssertionError, Exception) as e:
        Excel_dict["TestResult"] = "未通过"
        Excel_dict["res_json"] = res.json()
        Excel_dict["real_code"] = res.json()["code"]
    Excel_dict["id"] = item["id"]
    Excel_dict["module"] = item["module"]
    Excel_dict["description"] = item["description"]
    Write_list.append(Excel_dict)
print(Write_list)
shili2 =DoExcel()
shili2.write_excel("test_result/ExcelResult.xlsx","testCaseWrite",Write_list)