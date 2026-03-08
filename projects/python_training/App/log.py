←
←
# 获取一个日志记录器对象，赋值给变量logger供后续使用
# 将这个logger对象的级别手动设置为DEBUG，确保它能记录调试信息
logging
basicConfig
DEBUG
getLogger
level

# 配置整个日志系统的基础设置，包括根记录器的级别为DEBUG
logging.basicConfig(level = DEBUG)
logger = logging.getLogger()
logger.level = logging.DEBUG
