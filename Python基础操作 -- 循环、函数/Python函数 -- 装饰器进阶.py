# ------------------------- 装饰叠加 ------------------------
#   从上到下装饰， 从下到上执行

def zhuangshiqi_line(func):
    def inner():
        print("-"*30)
        func()
    return inner

def zhuangshiqi_star(func):
    def inner():
        print("*"*30)
        func()
    return inner

@zhuangshiqi_line  # == print_content = zhuangshiqi_line(print_content)
@zhuangshiqi_star  # == print_content = zhuangshiqi_star(print_content)
# print("-"*30)
# print("*"*30)
# print("社会我周哥，人狠话不多")
def print_content():
    print("社会我周哥，人狠话不多")

print_content()
# 结果：
    # ------------------------------
    # ******************************
    # 社会我周哥，人狠话不多


# -----------------------  对有参数进行装饰 ------------------------
#   无论什么场景，保证函数调用参数个数一致
#   为了通用，可以使用不定长参数，结合 拆包操作进行处理

def zsq(func):
    def inner(n1, n2):
        print("#"*20)
        func(n1, n2)
    return inner

@zsq
def print_content(n1, n2):
    print(n1, n2)

print_content(111,222)  # 注意 inner()函数传入的参数要和print_content一致
# 结果:
#   ####################
#   111 222


# -----------------------  使用不定长参数进行装饰 ------------------------
# 闭包函数中要记得拆包
def zsq(func):
    def inner(*args, **kwargs):
        print(args,kwargs)  # (111, 222) {'num3': 333}  这里将参数整体传入
        print("#"*20)
        func(*args, **kwargs)  # 这里是将参数拆包后，放入了fun函数中进行执行
    return inner

@zsq
def print_content(num1, num2, num3):
    print(num1, num2, num3)


print_content(111, 222, num3 = 333)
# 返回值：
#   ####################
#   111 222 333


# -----------------------  对有返回的函数进行装饰   ------------------------
# 无论什么场景，保证函数返回值一致
# 注意： 被装饰的函数里的格式要和inner闭包函数的格式一样才行

# inner闭包函数 和 装饰函数格式 不一样的情况：
def zsq(func):
    def inner(*args, **kwargs):
        print(args,kwargs)  # (111, 222) {'num3': 333}  这里将参数整体传入
        print("#"*20)
        func(*args, **kwargs)  # 这里是将参数拆包后，放入了fun函数中进行执行
    return inner

@zsq
def pnum(num1, num2, num3):
    print(num1, num2, num3)
    return num1+num2+num3  # 这里被装饰的函数中返回传入参数的和，同理调用的inner闭包函数中也要有对应的格式

@zsq
def pnum2(num):
    print(num)


res1 = pnum(111,222,333)
res2 = pnum2(123)

print(res1, res2)  # None None 这里返回None是因为 在调用inner函数时，并没有返回值，所以返回的是none

# inner闭包函数 和 装饰函数格式 一样的情况：
def zsq(func):  # 装饰器函数
    def inner(*args, **kwargs):
        # print(args,kwargs)
        # print("#"*20)
        res = func(*args, **kwargs)  # 这里是将参数拆包后，放入了fun函数中进行执行
        return res  # 这里的返回值 就是被装饰的函数（pnum / pnum2 ）执行的结果
    return inner

@zsq
def pnum(num1, num2, num3):
    print(num1, num2, num3)
    return num1+num2+num3  # 这里被装饰的函数中返回传入参数的和，同理调用的inner闭包函数中也要有对应的格式

@zsq
def pnum2(num):
    print(num)  # 这里被装饰的函数没有返回值 ， 则相当于None


res1 = pnum(123, 456, 789)
res2 = pnum2(258)

print(res1, res2)  # 1368 None # 666 表示的是将传入的参数进行了相加并返回打印，None是因为 pnum2 函数中没有对传入参数相加

# 程序执行的数据：
# re1:
#   123 456 789

#  res2:
#   258

# print打印：
#   1368 None


# --------------------------------  带有参数的装饰器 ----------------------------------------------------------------
# 通过@装饰器（参数） 的方式，调用这个函数，并传递参数，并把返回值，再次当做装饰器进行使用
# 先计算@ 后面的内容，把这个内容当做是装饰器

def getzsq(char):  # 这里的参数是装饰器的参数, 根据不同的参数生成不同的装饰器
    def zsq(func):
        def inner(*args, **kwargs):
            print(char*20)
            res = func(*args, **kwargs)  # 这里是将参数拆包后，放入了fun函数中进行执行
            return res  # 这里的返回值 就是被装饰的函数（pnum / pnum2 ）执行的结果
        return inner
    return zsq   # 这里是返回装饰器



@getzsq('#')
def fss():  # 被装饰函数
    print(123)

fss()

# 程序运行结果：
# ##################
# 123

@getzsq("A")
def fsa():  # 被装饰函数
    print(258)

fsa()

# 程序运行结果：
# AAAAAAAAAAAAAAAAAAAA
# 258


