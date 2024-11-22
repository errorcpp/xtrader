#  coding: utf-8

import inspect
import logging
import sys

EXPORT_LOG_FUNC_TO_BUILTIN = True
DEFAULT_LOGGER_NAME = "default"
# pylint: disable=C0103
logger = None # default logger

def set_default_logger_name(name:str):
    global DEFAULT_LOGGER_NAME, logger
    DEFAULT_LOGGER_NAME = name
    logger = None
    _init_default_logger()

#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(function_name)s - %(message)s')  # level=logging.INFO 可以控制不同level的格式

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.DEBUG:
            record.levelname = 'D'
        if record.levelno == logging.INFO:
            record.levelname = 'I'
        if record.levelno == logging.WARN:
            record.levelname = 'W'
        if record.levelno == logging.ERROR:
            record.levelname = 'E'
        return super().format(record)

# 创建颜色日志格式化程序
LOG_LEVEL_COLOR_MAP = {
    logging.DEBUG: '\033[0;36m',   # cyan
    logging.INFO: '\033[0;32m',    # green
    logging.WARNING: '\033[0;33m', # yellow
    logging.ERROR: '\033[0;31m',   # red
    logging.CRITICAL: '\033[0;37;41m',   # white on red
}

class CustomStreamHandler(logging.StreamHandler):
    def emit(self, record) -> None:
        try:
            log_color = LOG_LEVEL_COLOR_MAP.get(record.levelno, '\033[0m')  # default to reset color
            # 设置输出颜色
            self.stream.write(log_color)
            # 调用父类的emit方法输出日志
            super().emit(record)
            # 重置输出颜色
            self.stream.write('\033[0m')
            self.flush()
        except Exception:
            self.handleError(record)

def _init_default_logger():
    global logger
    logger = logging.getLogger(DEFAULT_LOGGER_NAME)
    logger.propagate = False # 不传播到父记录器
    logger.setLevel(logging.DEBUG)
    #formatter = logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s [custom_function_name%(function_name)s][funcname=%(funcName)s][%(filename)s:%(lineno)d]')
    #formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(message)s]\t[%(filename)s:%(lineno)d,func=%(funcName)s]')
    formatter = CustomFormatter('[%(asctime)s][%(name)s][%(levelname)s][tid=%(thread)s][%(filename)s:%(funcName)s:%(lineno)d] [%(message)s]')
    sh = CustomStreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

# pylint: enable=C0103
if logger is None:
    _init_default_logger()

##################################################################################################################################

def LOG_DEBUG(fmt, *args, **kwargs):
    '''
    '''
    # 自定义方案
    # formatter = logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s [func=%(function_name)s]')
    # extra = {
    #     "function_name" : inspect.stack()[1].function,
    # }
    # logger.debug("custom function_name by extra", *args, extra=extra, **kwargs)
    # 手工指定logging stack方式，不需要额外传递extra
    logger.debug(fmt, *args, stacklevel=2, **kwargs)

def LOG_INFO(fmt, *args, **kwargs):
    '''
    '''
    logger.info(fmt, *args, stacklevel=2, **kwargs)

def LOG_WARN(fmt, *args, **kwargs):
    '''
    '''
    logger.warning(fmt, *args, stacklevel=2, **kwargs)

def LOG_ERROR(fmt, *args, **kwargs):
    '''
    '''
    logger.error(fmt, *args, stacklevel=2, **kwargs)

######## 开放stacklevel

def LOG_DEBUG_WITH_STACKLEVEL(fmt, *args, stacklevel=3, **kwargs):
    '''
    '''
    logger.debug(fmt, *args, stacklevel=stacklevel, **kwargs)

def LOG_INFO_WITH_STACKLEVEL(fmt, *args, stacklevel=3, **kwargs):
    '''
    '''
    logger.info(fmt, *args, stacklevel=stacklevel, **kwargs)

def LOG_WARN_WITH_STACKLEVEL(fmt, *args, stacklevel=3, **kwargs):
    '''
    '''
    logger.warning(fmt, *args, stacklevel=stacklevel, **kwargs)

def LOG_ERROR_WITH_STACKLEVEL(fmt, *args, stacklevel=3, **kwargs):
    '''
    '''
    logger.error(fmt, *args, stacklevel=stacklevel, **kwargs)

########################################################################################################################

def LOG_DEBUG_EX(logger_name, fmt, *args, **kwargs):
    logging.getLogger(logger_name).debug(fmt, *args, stacklevel=2, **kwargs)

def LOG_INFO_EX(logger_name, fmt, *args, **kwargs):
    logging.getLogger(logger_name).info(fmt, *args, stacklevel=2, **kwargs)

