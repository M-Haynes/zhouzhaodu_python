# 私有化方法：
#   在函数前面加上 __ 将函数私有化
import panel.io.rest


# 内置特殊方法：
#   生命周期方法
#   其他内置方法：
#       信息格式化操作 -- __str__方法、 __repr__方法
#       调用操作 -- __call__方法
#       索引操作
#       切片操作
#       迭代器
#       描述器


# 信息格式化操作 -- __str__方法

class Person(object):

    def __init__(self, n, a):
        self.name = n
        self.age = a

    # 当我们想要打印一个对象，且这个对象有一定的格式时，可以借用 __str__ 实例方法
    def __str__(self):    # 实例作用 -- 信息格式化
        return "这个的姓名%s,这个人的年龄：%s"%(self.name,self.age)

# 方法一：
p1 = Person("sx", 18)
print(p1)  # 这个的姓名sx,这个人的年龄：18

# p2 = Person()
# print(p2)
# TypeError: __init__() missing 2 required positional arguments: 'n' and 'a' --这里调用这个方法需要传入参数

# 方法二：
s = str(p1)
print(s, type(s))  # 这个的姓名sx,这个人的年龄：18,  <class 'str'>


# 信息格式化操作 --  __repr__方法  == 获取这个实例对象的本质信息
class Person(object):

    def __init__(self, n, a):
        self.name = n
        self.age = a

    # 当我们想要打印一个对象，且这个对象有一定的格式时，可以借用 __str__ 实例方法
    def __str__(self):    # 实例作用 -- 信息格式化
        return "这个的姓名%s,这个人的年龄：%s"%(self.name,self.age)

    # 通过一个字符串来描述这个对象，这里面向的角色是开发者
    def __repr__(self):
        return "reprxxxxx"

p1 = Person("sx",18)
print(p1.age)
print(p1.name)
print(p1)  # 这个的姓名sx,这个人的年龄：18
# 运行结果：
# 18
# sx
# 这个的姓名sx,这个人的年龄：18

# 注意： 在调用Person这个类时，会先找__str__这个实例对象，有的话 执行， 没有的话，寻找并调用__repr__这个实例
p2 = Person("sc",13)
print(p2)  # 这个的姓名sc,这个人的年龄：13

# 方式一：
print(p2.__repr__())  # reprxxxxx
print(repr(p2)) # reprxxxxx

# 方式二：
#  直接在底下的交互窗口输入 类实例化的名称 就行

# 举例：
import datetime
t = datetime.datetime.now()
print(t)  # 2023-03-25 22:32:20.665740
print(repr(t))  # datetime.datetime(2023, 3, 25, 22, 32, 20, 665740)

# __repr__ 转成 __str__
res = eval(repr(t))
print(res) # 2023-03-25 22:34:29.656495


# --------------------------     调用操作 -- __call__方法  ------------------------
#   作用: 使得”对象“具备当做函数，来调用的能力
class Person(object):
    def __call__(self, *args, **kwargs):
        print("xxx",args,kwargs)
    pass

p = Person()
p()  # xxx () {} -- 使得Person这个对象，具有函数的能力 -- 这里对比类实例化函数的使用
p(123, 456, name = "zs") # xxx (123, 456) {'name': 'zs'}

# 具体的应用场景：
# 回顾 -- 偏函数

# 例子： 创建很多个画笔,画笔的类型(钢笔、铅笔)，画笔的颜色（红、黄、青、紫）
def creatPen(p_type,p_color):
    print("创建了一个%s 这个类型的画笔， 他是%s 颜色" %(p_type, p_color))


import functools
gangbi = functools.partial(creatPen, p_type = "钢笔")

gangbi(p_color="红色")
# 创建了一个钢笔 这个类型的画笔， 他是红色 颜色


# 面向对象的思路：
class PenFactory(object):
    def __init__(self,p_type):
        self.p_type = p_type

    def __call__(self, p_color):
        print("创建了一个%s 这个类型的画笔， 他是%s 颜色" %(self.p_type, p_color))

gangbiF = PenFactory("钢笔")
gangbiF("紫色")
# 创建了一个钢笔 这个类型的画笔， 他是紫色 颜色



# ---------------------------------- 索引操作 --------------------------------
# 作用：可以对一个实例对象进行索引
# 步骤：
#   1，实现三个内置方法
#   2，可以以索引的形式操作对象

# 对一个类的实例对象 -- 以字典的形式复制的时候，需要检测内置的函数 -- __setitem__、 __getitem__
class Person:

    def __init__(self):
        self.cache = {}

    def __setitem__(self, key, value):
        # print("setitem",key,value)
        self.cache[key] = value

    def __getitem__(self, item):
        # print("getitem",item)
        return self.cache[item]

    def __delitem__(self, key):
        # print("delitem",key)
        del self.cache[key]

