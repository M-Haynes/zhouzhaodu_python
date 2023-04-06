
# 类属性 和 实例属性 -- 区别： 存储地方不同,
class Person:
    age = 10
    def shilifangfa(self):
        print(self)  #
        print(self.age)
        print(self.num)

    @classmethod
    def leifangfa(cls):
        print(cls)
        print(cls.age)
        print(cls.num)

    @staticmethod
    def jingtailfangfa():
        print(Person.age)


p = Person()
p.num = 10  # 这里增加一个实例属性 num

# 实例化方法调用属性
p.shilifangfa()
# 执行结果：
#<__main__.Person object at 0x000001E889DD9E80>
# 10
# 10  -- 表明是可以通过实例来访问到类的属性值

Person.shilifangfa()
# 执行结果：
# <class '__main__.Person'>
# 10
# TypeError: shilifangfa() missing 1 required positional argument: 'self' -- 在访问实例属性值时是访问不到的，因为属性值存储在实例中，



p.leifangfa()
# 执行结果：
# <class '__main__.Person'>
# 10
# AttributeError: type object 'Person' has no attribute 'num'  -- 类方法只能访问到类属性里面的值，不能访问到实例属性的值


Person.leifangfa()
# 执行结果：
# <class '__main__.Person'>
# 10
# AttributeError: type object 'Person' has no attribute 'num'  -- 类方法只能访问到类属性里面的值，不能访问到实例属性的值


Person.jingtailfangfa()   # 10


