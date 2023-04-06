# 定义一个类：
#    class 类名：
#       pass

class Money:
    pass

print(Money)  # <class '__main__.Money'> 表示money 是一个类
one = Money()
print(one)  # 表示通过money这个类来实例化了一个对象


# 属性相关
#   属性和变量的区别 以及 判定依据
#       区别：
#           概念：变量 -- 可以改变的量值， 属性 -- 属于某个对象的特性
#           访问权限：
#               变量： 根据不同的位置，存在不同的访问权限 -- 全局变量、局部变量
#               属性： 只能通过对象来进行访问 -- 所以，必须先找到对象， 对象也是通过变量名来引用，而既然是变量，也有对应的访问权限
#       判定依据： 是否存在宿主（宿主： 对象属性| 类属性） -- 属性： object.属性 <-- 进行获取

# ----------------------------------------------------------------
# 对象属性：
#   增 -- 让一个对象有一些属性
#       1， 直接通过对象，动态添加 -- 语法： 对象.属性 = 值
#       2， 通过类的初始化方法（构造方法） -- __init__ 方法
# 1,定一个类
class Person:
    pass

# 2,根据类，创建一个对象
p = Person()

# 3, 给p对象，增加一些属性
p.age = 18
p.height = 180

# 4，验证是否有添加成功
print(p.age)  # 18
print(p.__dict__)  # 这里是打印当前这个对象里面所有的属性  -- {'age': 18, 'height': 180}  -- 键： 属性名称

#   查 -- 访问一个对象的属性  -- 对象.属性名称

#   改 -- 修改一个对象的属性 -- 对象.属性 == 新值
p.pets = ["小花","小狗"]
print(id(p.pets))  # 1765324286144

p.pets = ["12312"]
print(id(p.pets))  # 1765324515200

# 注意  上面对象的属性存储的id 不同， 表示在重新赋值对象属性时，系统里是重新开辟了一个地方来存储新的属性值
# 要想在原本的属性上增加值，则需要用append来进行操作
p.pets.append("小美")
print(id(p.pets))  # 2012650432320


#   删 -- 删除一个对象的属性
# del 对象.属性名
# p.new = 10
# print(p.new)  # 10
# del p.new
# print(p.new)  # AttributeError: 'Person' object has no attribute 'new'


# ---- 可以见 面向对象 -- 对象属性-- 修改操作截图


# ----------------------------------------------------------------
# 类属性
#   类也是一个对象，只不过这个对象有些特殊

# --- 增
#   方式一： 类名.类属性 = 值
#   方式二： class Dag:
#               doigcount = 0
# 注意：
#   类里的属性增加，是不能通过实例化的对象 来进行增加类属性的
class Dag:
    pass

Dag.count = 1
print(Dag.count)  # 1
print(Dag.__dict__)  # {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dag' objects>, '__weakref__': <attribute '__weakref__' of 'Dag' objects>, '__doc__': None, 'count': 1}

class Counter:
    age = 10
    count = 100


print(Counter.age)  # 10
print(Counter.count)  # 100
print(Counter.__dict__) # {'__module__': '__main__', 'age': 10, 'count': 100, '__dict__': <attribute '__dict__' of 'Counter' objects>, '__weakref__': <attribute '__weakref__' of 'Counter' objects>, '__doc__': None}


# --- 查
# 方式1: 通过类访问： 类名.类属性
# 方式2：通过对象访问： 对象.类属性
#   注意：为什么可以通过对象访问到类属性
#       和Python对象的属性查找机制有关 -- 优先到对象自身取查找属性 -- 找到则结束
#                                    若果没有找到，则根据 __class__ 找到对象对应的类 到这个类里面查找
class Counter:
    age = 10
    count = 100


print(Counter.age)  # 10

one = Counter()
print(one.age)  # 10
print(one.__dict__)  # {}
print(one.__class__.__dict__)  # {'__module__': '__main__', 'age': 10, 'count': 100, '__dict__': <attribute '__dict__' of 'Counter' objects>, '__weakref__': <attribute '__weakref__' of 'Counter' objects>, '__doc__': None}


# -- 修改
# 只能通过类名来修改, 不能通过实例化的对象来修改
class Counter:
    age = 10
    count = 100

Counter.age = 18
print(Counter.age)  # 18 -- 这里修改了类属性的age 为18


ones = Counter()
print(Counter.age)
ones.age = 19
print(ones.age)  # 19 -- 表示在对象属性里新建了一个age属性 并赋值为19 ，类里面的属性和属性值不变
print(ones.__dict__)  # {'age': 19}
print(Counter.age)  # 18


# ----- 删除
#   del 类名.类属性名
#   注意： 类属性的删除操作，只能通过类进行删除，不能通过类实例化后的对象 来进行删除

class Counter:
    age = 10
    count = 100

# del Counter.age
# print(Counter.age)  # AttributeError: type object 'Counter' has no attribute 'age'


# 注意：
#   类属性的內存存储问题 -- 一般情况下，属性存存储在__dict__ 的字典中，有些内置对象没有这个 __dict__属性
#                       一般 对象 可以直接修改 __dict__属性
#                       但 类 对象的__dict__ 为只读，默认无法修改，可以通过setattr方法修改
#   类属性被各个对象共享
# 查看一个类的所有属性
#   类名.__dict__


#  添加属性限制： --  限制 对通过类 实例化的 对象 的属性添加
#   使用 __slots__ = [] 来限制添加的属性


class Person:
    __slots__ = ["age"]  # 这里表示 实例化的 对象 只能添加age这个属性 ，不能添加其他属性
    pass

p = Person()
p.age = 10
print(p.age)  # 10
p.height = 180
print(p.height)  # AttributeError: 'Person' object has no attribute 'height'  -- 这里会报错，不能添加除 age 之外的属性

