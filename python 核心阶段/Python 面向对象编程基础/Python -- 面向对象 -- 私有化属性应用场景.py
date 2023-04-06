class Person:

    # 主要作用：当我们创建好一个 实例对象 之后，会自动的调用这个方法，来初始化这个对象，即给这个对象赋一个初始值
    def __init__(self):
        self.age = 10


p0 = Person()
p0.age = 20


p1 = Person()

p2 = Person()

p3 = Person()

print(p0.age)
print(p1.age)
print(p2.age)
print(p3.age)

# 运行结果： 注意 -- 这里的age是属于各自生成的实例，其中一个实例的改变，不会影响另外一个实例的初始值
# 20
# 10
# 10
# 10


# -------------------------------- 私有化属性 --------------------------------

# 数据保护
class Person:

    # 主要作用：当我们创建好一个 实例对象 之后，会自动的调用这个方法，来初始化这个对象，即给这个对象赋一个初始值
    def __init__(self):
        # 这里age 被私有化，只能类的内部调用，子类和模块的其他地方都不能调用和修改
        self.__age = 10

    # 可以使用类内部的实例，来访问到内的私有属性，从而进行私有属性的修改
    def setAge(self,value):
        self.__age = value

    # 同理 -- 可以使用类内部的实例，来访问类的私有属性，并进行返回输出
    def getAge(self):
        return self.__age


print("&"*100)
p5 = Person()
print(p5.getAge())  # 10
p5.setAge(100)
print(p5.getAge())  # 100


# 数据过滤
class Person:

    # 主要作用：当我们创建好一个 实例对象 之后，会自动的调用这个方法，来初始化这个对象，即给这个对象赋一个初始值
    def __init__(self):
        # 这里age 被私有化，只能类的内部调用，子类和模块的其他地方都不能调用和修改
        self.__age = 10

    # 可以使用类内部的实例，来访问到内的私有属性，从而进行私有属性的修改
    def setAge(self,value):
        if isinstance(value, int) and  0 < value < 100:
            self.__age = value
        
    # 同理 -- 可以使用类内部的实例，来访问类的私有属性，并进行返回输出
    def getAge(self):
        return self.__age


print("&"*100)
p5 = Person()
print(p5.getAge())  # 10
p5.setAge(100)
print(p5.getAge())  # 10  -- 表明这里进行了数据过滤


