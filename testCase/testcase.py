import unittest
#读取userCase.xlsx中的用例，使用unittest来进行断言校验

import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel

url = geturlParams.geturlParams().get_url() #调用我们的geturlParams获取我们拼接的URL
login_xls =readExcel.readExcel().get_xls('userCase.xlsx','login')


@paramunittest.parametrized(*login_xls)

class TestUserLogin(unittest.TestCase):
    def setParameters(self,case_name,path,query,method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query =str(query)
        self.method =str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        url1 ="http://127.0.0.1:8888/login?"
        new_url =url1+self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))  #将一个完整的url中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        info = RunMain().run_main(self.method,url,data1) #根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info) #将响应转换为字典格式
        if self.case_name =='login':
            self.assertEqual(ss['code'],200)
        if self.case_name =='login_error':
            self.assertEqual(ss['code'],-1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'],10001)


if __name__ == '__main__':
    unittest.main()
