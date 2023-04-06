# 实例方法：
#   class Person:
#       def function(self):  # self 仅仅是一个形参名称，表示接收这个实例本身
#           pass

# 标准使用：
#   使用实例调用实例方法：不用手动传，解释器会自动把调用对象本身传递过来
#   注意： 如果实例方法没有接收任何参数，则会报错 -- 一个自动传、 一个不接收

# 其他调用：
#   使用类调用 -- 因为实例方法，也是存贮在 类 空间的__dict__中，
#   间接调用
#   本质就是直接找到函数本身来调节

class Person:
    def eat2(self, food):
        print("在吃饭", self, food)

    def eat3(XXX):
        print(XXX)


p = Person()
print(p)  # <__main__.Person object at 0x0000027E5CAF2FD0> -- 是一个类Person的对象

p.eat2("土豆")  # 在吃饭 <__main__.Person object at 0x0000023B2795AEB0> 土豆

print(Person.eat2)  # <function Person.eat2 at 0x000001C387EE6D30> -- 这里是一个函数，类Person 的

# Person.eat2("土豆")  # TypeError: eat2() missing 1 required positional argument: 'food' -- 这里报出缺少一个参数--实例本身
Person.eat2("123", 123)  # 这里其实 是将实例的方法当做其本质 - 函数 来调用的 -- 在吃饭 123 123

print("#"*100)
func = Person.eat2
func(123,999)  # 在吃饭 123 999

s = Person()
s.eat3()  # <__main__.Person object at 0x00000273CAEC9E20>, 表明这个实例对象的第一个参数不一定要是self，在实例过程中，都会将这个方法传递给第一个参数
