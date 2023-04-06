# -- 类方法：
class Person:
    @classmethod
    #     classmethod(function) -> method
    #     Convert a function to be a class method
    def leifangfa(cls,a):
        print("这是一个类方法",cls,a)

# 通过类进行访问
Person.leifangfa(123)  # 这是一个类方法 <class '__main__.Person'> 123


# 通过实例进行访问，返回的是这个实例所对应的类，这个实例会被忽略
p = Person()
p.leifangfa(666)  # 这是一个类方法 <class '__main__.Person'> 666

func = Person.leifangfa
func(111)  # 这是一个类方法 <class '__main__.Person'> 111

# 装饰器的作用：在保证原本函数不改变的前提下，直接给这个函数增加一些功能


class A(Person):  # 表示建立了一个新类，来继承了Person这个类
    pass

# 使用衍生类来调用类方法，则会将这个衍射类本身传递给这个方法的第一个参数
A.leifangfa(0)  # 这是一个类方法 <class '__main__.A'> 0
