# --- 元类
# 概念：
#   创建对象的类 -- 对象是由类创建出来的 、 类也是一个对象、 所以类对象也是有另外一个类创建出来的
# 详情见 元类-- 演示图


# -----------------------类的创建方式 --------------------------------

# 正常的创建方式一 -- 自动创建
class Person:
    count = 0

    # 实例方法
    def eun(self):
        pass


# 用底层逻辑创建 -- 使用元类创建类
def run(self):
    print("----",self)

xxx = type("dog",(),{"count":0,"run":run})
print(xxx)  # <class '__main__.dog'>

print(xxx.__dict__)
# {'count': 0, 'run': <function run at 0x0000026C3167F670>, '__module__': '__main__',
# '__dict__': <attribute '__dict__' of 'dog' objects>,
# '__weakref__': <attribute '__weakref__' of 'dog' objects>, '__doc__': None}


d = xxx()
print(d)  # <__main__.dog object at 0x00000172CC2E3FD0>

d.run() # ---- <__main__.dog object at 0x00000274B10BAEE0>


# --------------------------- 类的创建流程 ---------------------------
# 一个类的创建 先从自身的描述中找寻指明的元类（使用 _ metaclass_）, 有的话就直接创建
# 若是没有指明，若存在继承时，则会去父类里面找，看父类里面有没有指明元类
# 若是还没有找到，则会去模块中寻找指明的元类，若是还没有找到，则会指明系统类的元类


# 检测类中是否有明确的__metaclass__ 属性
# 检测父类中是否存在__metaclass__ 属性
# 检测模块中是否存在 __metaclass__ 属性
# 通过内置的type这个元类，来创建这个类对象

# __metaclass__ 模块级别 -- 指明 创建的类的元类

# 指明元类方式一
class Person:
    __metaclass__ = xxx
    pass

# 指明元类 方式二
class Person(metaclass= xxx):
    pass


# 有继承关系

class Animal:
    pass

class Person(Animal):  # 表示Person 这个类继承了Animal类
    pass



