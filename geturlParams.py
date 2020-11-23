#获取接口的url、参数，method等

import readConfig as readConfig

readConfig = readConfig.ReadConfig()
class geturlParams():
    def get_url(self):
        new_url = readConfig.get_http('scheme')+'://'+readConfig.get_http('baseurl')+':8888'+'/login'+'?'
        #logger.info('new_url'+new_url')
        return new_url

if __name__=='__main__':      #验证拼接后的正确性
    print(geturlParams().get_url())