# 增加元素

#   append() -- 在列表的最后
#   语法：l.append(object) , object -- 添加的元素
#   注意： 会直接修改原列表

num = [1,2,3]
num.append(4)  # [1, 2, 3, 4]
print(num)


#   insert() -- 指定索引前面
#   语法：l.insert(index, object)
#   参数：index -- 索引， object -- 想要添加的元素
#   注意： 会直接修改原数组
num = [1, 2, 3, 4, 5]
num.insert(0, 8)  # [8, 1, 2, 3, 4, 5]
print(num)


#   extend() -- 往列表中，扩展另外一个可迭代序列
#   语法：l.extend(iterable)
#   参数：iterable -- 可迭代序列 -- 元祖、字符串、列表
#   注意：会直接修改原数组
#        和append之间的区别： extend 可以算是两个集合的拼接，  append 是把一个元素，追加到一个集合里
num = [1, 2, 3, 4, 5]
nums = ["1","a"]
num.extend(nums)  # [1, 2, 3, 4, 5, '1', 'a']
print(num)


# 乘法运算
numss = [1,3]
res = numss*2  # [1, 3, 1, 3]
print(res)


# 加法运算
#   和extend的区别 --  [] + []  只能列表类型和列表类型相加
n1 = [1, 2, 4]
n2 = ['a', 'v']
n3 = n2 + n1  # ['a', 'v', 1, 2, 4]
print(n3)

