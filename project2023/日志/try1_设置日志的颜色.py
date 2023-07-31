import logging
import colorlog

# 创建logger对象
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建一个StreamHandler用于输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建一个ColorFormatter来添加颜色
color_formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)

# 将ColorFormatter添加到StreamHandler
console_handler.setFormatter(color_formatter)

# 将StreamHandler添加到logger
logger.addHandler(console_handler)

# 使用不同级别的日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
