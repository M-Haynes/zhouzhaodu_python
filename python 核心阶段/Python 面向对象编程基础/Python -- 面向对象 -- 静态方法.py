class Person:
    @staticmethod  # 将一个函数转换为一个静态方法 ， 其不需要接收第一个默认参数
    def jintai():
        print("这是一个静态方法")

# 类方法调用
Person.jintai() # 这是一个静态方法

# 实例方法调用
p = Person()
p.jintai()  # 这是一个静态方法

# 函数本身调用
func = Person.jintai
func()  # 这是一个静态方法