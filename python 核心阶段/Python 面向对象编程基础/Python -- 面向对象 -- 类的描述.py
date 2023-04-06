# ------------------------------ 类的描述 ------------------------
# 目的：
# 方便理清逻辑思路
# 方便多人合作开发时间的沟通
# 方便生成项目文档

class Person:
    """
    关于这个类的描述，类的作用，类的构造函数等等、类属性的描述
    Attributes：
        count = int  代表是人的个数
    """
    count = 1

    def run(self,distence,stop):
        """
        # 这个方法的作用效果
        :param distence:   # 参数的含义，参数的类型int， 是都有默认值
        :param stop:  # 同上
        :return:  # 返回的结果的含义, 返回数据的类型
        """
        print("人在跑")
        return distence/stop

help(Person)


# C:\anaconda\python.exe "D:\code\Python基础\python 核心阶段\Python -- 面向对象 -- 类的描述.py"
# Help on class Person in module __main__:
#
# class Person(builtins.object)
#  |  关于这个类的描述，类的作用，类的构造函数等等、类属性的描述
#  |  Attributes：
#  |      count = int  代表是人的个数
#  |
#  |  Methods defined here:
#  |
#  |  run(self, distence, stop)
#  |      # 这个方法的作用效果
#  |      :param distence:   # 参数的含义，参数的类型int， 是都有默认值
#  |      :param stop:  # 同上
#  |      :return:  # 返回的结果的含义, 返回数据的类型
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  count = 1
#
#
# Process finished with exit code 0


# ------------------------------- 生成项目文档 ------------------------
# 方式一：
#   使用内置模块  pydoc -- 这里使用cmd
# 具体步骤：
#   查看文档描述-- Python3 -m pydoc 模块名称
#   启动本期服务，浏览文档 -- Python3 -m pydoc -p/b 6666  -- b 表示 系统会自动分分配一个端口号
#   生成指定模块的html文档 -- Python3 -m pydoc -w 模块名称

# 方式二：
#   使用第三方模块 Sphinx、 epydoc、doxygen



