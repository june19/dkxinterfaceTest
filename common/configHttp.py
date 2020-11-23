#主要文件主要来通过get，post，put，delete 等方法进行http请求，并拿到请求响应

import requests
import json

class RunMain():
    def send_post(self,url,data):  #定义一个方法，传入需要的参数url和data
        #参数必须按照url，data顺序传入
        result = requests.post(url=url,data=data).json() #因为这里要封装post方法，所以这里的url和data值不能写死
        res =json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res

    def send_get(self,url,data):
        result = requests.get(url=url,params=data).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res

    def run_main(self,method,url=None,data=None):
        result =None
        if method =='post':
            result = self.send_post(url,data)
        elif method == 'get':
            result =self.send_post(url,data)
        else:
            print("method值错误！！！")
        return result

if __name__=='__main__':
    result1 = RunMain().run_main('post','http://127.0.0.1:8888/login',{'name':'xiaoming','pwd':'111'})
    result2 = RunMain().run_main('get','http://127.0.0.1:8888/login','name=xiaoming&pwd=111')
    print(result1)
    print(result2)
