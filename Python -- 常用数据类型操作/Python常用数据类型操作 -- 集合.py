# 集合
# 概念：
#   无序的，不可随机访问的，不可重复的元素集合
#   与数学中集合的概念类似，可以对其进行交、并、差、补等逻辑运算
#   集合分为 可变集合 和非可变集合
#       可变集合：set -- 可以进行增、删、改
#       不可变集合：frozenset - 创建好之后，无法增删改

# 注意：
#   1，创建一个空集合，要用set 或者 frozenset 函数 不能用 s= {}
#   2， 集合中的元素，必须是可以哈希的值-- 暂时理解为 不可变类型
#   3，如果集合中的元素值出现重复，则会被合并为1个


# -------------------------------可变集合 ---------------------------------
# 方式一：
s = {1,2,3,4,5}
print(s,type(s))  # {1, 2, 3, 4, 5},  <class 'set'>

# 方式二：
s2 = set("abcs")
print(s2,type(s2))  # {'b', 'c', 'a', 's'} , <class 'set'>

# 注意：使用字典进行集合的创建，则只会根据key来创建
s3 = set({"name":"sx", "age":123})
print(s3,type(s3))  # {'name', 'age'} <class 'set'>

# 方式三：
s4 = set(x for x in range(0,10))
s5 = {c for c in range(0,10)}
print(s4, type(s4))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} <class'set'>
print(s5, type(s5)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} <class 'set'>


# ------------------------------- 不可变集合 ---------------------------------
# 方式一：
fs = frozenset("abc")
fs = frozenset([1,2,3])
fs = frozenset({"name":12, "age":89})
print(fs, type(fs))  # frozenset({'name', 'age'}) <class 'frozenset'>

# 方式二：
fx = frozenset(s for s in range(1,10))
print(fx, type(fx))  # frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9}) <class 'frozenset'>


# 可以使用集合的特性 快速给列表去重
s = [1,2,3,1,32,1,4,51,1,23,5,1]
sign_s = list(set(s))
print(sign_s)  # [32, 1, 2, 3, 4, 5, 51, 23] -- 这里去重了