def LOG_WARN_EX(logger_name, fmt, *args, **kwargs):
    logging.getLogger(logger_name).warning(fmt, *args, stacklevel=2, **kwargs)

def LOG_ERROR_EX(logger_name, fmt, *args, **kwargs):
    logging.getLogger(logger_name).error(fmt, *args, stacklevel=2, **kwargs)

def LOG_DEBUG_EX_WITH_STACKLEVEL(logger_name, fmt, *args, stacklevel=3, **kwargs):
    '''
    '''
    logging.getLogger(logger_name).debug(fmt, *args, stacklevel=stacklevel, **kwargs)

def LOG_INFO_EX_WITH_STACKLEVEL(logger_name, fmt, *args, stacklevel=3, **kwargs):
    '''
    '''
    logging.getLogger(logger_name).info(logger_name, fmt, *args, stacklevel=stacklevel, **kwargs)

def LOG_WARN_EX_WITH_STACKLEVEL(logger_name, fmt, *args, stacklevel=3, **kwargs):
    '''
    '''
    logging.getLogger(logger_name).warning(logger_name, fmt, *args, stacklevel=stacklevel, **kwargs)

def LOG_ERROR_EX_WITH_STACKLEVEL(logger_name, fmt, *args, stacklevel=3, **kwargs):
    '''
    '''
    logging.getLogger(logger_name).error(fmt, *args, stacklevel=stacklevel, **kwargs)

########################################################################################################################
def auto_log_func_enter_exit(func):
    '''
    @brief 自动在函数调用前后添加日志输出
    @demo
        @auto_log_func_enter_exit
        def xxx_func():
            pass
    '''
    def wrapper(*args, **kwargs):
        LOG_DEBUG("[auto_log] enter_func: %s", func.__name__)
        ret = func(*args, **kwargs)
        LOG_DEBUG("[auto_log] exit_func: %s", func.__name__)
        return ret
    return wrapper




# # 绑定日志函数到builtins,实际绑导出了本模块所有LOG_开头的callable
if EXPORT_LOG_FUNC_TO_BUILTIN:
    __ALL_VARS = None
    if __ALL_VARS is None:
        __ALL_VARS = vars()
        import builtins
        def declareGlobals():
            def setVars(name:str, value):
                if name.startswith("__") or name.startswith("_"):
                    return
                if name == "declareGlobals" or name == "builtins":
                    return
                if not callable(value):
                    return
                if name.find("LOG_") < 0:
                    return
                if hasattr(builtins, name):
                    raise RuntimeError("duplicate environment variables %s"%(name))
                setattr(builtins, name, value)
            for name, value in __ALL_VARS.items():
                setVars(name, value)
        declareGlobals()



# 特化参数，日志函数将被高频调用尽量减少调用
#inspect.stack()[stack_depth].function
#文件名
#最大长度
#是否包含文件夹之类的

# 测试不触发异常的时候try-except开销
# 实际测试损耗3%左右，在2到5浮动
def test_try_except_cost():
    # pylint: disable=C0415
    import time
    # pylint: enable=C0415
    run_times = 10000000
    start_time = time.time()
    for n in range(0, run_times):
        #logger.debug("sadfsdfasdfasdfsdfasdfasd%skaslkdflaskd;ksd%s,%s", 111111111, "sdafsdfsdf", time, stacklevel=1)
        "sadfsdfasdfasdfsdfasdfasd%skaslkdflaskd;ksd%s" % (111111111, "sdafsdfsdf")
    raw_cost = time.time() - start_time
    start_time = time.time()
    for n in range(0, run_times):
        try:
            # debug函数已经做过异常保护，参数异常后续代码正常执行
            #logger.debug("sadfsdfasdfasdfsdfasdfasd%skaslkdflaskd;ksd%s,%s", 111111111, "sdafsdfsdf",1, time, stacklevel=1)
            "sadfsdfasdfasdfsdfasdfasd%skaslkdflaskd;ksd%s" % (111111111, "sdafsdfsdf")
        except TypeError as e:
            logger.error("log error: %s", e)
            break
    safe_call_cost = time.time() - start_time
    print(raw_cost)
    print(safe_call_cost)
    diff = safe_call_cost - raw_cost
    print(diff, diff / raw_cost)


def test_entry():
    n = 1
    dt = {1:1,2:3}
    LOG_DEBUG("test:%s", "str")
    LOG_DEBUG("test:%s,%s,%s", 666, dt, "777")
    test_try_except_cost()

if __name__ == "__main__":
    test_entry()

