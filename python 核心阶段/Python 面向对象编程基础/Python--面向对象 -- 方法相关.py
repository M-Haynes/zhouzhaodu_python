#  方法的概念 =================================================
#   描述一个目标的行文 -- 比如描述一个人怎么吃，怎么喝，怎么玩
#   和函数非常相似 -- 都封装了一系列的行为动作、都可以被调用之后，执行一系列行为动作、
#       最主要的区别： 调用的方式不同

# 函数：
def eat():
    print(1)
    print(2)
    print(3)

# 调用函数
eat()
# 返回结果：
# 1
# 2
# 3



# 方法：
class Person:
    def eat2(self):
        print(4)
        print(5)
        print(6)

p = Person()
p.eat2()  # 这里的调用：目标.方法
# 返回结果：
# 4
# 5
# 6


# 方法的划分： --- 实例方法、 类方法、 静态方法 =================================
# 注意：
#   1，划分的依据是： 方法的第一个参数必须要接收的数据类型
#   2，不管是哪一种类型的方法，都是存储在类中，没有存储在实例当中
#   3，不同的类方法， 调用的方式不同
#           但是，不管怎么调用，把握一个原则：
#               不管是自己传递，还是结束期帮我们处理，最终要保证不同类型的方法，第一个参数接收到的数据，是他们想要的类型

# --- 实例方法：
#   默认的第一个参数需要接收到一个实例

# --- 类方法：
#   默认第一个单数需要接收到一个类

# --- 静态方法：
#   静静的看着前面两个装逼，第一个参数啥也不默认接收


# 实例 -- 判断划分依据
class Person:
    def eat2(self):
        print("这是一个实例方法",self)

    @classmethod
    def leifangfa(cls):
        print("这是一个类方法",cls)

    @staticmethod
    def jingtaifangfa():
        print("这是一个静态方法")

p = Person()  # 这是一个实例方法 <__main__.Person object at 0x0000028EE2F6BE50>
print(p.eat2())  # None -- 这里None的原因是： eat2函数中，并没有返回值
p.eat2()  # 这是一个实例方法 <__main__.Person object at 0x000002E406B8BEB0>
Person.eat2(123)  # 这里是直接调用了类里面的实例函数
Person.leifangfa()  # 这是一个类方法 <class '__main__.Person'>

Person.jingtaifangfa()  # 这是一个静态方法

# 都存贮在类对象里面
print(p.__dict__)  # {}
print(Person.__dict__)
# 返回值：
# {'__module__': '__main__',
# 'eat2': <function Person.eat2 at 0x0000029B934C83A0>,
# 'leifangfa': <classmethod object at 0x0000029B9689BFA0>,
# 'jingtaifangfa': <staticmethod object at 0x0000029B9689BF70>,
# '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# '__doc__': None}


# --- 方法使用 =================================================================
# 1,语法
# 2,不同类型的方法的规则
# 3,不同类型方法的调用
# 根据不同的问题，自己决定，设计怎样的方法来解决问题
