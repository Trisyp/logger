from utils.root_dir import root_dir

import logging
from utils.singleton import SingletonType
from utils.params import log_level
from pathlib import Path
import os


# 这个是日志保存本地的路径
log_path = Path(f"{root_dir}/logs/")


class Log(metaclass=SingletonType):
    def __init__(self):
        # 文件的命名
        self.info_log_name = os.path.join(log_path, 'log') + '.log'
        self.error_log_name = os.path.join(log_path, 'error') + '.log'
        self.logger = logging.getLogger()

        # 设置日志级别
        if log_level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif log_level == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)
        elif log_level == "WARNING":
            self.logger.setLevel(logging.WARNING)
        else:
            self.logger.setLevel(logging.INFO)

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - thread_id:%(thread)d - process_id:%(process)d - %(levelname)s: %(message)s')

    def __console(self, level, log_name, message, Handler_flag=True):
        # 创建一个FileHandler，用于写到本地
        os.makedirs(log_path, exist_ok=True)
        fh = logging.FileHandler(log_name, 'a')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        # 根据日志等级来打印日志内容
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            if not Handler_flag:
                self.logger.removeHandler(ch)
                ch.close()
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def debug(self, message):
        self.__console('debug', self.info_log_name, message, True)

    def info(self, message):
        self.__console('info', self.info_log_name, message, True)

    def warning(self, message):
        self.__console('warning', self.info_log_name, message, True)

    def error(self, message):
        self.__console('error', self.info_log_name, message, True)
        self.__console('error', self.error_log_name, message, False)
