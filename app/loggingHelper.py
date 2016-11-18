# --coding: utf-8--
import logging
import datetime
import sys
import os

project_name = "Flask_web_log"


def getLogger(folder_name):
    logger = logging.getLogger('mylog')
    folder = '/var/log/netShell/' + folder_name.strip()
    if not os.path.exists(folder):
        os.makedirs(folder)
    log_file = folder + os.sep + "%s.log" % (datetime.datetime.now().strftime("%Y-%m-%d"))
    print log_file

    logger.setLevel(logging.DEBUG)
    logger_format = logging.Formatter(fmt='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    logger_fh = logging.FileHandler(log_file)  # 记录log
    logger_fh.setFormatter(logger_format)
    logger.addHandler(logger_fh)

    s_h = logging.StreamHandler(sys.stderr)  # 输出到控制台
    logger.addHandler(s_h)
    return logger