p = Person()
p["name"] = "sx"

print(p["name"])
# 运行结果： None  -- 因为这里并进行存储，所以返回值是none-- 可以初始化__init__ 手动存入


# 增加了初始化实例 __init__ 后的运行
print(p["name"])  # sx

del p["name"]
# print(p["name"]) # KeyError: 'name' -- 这里表示字典中没有了name字典
print(p.cache)  # {} -- 这里表示字典中没有了name字典


# -------------------------------- 切片操作 --------------------------------
# Python3.x 统一由"索引操作"进行管理
#   def __setitem__(self, key, value)
#   def __getitem__(self, item):
#   def __delitem__(self, key):

class Person:
    def __setitem__(self, key, value):
        print("setitem",key,value)


p = Person()
p[0:4:2] = [1,2]
# 运行结果：
# setitem slice(0, 4, 2) [1, 2] -- etitem slice(0, 4, 2)表示切片对象

class Person:
    def __setitem__(self, key, value):
        print(key.start)
        print(key.stop)
        print(key.step)
        print(value)

p = Person()
p[0:4:2] = [1,2]
# 运行结果：
# 0
# 4
# 2
# [1, 2]
# p[0:5:2]  # TypeError: 'Person' object is not subscriptable -- 表明类对象里面没有获取实例

# 对上面报错的修正：
class Person:
    def __setitem__(self, key, value):
        print(key.start)
        print(key.stop)
        print(key.step)
        print(value)

    def __getitem__(self, item):
        print("getitem", item)

    def __delitem__(self, key):
        print("delitem", key)
p = Person()
p[0:5:2]  # getitem slice(0, 5, 2)  返回的是一个切片对象 slice(0, 5, 2)

del p[0:5:2]  # getitem slice(0, 5, 2)  表示删除了


# 对列表内的数值重新赋值操作
class Person:
    def __init__(self):
        self.items = [1,2,3,4,5,6,7,8,9]

    def __setitem__(self, key, value):
        self.items[key] = value
        # 或者 --这里要先判断是否是一个slice，有一个容错判断
        if isinstance(self.items,list):
            self.items[key.start: key.stop: key.step] = value

    def __getitem__(self, item):
        print("getitem", item)

    def __delitem__(self, key):
        print("delitem", key)
p = Person()
p[0:4:2] = ["a","b"]
print(p.items)  # ['a', 2, 'b', 4, 5, 6, 7, 8, 9] --这里是调用了__setitem__ 实例对列表进行了更改


# ------------------------------  比较操作 -----------------------------------
# 作用：可以自定义对象“比较大小，相等以及真假”规则
# 步骤：等于：__eq__
#      不等于： __ne__
#      小于：__lt__
#      小于等于：__le__
#      大于：__gt__
#      大于等于: __ge__

# 注意：
#   如果对于反向操作的比较符，只定义了其中一个方法，但使用的是另外一种比较运算
#   那么，解释器会采用调换参数的方式进行调用该方法
#   但是，不支持叠加操作

class Person:
    def __init(self,age,height):
        self.age = age
        self.height = height

    # == != > <  =>  <=

    # ==
    def __eq__(self, other):
    # 这里self,是第一个实例化对象参数，other 是第二个实例化对象参数化
        print(self)
        print(other)
        return self.age == other.age

    # !=
    def  __ne__(self, other):
        print("xxx")

    # >
    def __gt__(self, other):
        pass

    # >=
    def __ge__(self, item):
        pass

    # <
    def __lt__(self, other):
        pass

    # <=
    def __le__(self, other):
        pass


p1 = Person()
p2 = Person()
print("@"*100)
print(p1 != p2)
print(p1 <= p2)
# 巡行结果：
# xxx
# None
# None


# ------------------------------------ 上下文环境的布尔值 ----------------------------

class Person:

    def __init__(self):
        self.age = 10

    def __bool__(self):
        return self.age > 5

p = Person

if p:  # 非空即真，非0即真
    print("XX")  # XX


# --------------------------------------- 遍历操作 --------------------------------
# 遍历操作 -- 使用for  in  或者使用 迭代器来访问
# 现在 需要通过创建类 来实现 遍历操作

# for in 实现方式：
#   类 --  __getitem__方法 、 __iter__ 方法

# 方式一：
class Person:
    def __init__(self):
        self.result = 1

    # 设置循环遍历
    def __getitem__(self, item):
        self.result += 1
        if self.result >= 6:
            # 抛出异常
            raise StopIteration("停止遍历")
        return self.result
    pass

p = Person()

for i in p:
    print(i)
# 运行结果：
# 2
# 3
# 4
# 5

