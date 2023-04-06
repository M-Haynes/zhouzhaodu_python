# 形参： 函数定义时,设置的”参数名称“即为形参
# 实参： 在调用函数的时候，传递的真实数据，即为实参


# ------------------------------------ 多个参数 ----------------------------------------------------------------
#   需要动态的调整函数体中多个处理信息时， 可以用 逗号 做分割，接收多个参数
# 定义：
#       def 函数名(参数1， 参数2):
#           函数体 -- 函数体中，可以直接以变量的方式使用所有参数
# 调用方式：
#       方式一： 函数名(参数1，参数2，参数3....)  -- 形参和实参一一对应
#       方式二： 函数名(参数名1 = 参数1， 参数名2 = 参数2) -- 指明形参名称， 不需要严格按照顺序


# ------------------------------------不定长参数 -------------------------------
# 定义：
#   def函数名(*args):  --- 传入的参数形式是一个元组
#       函数体 --  函数体中，可以直接以元组变量的方式使用该参数
# 使用方式：
#   函数名(参数1， 参数2 ，参数3)

def my_sum(*args):
    print(args,type(args))  # (1, 2, 23, 3, 42) <class 'tuple'>
    sum = 0
    for i in args:
        sum += i
    return sum

my_sum(1, 2, 23, 3, 42)


# 定义：
#   def 函数(**kwargs):  -- 传入的形式是一个字典的形式
#       函数体 -- 函数体中，可以直接以字典变量的方式使用该参数
# 使用方式：
#   函数名(参数名称1 = 参数1， 参数名称2 = 参数2...)

def my_key(**kwargs):
    print(kwargs, type(kwargs))  # {'name': '牛', 'age': '20'} <class 'dict'>

my_key(name="牛", age="20")


# ------------------------------------- 参数的拆包 和 装包 --------------------------------
# 装包 -- 把传递的参数，包装成一个集合，称之为“包装”
# 拆包 -- 把集合参数，再次分解成单独的个体，称之为拆包

def mysum(a, b, c, d):
    print(a+b+c+d)

def tt(*args):
    print(args)

    # 拆包
    print(*args)
    # 这里错误是因为 test传入的参数是元组类型，作为一个整体
    # mysum((1,2,3,4))  # TypeError: mysum() missing 3 required positional arguments: 'b', 'c', and 'd'
    mysum(args[0], args[1], args[2], args[3]) # 10

    # 直接拆包
    mysum(*args)  # 10

tt(1, 2, 3, 4)


def myab(a, b):
    print(a)
    print(b)

def input_test(**kwargs):
    print(kwargs)
    # 拆包操作：
    # 应该使用 ** 进行拆包操作
    # a=1, b=2
    # 注意： 拆包后的数据和输入时的数据一一对应
    myab(**kwargs)  # 1 , 2
    myab(a=1, b=2)

input_test(a=1, b=2)


# ------------------------------------- 缺省参数 -------------------------------------
# 场景：
#       使用一个函数的时候，如果大多数情况下， 使用的某个数据是一个固定值，或者属于主功能之外的小功能实现，
#       则可以使用默认值 -- 这种参数，称为“缺省参数”
# 定义：
#       def 函数名(变量名1 = 默认值1，变量名2 = 默认值2)：
#           函数体 --  函数体中，即使外接没有穿肚指定变量，也可以使用，只不过值是给定的默认值
# 使用：
#       函数名(变量1，变量2) -- 此处如果是缺省参数，则可以不填写

def hit(some="豆豆"):
    print("我想打", some)

hit("zhangsan")  # 我想打 zhangsan
hit()  # 我想打 豆豆


# -------------------------------- 参数注意事项 ----------------------------------------------------------------
# 值传递 和 引用传递
# 值传递：
#   是指传递过来的，是一个数据的副本，修改副本，对原件没有影响
# 引用传递:
#   是指传递多来的，是一个变量的地址，通过地址，可以操作同一份原件

# 注意:
#   在Python中，只有引用传递（地址传递）
#       但是 如果传入的数据类型是可变类型，则可以改变原件， 数据类型是不可变类型，则不可以改变原件，重新开辟一个空间存储

