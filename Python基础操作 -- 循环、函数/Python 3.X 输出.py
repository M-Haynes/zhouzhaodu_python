# Python 输出
import sys
import time
# 输出一个值
print(123)

# 输出一个变量
num = 55
print(num)

# 输出多个变量
num2 = 22
print(num, num2)

# 格式化输出
name = 'qw'
age = 18
# 我的名字是XXXX，年龄XXX
print("我的名字是%s,年龄是%d" % (name,age))
# 注意 %s 指执行字符串格式化，%d 指数字也是整数，这里跟%i一样， %f 指执行浮点数格式化
print("我的名字是{0}，年龄是{1}".format(name,age))

# 输出到文件中
f = open("test.txt", "w")
print("XXXXXX",file=f)

# 输出不自动换行
print("abc",end= "\n")  # end表示以什么结束

# 输出的各个数据，使用分割符分割
print("1","2","3",sep= "__")

# flush 参数的说明  # 对输出的内容不设置时间，直接将存在缓存内的输出内容打印出来
print("请输出",end ="",flush=True)
time.sleep(5)

mas = 10
# width, 表示占用的宽度
print("%-10d"% mas)  # 表示左对齐，输出10个位

# 用0 来填充空位
min = 5
sec = 10
# 05:18
print("%02d:%02d" % (min, sec))

# 浮点数的输出
scorer = 59.99
print("%.2f"% scorer)

# %g 自动调整输出的格式

# 动态实现%号输出
#99%
print("99%")
score = 55
print("%d%%"%score)




