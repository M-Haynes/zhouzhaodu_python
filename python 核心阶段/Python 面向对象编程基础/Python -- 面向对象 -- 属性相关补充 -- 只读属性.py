#  概念：
#   一个属性(一般值实例属性)，只能读取，不能写入
# 应用场景：
#   有些属性，只限制在内部根据不同场景进行修改，而对外界来说，不能修改，只能读取
#   比如：电脑类网速属性，网络状态属性

# ---------------------------------- 方案一：  --------------------------------
#   方案 ：
#       全部隐藏 -- 私有化 -- 既不能读，也不能写
#       部分公开 -- 公开读的操作
#           优化：@property -- 将一些 “属性的操作方法（删改查）”关联到某一个属性中

#   具体实现：
#       私有化 -- 通过"属性前置双下划线”实现

class Person:
    def __init__(self):
        self.__age = 18

    # 提供一个供外界访问到类内部私有属性的实例方法
    def getAge(self):
        return self.__age

p1 = Person()
print(p1.getAge())  # 18


class Person:
    def __init__(self):
        self.__age = 18

    # 主要作用就是：可以以使用属性的 读取的 方式，来使用这个方法
    @property
    def getAge(self):
        return self.__age

p1 = Person()
print(p1.getAge)  # 18  -- 注意： 这里对比上面，这里没有（），这里是以读取属性的方式使用这个方法


# --------------------------------
# @property：
#   经典类 -- 没有继承（object）
#   新式类 -- 继承（object）
#   Python2.x版本定义一个类时，默认不继承（object）
#   Python3.x版本定义一个类时，默认继承（object）

# 第一种方式
class Person(object):

    def __init__(self):
        self.__age = 10

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    # 这里使用property的方法，是的上面的操作方法和属性关联起来
    age = property(get_age, set_age)  # 这里没有加（）表示不是调用，而是方法本身

p = Person()
print(p.age)  # 10

p.age = 18
print(p.age)  # 18
print(p.__dict__)  # {'_Person__age': 18} 表示是对类的私有属性进行操作


# 第二种方式： -- 使用装饰器
class Person(object):

    def __init__(self):
        self.__age = 10

    @property
    def get_age(self):
        print("______ get")
        return self.__age

    @get_age.setter  # 这里要注意不是@property,因为上面已经@了
    def set_age(self, value):
        print("_____ set")
        self.__age = value

p = Person()

print(p.get_age)  # 10

p.set_age = 18
print(p.set_age)

# 运行结果：
# ______ get
# 10

# _____ set
# ______ get
# 18
# 注意这里每次都调用了类里面的get和set方法


# ---------------------------------- 方案二：  --------------------------------
class Person(object):

    # 当我们通过 "实例.属性 = 值"， 给一个实例增加一个属性，或者说，修改一下属性值的时候，都会调用这个方法
    # 在这个方法内部，才会真正的把，这个属性，以及对应的数据，给存储到__dict__字典里面
    def __setattr__(self, key, value):
        print(key, value)
        # 1,判定，key，是否使我们需要设置的只读属性名称
        if key == "age" and key in self.__dict__.keys():
            print("这个属性时只读属性，不能设置数据")

        #2，如果说不是，只读属性的名称， 真正的给他添加到这个实例里面去
        else:
            # self.key = value -- 这里采用这样的方式会死循环
            self.__dict__[key] = value

p1 = Person()
p1.age = 10
print(p1.age)  # 10

p1.name = "ab"
print(p1.name)  # ab

p1.age = 999
print(p1.__dict__)  # {'age': 10, 'name': 'ab'}