def tt(num):
    print(id(num))  # 1772255926448

a = 123
print(id(a))  # 1772255926448
tt(a)
# 函数中的num地址 和 传入的a 的地址一样


# ------------------------------------- 函数的使用描述 -------------------------------------
# 一般函数的描述，需要说明如下几个信息：
#   函数的功能
#   参数 -- 含义、类型、是否可以省略、默认值
#   返回值 -- 含义、类型


# ------------------------------------- 偏函数 --------------------------------
# 概念&场景：
#       当有些参数， 在大部分场景下都是某一个固定值， 为了简化使用，可以创建一个新函数，指定我们要使用的函数的某个参数
#       为了某个固定的值，这个新函数就是"偏函数"

# 方式一：
#   自己写一个新的
def tt_1(a, b, c, d=1):  # 这里固定了d为默认值1
    print(a+b+c+d)


def tt_2(a, b, c, d=2):  # 当我们想要发现d=2 也是一个常用数据 --这里就可以写一个新函数来对d进行默认
    tt_1(a, b, c, d)

tt_2(1, 2, 3)  # 8


# 方式二：
# 借助functools模块的partial函数：
#      import functools
#           newFunc = functools.partial(函数，特定参数 = 偏爱值)

import functools
newFunc = functools.partial(tt_1, c=5)  # 这里使用了函数 对 tt_1 这个函数中的c设置为默认值5
print(newFunc, type(newFunc))

newFunc(1, 2)  # 9


# 举例场景：
numStr = "10010"
result = int(numStr, base = 2)
print(result)  # 18

# 假设在往后的一段时间内，我都需要把一个二进制的字符串，转换成对应的十进制数据
import functools
int2 = functools.partial(int, base = 2)
print(int2(numStr))  # 18


# ------------------------------------- 高阶函数 -------------------------------------
# 概念：
#   当一个函数A的参数，接收的又是另一个函数时，则把这个函数A称为是"高阶函数"
# 例如： sorted() 函数

l = [{"name":"sz","age":18,"weight":120},{"name":"sz2","age":13,"weight":110},{"name":"sz3","age":23,"weight":160}]

def getkey(x):  # 这里的参数x 一定要有
    return x["name"]

result = sorted(l, key=getkey, reverse=True)
print(result)  # [{'name': 'sz3', 'age': 23, 'weight': 160}, {'name': 'sz2', 'age': 13, 'weight': 110}, {'name': 'sz', 'age': 18, 'weight': 120}]


# 动态的计算两个数据
def caculate(num1, num2, caculteFunc):
    result = caculteFunc(num1, num2)
    print(result)

def sum(a,b):
    return a+b

def jianfa(a,b):
    return a-b

caculate(1, 2, jianfa)  # -1 -- 这里是调用jiafa函数

caculate(6, 2, sum)  # 8


# ------------------------------------------ 返回函数 --------------------------------
# 概念：
#   是指一个函数内部，它返回的数据是另外一个函数； 把这样的操作称为“返回函数”
#   根据不同参数，获取不同操作，做不同计算

def getFunc(flag):
    # 1,再次定义几个函数
    def sum(a, b, c):
        return a+b+c
    def jian(a, b, c):
        return a-b-c

    # 2 根据不同的flag值，来返回不同的操作函数
    if flag == "+":
        return sum   # 这里是将整sum函数返回
    elif flag == "-":
        return jian  # 这里是将jian函数返回

result = getFunc("+")  # 这里返回的是sum函数
print(result, type(result))  # <function getFunc.<locals>.sum at 0x00000219CCBD33A0> <class 'function'>

res = result(1, 2, 3)
print(res, type(res))  # 6 <class 'int'>


# ------------------------------------------ 匿名函数 ------------------------------------------
# 概念：也称为"lambda函数" -- 顾名思义，就是指没有名字的函数
# 语法：
#   lambda 参数1，参数2.... : 表达式
#   限制： 只能写一个表达式，-- 不能直接return
#         表达式的结果就是返回值，所以，只适用于一些简单的操作处理

