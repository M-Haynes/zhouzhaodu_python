# 单一集合操作

# ------------------------------- 可变集合 ---------------------------------
# 增
# set.add(value)  -- value 一定是不可变类型数据
s = {1, 2, 3}
s.add(4)
print(s, type(s))  # {1, 2, 3, 4} <class 'set'>


# 删
# s.remove(element)
#   指定删除set对象中的一个元素
#   如果集合中没有这个元素，则返回一个错误

s = {1,2,3,4,5,6,7,8,9,10,11,12}
res = s.remove(3)
print(res, s)  # None {1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# s.discard(element)
#   指定删集合中的一个元素
#   如果集合中没有这个元素，则不做任何事情
s = {1,2,3,4,5,6,7,8,9,10,11,12}
ress = s.discard(9)
print(ress, s)  # None {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12}

ress = s.discard(199)
print(ress, s)  # None {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12}

# s.pop(element)
#   删除并返回第一个集合中的元素
#   若集合为空，则返回一个错误
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
dis = s.pop()
print(dis, s)  # 1 {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

dis = s.pop()
print(dis, s)  # 2 {3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# s.clear()
#   清空一个集合中的所有元素 -- 这里只是集合元素删除了，集合本身存在

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s.clear()
print(s, type(s))  # set()  <class 'set'>


# ------------------------------- 不可变集合 ---------------------------------
# 不能进行增删改
# 遍历 -- 可变和不可变的方式都是相同的
# for in
s = {1,2,3,4}
for i in s:
    print(i)  # 1 2 3 4

#  通过迭代器进行遍历 -- 迭代器只能使用一次
s = {1,2,3,4}
its = iter(s)
for i in its:
    print(i)  # 1\2\3\4


# ------------------------------- 集合之间的操作 --------------------------------
# 注意 --- 可变集合 于 不可变集合混合运算，返回结果类型以运算符左侧为主
# 交集
# 方式一：
#   intersection(iterable)
#       iteralbe -- 可迭代对象（注意 - 内部一定是可哈希的值） -- 字符串（只判定字符串中的非数字），元组， 列表， 字典（判定key），集合
#   注意： 不改变原来集合
s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}
res = s1.intersection(s2)
print(res, type(res))  # {2, 3} <class 'set'>
print(res, s1, s2)  #  {2, 3}, {1, 2, 3, 4, 5, 45}, {2, 3, 6, 7, 8}
ress = s1.intersection([1,2])
print(ress, type(ress))  # {1, 2} <class 'set'>

# 方式二:
#   逻辑与 ’&‘ -- 只能判断都是集合的数据，不改变原集合
s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}
res = s1 & s2
print(res, type(res))  # {2, 3} <class'set'>
print(res, s1, s2)  #  {2, 3}, {1, 2, 3, 4, 5, 45}, {2, 3, 6, 7, 8}

# 方式三：
# intersection_update(..)
#   交集计算完毕后，会再次复制给原对象
#      会更改原对象 -- 所以只适用于可变集合
s1 = {1, 2, 3, 45, 4, 5}
s2 = frozenset({2, 3, 6, 7, 8})

result = s1.intersection_update(s2)
print(result, s1)  # None {2, 3}  -- 这里s2集合已经被改变
print(type(s2))  # <class 'frozenset'> -- 这里s2的集合类型已经改变

# 对比
# wrong_result = s2.intersection_update(s1)  # 这里会报错-- 因为s2 是不可变集合


# 并集
# union()
#   返回并集，不会改变原本集合
s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}

res = s1.union(s2)
print(res, s1)  # {1, 2, 3, 4, 5, 6, 7, 8, 45}, {1, 2, 3, 4, 5, 45}

# 逻辑 或 ‘|’
s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}
s3 = frozenset([1,2,3,4,5,87])
res = s1 | s2
print(res, s1)  # {1, 2, 3, 4, 5, 6, 7, 8, 45} {1, 2, 3, 4, 5, 45}
print(type(res))  # <class 'set'> -- 这里res 是按照s1 的类型

ress = s3 | s1
print(ress, s3)  # frozenset({1, 2, 3, 4, 5, 45, 87}), frozenset({1, 2, 3, 4, 5, 87}) -- 这里 ress 的类型跟随了s3

# update()
#   会更新原本的集合
s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}

res =s1.update(s2)
print(res, s1)  # None {1, 2, 3, 4, 5, 6, 7, 8, 45}  -- 这里s1 被改变了


# 差集
# difference()
# 算术运算符 减 ‘-’
# difference_update()  -- 改变原来的集合

s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}

res = s1.difference(s2)
print(res, s1)  # {1, 45, 4, 5} {1, 2, 3, 4, 5, 45}

res2 = s1 - s2
print(res2, s1)  # {1, 45, 4, 5} {1, 2, 3, 4, 5, 45}

res3 = s1.difference_update(s2)
print(res3, s1)  # None {1, 4, 5, 45} -- 这里s1 被改变了


# 集合的判定
# isdisjoint()  --- 两个集合不相交
s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}
print(s1.isdisjoint(s2)) # False

# issuperset() --- 一个集合包含另外一个集合
s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}
print(s1.issuperset(s2)) # False


# issubset() --- 一个集合包含于另一个集合
s1 = {1, 2, 3, 45, 4, 5}
s2 = {2, 3, 6, 7, 8}
print(s2.issubset(s1))  # False


