# --------------------------  私有化属性 ------------------------

#   Python并乜有真正的私有化支持，但是可以使用下划线完成伪私有的效果
#       类属性(方法)和实例属性(方法)遵循相同的原则


# 不同属性 ：  详情 -- 见 私有化属性 -- 不同属性展示.png


# -------------------- 公有属性 --------------------
# X
# 内部访问、子类内部访问、模块内其他位置访问、跨模块访问

class Animal:
    x = 10
    def test(self):
        print(Animal.x)
        print(self.x)


class Dog(Animal):
    def test2(self):
        print(Dog.x)
        print(self.x)
    pass



# 测试代码
a = Animal()
a.test()
# 运行结果： # 表明在类的内部 可以访问到公用属性x
# 10
# 10

d = Dog()
d.test2()
# 运行结果： # 表明在继承类的内部 可以访问到父类的公用属性x
# 10
# 10

a = Animal()
d = Dog()
print(Animal.x)
print(Dog.x)
print(a.x)
print(d.x)
# 运行结果：
# 10
# 10
# 10
# 10


# ----------------------- 受保护属性 ------------------------
# _y
# 类内部访问 -- 可以
# 子类内部访问 -- 可以
# 模块内其他位置访问
#   类访问：父类（警告）, 派生类（警告）,
#   实例访问：父类实例(警告)，派生类实例(警告)
# 跨模块访问
#   import 形式导入
#   from module import * 形式导入
#       有__all__指明对应变量（警告）
#       没有__all__指明对应变量 -- 不可以

class Animal:
    _x = 10
    def test(self):
        print(Animal._x)
        print(self._x)


class Dog(Animal):
    def test2(self):
        print(Dog._x)
        print(self._x)
    pass

# 类和子类都可以访问
print("$"*100)
a = Animal()
a.test()
d = Dog()
d.test2()

# 模块内其他位置访问 -- 警告
print(Animal._x)
print(Dog._x)
print(a._x)
print(d._x)
# 运行结果
# 10
# 10
# 10
# 10


# ----------------------- 私有属性 ------------------------
# __y
# 类内部访问 -- 可以
# 子类内部访问 -- 不可以
# 模块内其他位置访问
#   类访问：父类（不可以）, 派生类（不可以）,
#   实例访问：父类实例(不可以)，派生类实例(不可以)
# 跨模块访问
#   import 形式导入
#   from module import * 形式导入
#       有__all__指明对应变量（警告）
#       没有__all__指明对应变量 -- 不可以

# 实现机制：
#   名字重整 -- 重改__x 为另外一个名称，如 _类名__x
# 目的：
#   防止外界直接访问
#   防止被子类同名称属性覆盖

# 应用场景：
#   数据保护
#   数据过滤

class Animal:
    __x = 10
    def test(self):
        print(Animal.__x)
        print(self.__x)


class Dog(Animal):
    def test2(self):
        print(Dog.__x)
        print(self.__x)
    pass

# 类内部访问 -- 可以
print("%"*100)
a = Animal()
a.test()
# 10
# 10


# 子类访问 -- 失败
d = Dog()
d.test2()
# 结果：AttributeError: type object 'Dog' has no attribute '_Dog__x'

# 模块内其他位置访问 -- 失败
print(Animal.__x)
print(Dog.__x)
print(a.__x)
print(d.__x)

# 注意：
h = Animal()
h.__x = 10
print(h.__dict__)  # {'__x': 10} 这个表示 是在实例中创建了一个私有属性，不是修改原来的类里面的私有属性

# 这里在别的文件中使用import 文件名 是可以访问到__a的值
# 但是在使用from 文件名 import * 时，是不可以访问到的
#   但是这里是可以使用 __all__ = ['__a']来是的这个私有变量可以被调用
__a = 666

