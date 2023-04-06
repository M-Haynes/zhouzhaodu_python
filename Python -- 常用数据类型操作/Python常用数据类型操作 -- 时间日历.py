# ---------------------------------------------time模块 --------------------------------------
# 提供了处理时间和表示之间转换的功能
# 获取当前时间戳
    # 概念 -- 从0时区的1970年 1月1号 0：0：0 到给定日期时间的秒数 --  浮点数
    # 获取方式：
#       import time
#           time.time()
import time
result = time.time()


# 获取时间元组
# 概念 -- 很多Python时间函数将时间处理为9个数组的元组
#       0 -- 含义：4位数年，属性：Tm_year, 值：2008
#       1 -- 含义：月， 属性：tm_mon, 值：1-12
#       2 -- 含义：日， 属性：tm_mday， 值：1-31
#       3 -- 含义：小时， 属性： tm_hour， 值：0-23
#       4 -- 含义：分钟， 属性：tm_min， 值：0-59
#       5 -- 含义：秒，属性：tm_sec， 值：0-61
#       6 -- 含义：一周的第几日， 属性：tm_wday， 值：0-6 (0是周日)
#       7 -- 含义：一年的第几日， 属性：tm_yday， 值：1-366
#       8 -- 含义：夏令时， 属性：tm_isdst，  值：-1（决定是否为夏令时的标记）,0,1
# 获取方式： time.localtime([seconds])
#           seconds -- 可选的时间戳，默认为当前时间戳
res_time = time.localtime()
print(res_time)  # time.struct_time(tm_year=2023, tm_mon=2, tm_mday=27, tm_hour=23, tm_min=0, tm_sec=38, tm_wday=0, tm_yday=58, tm_isdst=0)


# 获取格式化时间
#   秒 -> 可读时间
#       import time
#       time.ctime([seconds])
#           seconds --  可选的时间戳，默认为当前时间戳

t = time.time()
res = time.ctime(t)
print(res)  # Mon Feb 27 23:05:36 2023


#   时间元组 -> 可读时间
#       import time
#           time.asctime([p_tuple])
#               p_tuple --  可选的时间元组，默认为当前时间元组

time_tuple = time.localtime()
ress = time.asctime(time_tuple)
print(ress)  # Mon Feb 27 23:08:11 2023


# 格式化日期字符串 < -- > 时间戳
#  时间元组  -- > 格式化日期
#   time.strftime(格式字符串， 时间元组)
#   例如：
#       time.strftime("%Y-%m-%d  %H:%M:%s", time.localtime())
#       2023-02-28 20:15:00

result_format = time.strftime("%y-%m-%d %H-%M-%S", time.localtime())
print(result_format)  #  23-02-27 23-30-09


# 格式化日期 -> 时间元组
#   time.strptime(日期字符串，格式符字符串)

pt = time.strptime("23-02-27 23-30-09", "%y-%m-%d %H-%M-%S")
print(pt) # time.struct_time(tm_year=2023, tm_mon=2, tm_mday=27, tm_hour=23, tm_min=30, tm_sec=9, tm_wday=0, tm_yday=58, tm_isdst=-1)


# 时间元组 -> 时间戳
#   time.mktime(时间元组)
tt = time.mktime(pt)
print(tt)  # 1677511809.0


# 获取当前CPU时间
# time.perf_counter() -- 浮点数的秒数
#   可用来统计一段程序代码的执行时间

start_time = time.perf_counter()
for i in range(0, 100):
    print(i)
end_time = time.perf_counter()
print(end_time - start_time)


# 休眠n秒
#   推迟线程的执行
#       time.sleep(seconds)


# ----------------------------- calendar 模块 ----------------------------------------------------------------
#   提供与日历相关的功能，比如：为给定的月份或年份打印文本日历的功能
#   import calendar
#       calendar.month(2023,9)

import calendar
print(calendar.month(2023, 9))
#    September 2023
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30


# --------------------------------datetime 模块 ----------------------------------------------------------------
# Python处理日期和时间的标准库
#   模块中有datetime类，还有date类，以及time类
#   可以做一些计算之类的操作

# 获取当天日期
import datetime
rest1 = datetime.datetime.now()
rest2 = datetime.datetime.today()
print(rest1, rest2)  #  2023-02-28 08:37:57.515432   2023-02-28 08:37:57.515432
print(type(rest1), type(rest2))  # <class 'datetime.datetime'> <class 'datetime.datetime'>
# 注意： 上面的rest1,rest2 类型是一个对象 -- 原因是datetime是一个类，想要获取具体的信息，可以采用类的方式进行调用
# 单独获取当前的年月日时分秒
print(rest1.year)  # 2023
print(rest2.month)  # 2
print(rest1.day)  # 28
print(rest1.minute)  # 43


# 计算n天之后的日期
#   datetime.timedalta() 函数
import datetime
t = datetime.datetime.today()
st = datetime.timedelta(days=7)
result = t + st
print(t, result)  # 2023-02-28 21:59:33.913650,  2023-03-07 21:59:33.913650


# 计算两两个日期的时间差
import datetime
first_time = datetime.datetime(2023, 9, 1, 12, 00, 00)
second_time = datetime.datetime(2023, 9, 4, 12, 0, 0)
print(first_time, type(first_time))  # 2023-09-01 12:00:00 <class 'datetime.datetime'>
result = second_time - first_time  # 259200.0
print(result.total_seconds())
