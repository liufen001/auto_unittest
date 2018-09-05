import logging
import time

class TSlog(object):

    def __int__(logfile):

        #创建一个alog
        alog=logging.getLogger()
        alog.setLevel(logging.DEBUG)

        #设置日志文件名
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_name = logfile + rq + '.log'

        #创建一个handler用于写入日志文件
        tlog=logging.FileHandler(log_name,encoding='utf-8')
        tlog.setLevel(logging.INFO)

        #创建一个handler用于写入控制台
        clog=logging.StreamHandler()
        clog.setLevel(logging.WARN)

        #设置日志的输出样式
        tf=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-10s: %(message)s')
        cf=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        tlog.setFormatter(tf)
        clog.setFormatter(cf)

        #给alog添加handler
        alog.addHandler(tlog)
        alog.addHandler(clog)
        return

    def Error(msg):
        logging.error(msg)

    def Info(msg):
        logging.info(msg)

    def Warn(msg):
        logging.warning(msg)

if __name__ == '__main__':

    TSlog.__int__('../Result/log/')
    TSlog.Error('error msg')
    TSlog.Info('info msg')
    TSlog.Warn('warn msg')

