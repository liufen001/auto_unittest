#icoding = utf-8
'''
读取Excel中的文件，通过Excel配置用例是否执行
u'../用例配置.xlsx'
u'用例'
'''


import xlrd

def testcase_conf(s_test,s_name):
    xr = xlrd.open_workbook(s_test).sheet_by_name(s_name)
    nr = xr.nrows
    nw = xr.ncols
    e_d={}
    for i in range(1,nr):
        e_cells = []
        for j in range(1,nw):
            val = xr.cell_value(i,j)
            e_cells.append(val)

        e_d[e_cells[0]]=e_cells

    return e_d



if __name__ == '__main__':
    print (testcase_conf(u'../用例配置.xlsx',u'用例'))
