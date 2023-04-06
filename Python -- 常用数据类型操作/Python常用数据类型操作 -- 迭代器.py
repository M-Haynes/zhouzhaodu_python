# ------------------------------- 迭代器 -------------------------------
# 迭代：
#   是访问集合元素的一种方式， 按照某种顺序逐个访问集合中的每一项

# 可迭代对象
#   能够被迭代的对象，称为可迭代对象
#   判定依据: 能作用于 for in
#   判定方法：
#           import colllections
#           isintance(obj,collections.Iterable)

# 迭代器：
#   是可以记录遍历位置的对象
#   从第一个元素开始，往后通过next()函数，进行遍历
#   只能往后，不能往前
#   判定依据： 能作用于 next() 函数
#   判定方法：
#       import collections
#       isintance(obj,collections.Iterator)
#   注意:
#       迭代器也是迭代对象，所以也可以作用于 for in
#       迭代对象不一定是迭代器，iterable -- 表示有某种能力，iterator -- 表示有这个器具


# 例子：
num1 = "abc"
num2 = [1,2,3,4,5,6,7,8,9]
num3 = True

for num in num1:
    print(num)

import collections
res = isinstance(num1, collections.Iterable)  # True
print(res)

ress = isinstance(num2, collections.Iterable)  # True
print(ress)

resss = isinstance(num3, collections.Iterable)  # False
print(resss)

# 对比ress 的 判断结果
res = isinstance(num2, collections.Iterator)  # False
print(res)


# 生成一个迭代器 iter（）
num2_iter = iter(num2)
res_num2_iter = isinstance(num2_iter, collections.Iterator)  # True
print(res_num2_iter)


# 为什么会生产迭代器
#   1，仅仅在迭代到某个元素是才处理该元素 -- 增加了性能
#       再次之前 -- 元素可以不存在， 在此之后 -- 元素可以被销毁，、
#       特别适用于遍历一个巨大的或无限集合 -- “斐波那契数”（后面一个数是前面两个数之和）
#   2，增加了一个统一的访问集合的接口
#       不同类型的集合，访问的接口是不同的，迭代器可以把所有的可迭代对象，转换成迭代器进行使用
#       iter（iterable） -- iter(str), iter(list), iter(tuple), iter(set), iter(dict)


# 迭代的简单使用
#   使用next（）函数，从迭代器中取出下一个对象，从第一个元素开始
#   可以直接作用于 for in  -- 内部会自动调用迭代对象的next()， 会自动处理迭代完毕的错误

# 注意：
#   如果取出完毕，再继续取出，则会报错 -- stopIteration
#   迭代器一般不能多次迭代

l = [1, 2, 3, 4, 5, 6, 7]
lt = iter(l)

# next() 函数
print(next(lt))  # 1
print(next(lt))  # 2
print(next(lt))  # 3
print(next(lt))  # 4
print(next(lt))  # 5
print(next(lt))  # 6
print(next(lt))  # 7