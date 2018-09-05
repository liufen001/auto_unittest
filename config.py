#用来配置测试用例文件是否执行，直接用字典方式配置

#cf_testcase = {'cf_login_testcase': True}

'''
用来配置测试用例文件是否执行
#用excel的方式配置
'''

import xlrd

def conf_tests(e_name,s_name):
    xr = xlrd.open_workbook(e_name).sheet_by_name(s_name)
    cr = xr.nrows
    cc = xr.ncols
    c_d={}
    for i in range(1,cr):
        c_cells=[]
        for j in range(1,cc):
            val = xr.cell_value(i,j)
            c_cells.append(val)

        #每循环一次生成一个字典的键和对应的值
        c_d[c_cells[0]]=c_cells
    return c_d


if __name__ == '__main__':
    print (conf_tests())

