import xlwt
import xlrd

"""
 if sheet1.row_values(i)[0] != u'case_name':
 cls.append(sheet1.row_values(i))
 return cls
"""


#第一步：新建工作簿，添加行和列数据

def create_Excel():
    workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
    sheet1 = workbook.add_sheet("login")
    sheet1.write(0, 0, "case_name")
    sheet1.write(0, 1, "path")
    sheet1.write(0, 2, "query")
    sheet1.write(0, 3, "method")
    sheet1.write(1, 0, "login")
    sheet1.write(1, 1, "/login")
    sheet1.write(1, 2, "name=xiaoming&pwd=111")
    sheet1.write(1, 3, "post")
    sheet1.write(2, 0, "login_error")
    sheet1.write(2, 1, "/login")
    sheet1.write(2, 2, "name=xiaoming&pwd=111222")
    sheet1.write(2, 3, "post")
    sheet1.write(3, 0, "login_null")
    sheet1.write(3, 1, "/login")
    sheet1.write(3, 2, "name=xiaoming&pwd=")
    sheet1.write(3, 3, "post")


    workbook.save(r'E:\myshare\tlj\dkxinterfaceTest\testFile\case\usercase1.xlsx')





#第二步：读取数据

def read_Excel():
    #cls = []
    workbook = xlrd.open_workbook(r'E:\myshare\tlj\dkxinterfaceTest\testFile\case\userCase1.xlsx')
    print(workbook.sheet_names())  #查看所有sheet名称
    sheet1 = workbook.sheet_by_index(0) #用索引取第1个sheet

    cell_00 = sheet1.cell_value(0,0)  #读取第1行第1列数据
    row0 = sheet1.row_values(0)  #读取第1行数据
    print(row0)
    nrows = sheet1.nrows         #读取行数
    for i in range(nrows):        #循环逐行打印
        if i ==0:
            continue
        print(sheet1.row_values(i)[:4]) #取前1列






if __name__ == '__main__':
    read_Excel()
     #print(read_Excel()[1][0])