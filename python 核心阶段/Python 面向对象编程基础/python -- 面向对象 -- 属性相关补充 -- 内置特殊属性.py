# 内置特殊属性
# ----------------------- 类属性： ------------------------
# __dict__: 类的属性
# __bases__: 类的所有父类构成元组
# __doc__: 类的文档字符串 -- 即类的描述说明，而不是方法的描述
# __namne__: 类对象对应的名称
# __module__: 类定义所在的模块


class Person(object):
    """
    这是一个类！！
    """
    def __init__(self):
        """
        这是一个初始化实例
        """
        self.age = "1213"

    def run(self):
        print("run")


print(Person.__dict__)
# {'__module__': '__main__', '__init__': <function Person.__init__ at 0x000002761CDF9670>,
# 'run': <function Person.run at 0x0000027619B883A0>, '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

print(Person.__bases__)  # (<class 'object'>,)

print(Person.__doc__)  # 这是一个类！！

print(Person.__name__)  # Person -- 类对象的名称

print(Person.__module__)  # __main__


# ------------------------- 实例属性：------------------------------------
# __dict__: 实例的属性
# __class__: 实例对应的类

p = Person()
print(p.__class__)  # <class '__main__.Person'>