# 方式二：
class Person:
    def __init__(self):
        self.result = 1

    # 设置循环遍历
    def __getitem__(self, item):
        self.result += 1
        if self.result >= 6:
            # 抛出异常
            raise StopIteration("停止遍历")
        return self.result

    # 注意：__iter__的优先级比 __getitem__ 要高，两者存在时，是默认运行__iter__的
    # 这里__iter__ 函数的作用，跟iter的作用相同，将迭代对象设置成一个迭代器,可以通过设置__next__来访问
    def __iter__(self):
        # return iter([1,2,3,4,5,6,7,8])
        # 返回self 的意义是 ，将person这个实例当做一个迭代器
        return self  # 这里如果没有__next__实例方法，则会报错，因为返回的是没有next方法的迭代器 --TypeError: iter() returned non-iterator of type 'Person'

    def __next__(self):
        self.result += 1
        # 这个实例方法里面要设置一个终止条件
        if self.result >= 6:
            raise StopIteration("停止遍历")
        return self.result
    pass

p = Person()
print(p)  # <__main__.Person object at 0x0000020CBFE1EBE0>
for i in p:
    print(i)
# 实现机制：
# 在使用for in遍历一个对象时，首先会使用iter这个函数对p对象计算出里面的迭代器
#   而这个迭代器的获取方式，本质就是调用 __iter__这个方法来获取，拿到迭代器后，
#   会使用__next__方法来获取这个迭代器内的下一个数据，直到获取完毕，抛出一个stopiteration这个异常为止

# 运行结果：
# 2
# 3
# 4
# 5


# -------------------------------- 恢复迭代器初始值 ------------------------------------------
class Person(object):
    def __init__(self):
        self.age = 1

    def __iter__(self):
        self.age = 1  # 表示将迭代重置了，这样就可以多次使用迭代器
        return self

    def __next__(self):
        self.age += 1
        if self.age >6:
            raise StopIteration("stop")
        return self.age

p = Person()

import collections
# 注意：必须要有 __iter__ 和 __next__在一起，才是一个迭代器，否则则不是
# 而 __iter__ 只表示一个可迭代的对象， 可迭代对象-- 可以用for in 进行遍历，反之则不一定（__getitem__ 方法）
print(isinstance(p,collections.Iterator))

for i in p:
    print(i)

# 运行结果：
# True
# 2
# 3
# 4
# 5
# 6


#  -------------------------------------- __iter__ 函数的使用 -----------------------------
# 将对象转成一个迭代器

class Person:
    def __init__(self):
        self.result = 1

    # 设置循环遍历
    # def __getitem__(self, item):
    #     self.result += 1
    #     if self.result >= 6:
    #         # 抛出异常
    #         raise StopIteration("停止遍历")
    #     return self.result

    def __iter__(self):
        return self
    def __next__(self):
        self.result += 1
        if self.result >= 6:
            raise StopIteration("停止遍历")
        return self.result

    # 当没有__next__方法时，需要使用 __call__方法，将对象变成一个方法来执行
    def __call__(self,*args,**kwargs):
        self.result += 1
        if self.result >= 6:
            raise StopIteration("停止遍历")
        return self.result


p = Person()

print("$"*100)
# 当只有__getitem__， 没有__iter__、和__next__ 方法时
# pt = iter(p)  # 将对象p 编程一个迭代器
# pt = iter(p.__next__, 4)  # 2,3 -- 表示直接调用内置__next__函数进行遍历，并判断是否大于4
pt = iter(p, 4)  # 使用__call__ 方法
# 运行结果：
# 2
# 3

for i in pt:
    print(i)
# 运行结果：
# 2
# 3
# 4
# 5

# 当有 __iter__、和__next__ 方法时,  没有__getitem__ -- __iter__ 方法本质就是将p对象转换成迭代器

pt = iter(p)
print(pt is p)  # True


# -------------------------------------- 描述器 --------------------------
# 概念：可以表述一个属性操作的对象
# 概念：一个类里面有一个属性，这属性 指向一个特殊对象，这对象里面实现了三个特殊的实例方法：__set__、 __get__、__delete__
# 则将这样一个对象称为一个描述器，详情见描述器原理.png

# 定义方式1： -- property -- 将类中的方法封装成一个属性（描述器）
class Person(object):
    def __init__(self):
        self.__age = 10

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            value = 0
        self.__age = value

    def del_age(self):
        del self.__age

    # 这里通过 property 来将方法设置成属性
    age = property(get_age, set_age, del_age)


# 使用 调用类里面的方法来进行操作
p = Person()
print(p.get_age())  # 10 -- 这里是通过调用方法 来获取类里面的私有属性值

p.set_age(-10)
print(p.get_age())
# 运行结果： 0