l = [{"name":"sz","age":18,"weight":120},{"name":"sz2","age":13,"weight":110},
     {"name":"sz3","age":23,"weight":160}]

# def getkey(x):  # 这里的参数x 一定要有
#     return x["name"]
# result = sorted(l, key=getkey, reverse=True)

result = sorted(l,key = lambda x: x['name'],reverse=True)
print(result)  #  [{'name': 'sz3', 'age': 23, 'weight': 160}, {'name': 'sz2', 'age': 13, 'weight': 110}, {'name': 'sz', 'age': 18, 'weight': 120}]


# ------------------------------------------ 闭包 ------------------------------------------
# 概念：
#   在函数嵌套的前提下，内层函数引用了外层函数的变量(包括参数)
#   外层函数，又把 内层函数，当做返回值 进行返回
#       这个内层函数+ 所引用的外层变量，称为"闭包"

# 注意事项：
#   1，闭包中，如果要修改引用的外层变量，需要使用nonlocal变量 申明，否则当做是闭包内，新定义的变量
#   2，当闭包内，引用了一个，后期会发生变化的变量是，一定要注意

def tt():
    s = 10  # 外层函数的定义变量
    def tt2():
        print(s)  # 这里是引用了外层函数的变量
    return tt2  # 注意： 这里不是调用函数，而是返回整个函数

newFunc = tt()
newFunc()  # 10


# 标准格式：
#   def test1(a):
#       b = 10
#     其他函数定义代码：
#           def test():
#               print(a)
#               print(b)
#        return test2


# 应用场景：
def line_confing(content,length):

    def line():
        print("_"*(length // 2) + content + "_"*(length //2))
    return line

line = line_confing("闭包",20)

line()  # __________闭包__________

# 假设现在我需要别的名称的分割符
line1 = line_confing("你好",30)
line1()  # _______________你好_______________


# 注意事项举例：
def tes1():
    num = 10
    def tes2():
        num = 666  # 这里是内部函数重新定义的变量值，这里的变量值是内部独立的
        print(num)

    print(num)  # 这里是调用外部的变量num
    tes2()  # 这里是打印了内部的变量 num = 666
    print(num)  # 10 这里是因为内部的num没去修改外部的变量

    return tes2

result = tes1()
# result()  # 10


# 将内部的num申明为全局变量
def tes1():
    num = 10
    def tes2():
        nonlocal num
        num = 666  # 这里是内部函数重新定义的变量值，这里的变量值是内部独立的
        print(num)

    print(num)  # 这里是调用外部的变量num
    tes2()  # 这里是打印了内部的变量 num = 666
    print(num)  # 666

    return tes2

result = tes1()


# 函数，什么时候，才会确定，内部，变量标识，对应的值
# 当函数被调用的时候，才会真正的确定，对应的值，到底是什么，在此之前，都是以普通的变量标识名称而存在
def tes1():
    a = 1
    def tes2():
        print(a)
    a = 2
    return tes2

newFunc = tes1() # 这时候的tes1中没有调用tes2,而是直接将a的值赋值为2
newFunc() # 这里是调用tes1函数，执行了tes2 函数，在tes2函数中执行了打印a值，这里a 已经赋值为2了，所以打印出来的值为2


# 举例2
def tess1():
    funs = []
    for i in range(1,4):
        def tess2(num):
            def inner():
                print(num)
            return inner
        funs.append(tess2(i)) # 这里作用是调用了tess2 函数的执行，但是并没有执行inner,而是将inner函数整个放入了列表中
    return funs

newFunc = tess1()
print(newFunc)  #  [<function tess1.<locals>.tess2.<locals>.inner at 0x0000018EFE7B4820>, <function tess1.<locals>.tess2.<locals>.inner at 0x0000018EFE7B4790>, <function tess1.<locals>.tess2.<locals>.inner at 0x0000018EFE7B48B0>]
# 注意： 这里返回的是三个inner函数

newFunc[0]()  # 这里是执行了newFunc列表中的第一个inner函数，答应的值是 -- 1
newFunc[1]()  # 这里是执行了newFunc列表中的第一个inner函数，答应的值是 -- 2

