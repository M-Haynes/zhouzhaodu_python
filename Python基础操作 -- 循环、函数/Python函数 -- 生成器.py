# ------------------------------------ 概念 ----------------------------------------------------------------
# 生成器：
#   一个特殊的迭代器（迭代器的抽象层级更高）
#   所以，拥有迭代器的特性：
#       惰性计算数据，节省內存
#       能够记录状态，并通过next()函数，访问下一个状态
#       具备可迭代特性
# 迭代器 概念参考 -- python常用数据类型操作 -- 迭代器

# ------------------------------------ 创建方式  --------------------------------
# 方式一：
#  生成器表达式 -- 把列表推导式的[] 修改成()

# 列表推导式
l = [i for i in range(100) if i%2 == 0]
print(l)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


# 生成器
g = (i for i in range(100) if i%2 == 0)
print(g)  # <generator object <genexpr> at 0x000002CA680AD350> 返回的是一个生成器

# 访问生成器里的元素-- （注意 生成器是能够记录状态的）
# 方式1：
print(next(g))  # 0
print(next(g))  # 2
print(next(g))  # 4
print(next(g))  # 6
print("...")

# 方式2：
print(g.__next__())  # 8
print("$"*100)

# 方式3：
for i in g:
    print(i)  # 对生成器里面的内容进行遍历


# 方式二：
# 生成器函数， 函数中包含 yield语句， 这个函数的执行结果就是“生成器”，里面的代码是不会被执行的，
def te():
    print("XXX")
    yield 1
    print("a")

    yield 2
    print("b")

    yield 3
    print("c")

    yield 4
    print("d")

    yield 5
    print("e")


print(te())  # <generator object te at 0x0000029E374A29E0> 这里是生成了一个生成器，并没有执行里面的代码

# 执行里面的代码内容
g = te()  # 调用这个函数，生成一个生成器
print(g)

print(next(g))
# 返回值：
#   XXX
#   1   --- 注意 这里索引到yield 时 才会停止，同时将yield后面迭代器状态值 1 返回给外界，即yield 表示每次遍历截止的位置

print(next(g))
# 返回值：
# a
# 2

print(next(g))
# 返回值：
# b
# 3


#---------------------------- 访问产生数据的方式  -------------------------------------
# 生成器具备可迭代特性
# next函数 -- 等价于 -- 生产器.__next__()
# for in


# ------------------------------------ send()方法 -----------------------------------
# send方法有一个参数，指定的是上一次被挂起的yield 语句的返回值
# 相比于.__next__() -- 可以额外的给yield语句 传值
# 注意第一次调用 --- t.send(None) -- 第一次调用必须要传None
print("分割线")

def tess():
    res1 = yield 1
    print(res1)

    res2 = yield 2
    print(res2)

    res3 = yield 3
    print(res3)
g = tess()  # 这里调用函数生成了一个生成器


# print(next(g))
print(g.__next__())
# 运行程序结果：
# 分割线
# 1

print(g.__next__())
# 运行程序结果
# None --  这里是执行了 print(res1),
# 2 -- 这里是将yield 的状态值2 返回给 print(g.__next__()),并打印出来

print(g.send("666"))
# 程序运行结果
# 666  -- 这里是使用send函数将666 赋值给res2 并进行打印
# 3 -- 这里是将yield 的状态3 返回给 print(g.__next__()),并打印出来

# print(g.send('444'))  # 这里程序会报错 -- StopIteration


# --------------------------------  关闭生成器 -----------------------------------
# g.close()
# 后续如果继续调佣，会抛出StopIteration异常显示

def tess():
    res1 = yield 1
    print(res1)

    res2 = yield 2
    print(res2)

    res3 = yield 3
    print(res3)

g = tess()
print(g.__next__())
print(g.__next__())
# 关闭生成器
g.close()


#   -------------------------------- 注意事项  --------------------------------
# 如果碰到return -- 会直接终止，抛出StopInteration 异常显示
# 生成器只会遍历一次

print("分割线2")

def tesss():
    res1 = yield 1
    print(res1)

    return 10

    res2 = yield 2
    print(res2)

    res3 = yield 3
    print(res3)

g = tesss()
print(g.__next__())
print(g.__next__())  # 这里程序见到return 会报错，并将10 返回 --StopIteration: 10
