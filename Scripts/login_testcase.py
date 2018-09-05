#coding=utf-8
import unittest
from PO.HomePage import baidusearch
from Libs.log_utils import TSlog
from Libs.excel_utils import testcase_conf
from config import conf_tests

#配置用例类是否执行
conf_tests_name = u'用例类配置.xlsx'
conf_sheet_name = u'用例类'
conf_tests = conf_tests(conf_tests_name,conf_sheet_name)

#配置用例是否执行
test_conf = testcase_conf(u'单个用例配置.xlsx', u'用例')

#@unittest.skipUnless(cf_testcase['cf_login_testcase'],'跳过此用例类')
@unittest.skipUnless(conf_tests['MyTestCase'][-1],'%s:跳过此用例类'%conf_tests_name)
class MyTestCase(unittest.TestCase):
    url = 'https://weibo.com/'
    username = '1148270541@qq.com'
    password = 'heihei123*#'
    wusername = '1234'
    wpassword = '1234'

   # (u'../用例配置.xlsx', u'用例')
    #@unittest.skipUnless(cf_test1,'跳过此测试用例')
    @unittest.skipUnless(test_conf["test1"][-1],'跳过此测试用例')
    def test1(self):
        TSlog.Warn('test1执行开始')
        baidusearch.__int__(self,self.url)
        baidusearch.login(self,self.username,self.password)
        ret = baidusearch.page_should_contain(self,'我的赞')
        self.assertTrue(ret,'输入正确的用户名和密码登录，验证失败')
        print(ret)
        baidusearch.bclose(self)
        TSlog.Warn('test1执行结束')

    #@unittest.skipUnless(cf_test2,'跳过此测试用例')
    @unittest.skipUnless(test_conf["test2"][-1], '跳过此测试用例')
    def test2(self):
        TSlog.Warn('test2执行开始')
        baidusearch.__int__(self,self.url)
        baidusearch.login(self,self.wpassword,self.password)
        ret = baidusearch.page_should_contain(self, '用户名或密码错误')
        self.assertTrue(ret,'输入错误的用户名登录，验证失败')
        print(ret)
        baidusearch.bclose(self)
        TSlog.Warn('test2执行结束')


if __name__ == '__main__':
    unittest.main()
