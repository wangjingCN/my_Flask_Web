import logging
import time
import os
from .api.commonUtil import make_dir

project_name = "Flask_web_log"
folder_format = time.strftime('%Y-%m', time.localtime(time.time()))
log_file_name = project_name + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + project_name + os.sep + folder_format
make_dir(log_file_folder)
log_file_str = log_file_folder + os.sep + log_file_name

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger_format = logging.Formatter(fmt='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logger_fh = logging.FileHandler(log_file_str)
logger_fh.setFormatter(logger_format)
logger.addHandler(logger_fh)

# logger = logging.getLogger('logging.log')

# logger_stream= logging.StreamHandler()
# logger_stream.setLevel(logging.DEBUG)
# logger_stream.setFormatter(logger_format)
# logger.addHandler(logger_stream)


# logging.basicConfig(filename='logging.log', filemode='a', level=logging.DEBUG,format='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')