# 使用property 将方法设置成属性后
# p1 = Person()
# print(p1.age)  # 10
# del p.age
# print(p.age)  # AttributeError: 'Person' object has no attribute '_Person__age'

# help(Person)
# class Person(builtins.object)
#  |  Methods defined here:
#  |
#  |  __init__(self)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  del_age(self)
#  |
#  |  get_age(self)
#  |
#  |  set_age(self, value)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:  数据描述器
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  age


class Person(object):
    def __init__(self):
        self.__age = 10
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if value < 0:
            value = 0
        self.__age = value
    @age.deleter
    def age(self):
        del self.__age

p3 = Person()
p3.age = 19
print(p3.age)  # 19
del p3.age


# -------------------------------  描述器 - 定义方法2 ---------------------------------
# 定义一个类，设置描述器
class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, instance):
        print("delete")

class Person:
    age = Age()  # 系统会自动识别这个类为描述器 ， 调试的话  是通过实例来调用，而不是用过类（person）


p = Person()
p.age = 10
print(p.age)
del p.age

# 运行结果
# set
# get
# None  -- 因为 print(p.age) 这个步骤中，Age类没有返回值  所以 是None
# delete


# --------------------------------- 不能够顺利转换的场景 -----------------------------
# 一个实例属性的正常访问顺序
#   实例对象自身的__dict__字典
#   对应类对象的__dict__字典
#   如果有父类，会在往上层的__dict__字典中检测
#   若果没有找到，又定义了__getattr__方法，就会调用这个方法

# 而在上述的整个过程中，是如何将描述器的__get__方法嵌入到查找机制的？
# 就是通过这个方法实现
#   __getattribute__
#   内部实现模拟 -- 如果实现了描述器方法__get__就会直接调用
#   如果没有，则按照上面的机制去查找

class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, instance):
        print("delete")

class Person:
    age = Age()
    def __getattribute__(self, item):
        print("XXXXXXX")

print("#"*100)
p5 = Person()
p.age = 10
print(p5.age)
# del p5.age
# 运行结果：
# set
# XXXXXXX -- 这里我们自己将系统内的访问函数重新定义了，所以导致了没有办法进行对应装饰器里面方法的调用
# None
# delete


# -----------------------------------------描述器 - 和 实例属性 同名时，操作优先级  -----------------------
# 资料描述器 get set
# 非资料描述器  仅仅实现了 get 方法， 那么他就是一个非资料描述器
# 资料描述器 > 实例属性 > 非资料描述器

# 资料描述器
class Age(object):
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, instance):
        print("delete")

class Person:
    age = Age()

    def __init__(self):
        self.age = 10

print("&"*100)

p9 = Person()
p9.age = 10
print(p9.age)
print(p9.__dict__)

# 运行结果：
# set -- 这里在创建person实例时，会自动的执行__init__ 方法： self.age = 10 这时候会调用Age中的方法：__set__
# set -- 这里执行了p.age = 10 就再次执行了Age中的方法：__set__
# get
# None
# {}  -- 表示 p9这个实例属性是一个空的字典

# 非资料描述器
class Age(object):
    def __get__(self, instance, owner):
        print("get")


class Person:
    age = Age()

    def __init__(self):
        self.age = 10

print("&"*100)

p9 = Person()
p9.age = 10
print(p9.age)
print(p9.__dict__)

# 运行结果：
# 10
# {'age': 10}


# -----------------------------------------描述器 - 值的存储问题  -----------------------
# 注意： 描述器内的存储__dict__ 是共享的，
#   也就是说，当我们通过创建了person的不同的实例，但是调用的描述器Age是相同的存储地址，但是创建的person类存储是不同的
#   所以这里修改的值绑定的应该是person类中的__dict__

class Age(object):
    def __get__(self, instance, owner):
        return instance.v
        # print("get")

    def __set__(self, instance, value):
        instance.v = value
        print("set",self,instance,value)
        # set
        # self : <__main__.Age object at 0x000001154CA55D60>
        # instance : <__main__.Person object at 0x000001154CABDC40>
        # value : 10

    def __delete__(self, instance):
        print("delete")

class Person:
    age = Age()


print("&"*100)
p9 = Person()
p9.age = 10
print(p9.age)
print(p9.__dict__)

p10 = Person()
p10.age = 12
print(p10.age)
print(p10.__dict__)
print(p9.__dict__)

# 运行结果：
# set <__main__.Age object at 0x00000151B6E78100> <__main__.Person object at 0x00000151B6F52C10> 10
# 10
# {'v': 10}
# set <__main__.Age object at 0x00000151B6E78100> <__main__.Person object at 0x00000151B6E784C0> 12
# 12
# {'v': 12}
# {'v': 10}


