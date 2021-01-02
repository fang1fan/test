from time import time

def cal_time(func):

    # 定义嵌套函数，用来打印出装饰的函数的执行时间
    def wrapper(*args, **kwargs):
        # 定义开始时间和结束时间，将func夹在中间执行，取得其返回值
        start = time()
        func_return = func(*args, **kwargs)
        end = time()
        # 打印方法名称和其执行时间
        print(f'{func.__name__}() execute time: {end - start}s')
        # 返回func的返回值
        return func_return

    # 返回嵌套的内层函数
    return wrapper
