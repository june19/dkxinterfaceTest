#读取exxcel的方法

import os
import getpathInfo #自己定义的内部类，该类返回项目的绝对路径
#调用读Excel的第三方库xlrd
from xlrd import open_workbook

path = getpathInfo.get_Path()

class readExcel():
    def get_xls(self,xls_name,sheet_name):
        cls = []
        #获取用例文件路径
        xlspath = os.path.join(path,"testFile",'case',xls_name)
        # 打开用例Excel
        file = open_workbook(xlspath)
        # 获得打开Excel的sheet
        sheet = file.sheet_by_name(sheet_name)
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):
            #根据行数做循环
            if sheet.row_values(i)[0] !=u'case_name':
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':   #我们执行该文件测试一下是否可以正确获取excel中的值
    print(readExcel().get_xls('userCase1.xlsx','login'))
    print(readExcel().get_xls('userCase1.xlsx','login')[0][1])
    print(readExcel().get_xls('userCase1.xlsx','login')[1][2])
