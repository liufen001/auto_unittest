# coding=utf-8

import unittest
from Libs.log_utils import TSlog
#from HTMLtestreport import HTMLTestRunner
from HTMLTestRunner_Charts import HTMLTestRunner
from time import strftime
from Libs.email_utils import send_test_report


def main():
    TSlog.__int__('./Result/log/')
    TSlog.Error(u'========> 测试执行开始 <=======')

    #执行用例的路径
    suite = unittest.defaultTestLoader.discover('./Scripts', '*_testcase.py', top_level_dir=None)
    #获取生成报告的系统时间
    ts = strftime('%Y%m%d_%H%M%S')
    #报告存放路径
    report_file = './Result/report/%shtmlreport.html'%ts
    ref = open(report_file,'w',encoding='utf-8')
    #执行用例并生成报告
    runner = HTMLTestRunner(stream=ref,verbosity=2,title=u'测试报告',description=u'测试类测试报告')
    runner.run(suite)
    ref.close()
    #执行完用例把报告发送给指定人员邮箱
    send_test_report(report_file, u'%s测试报告'%ts, u'%s生成的测试报告，请查收'%ts, ['1148270541@qq.com','122815306@qq.com'])
    TSlog.Error(u'========> 测试执行结束 <=======')

if __name__ == '__main__':
    main()
