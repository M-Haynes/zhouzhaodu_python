#   经典类 -- 没有继承（object）
#   新式类 -- 继承（object）
#   Python2.x版本定义一个类时，默认不继承（object）
#   Python3.x版本定义一个类时，默认继承（object）

class Person:
    pass

print(Person.__bases__)
# (<class 'object'>,)
