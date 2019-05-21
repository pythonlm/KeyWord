#encoding=utf-8
import logging
import logging.config
from ProjectVar.Var import *


#读取日志的配置文件
logging.config.fileConfig(project_path+"\\Conf\\Logger.conf")
#选择一个日志格式
logger = logging.getLogger("example02")

def error(message):
    #打印debug级别信息
     logger.error(message)
def info(message):
    #打印info级别信息
     logger.info(message)
def warning(message):
    #打印warning级别信息
     logger.warning(message)

