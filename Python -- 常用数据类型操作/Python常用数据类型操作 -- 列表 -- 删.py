# 删加元素

#   insert() -- 指定索引前面
#   语法：l.insert(index, object)
#   参数：index -- 索引， object -- 想要添加的元素
#   注意： 会直接修改原数组
num = [1, 2, 3, 4, 5]
num.insert(0, 8)  # [8, 1, 2, 3, 4, 5]
print(num)


#   del() -- 可以删除一个指定元素（对象）
#   语法：del 指定元素
#   注意：
#       可以删除整个列表
#       删除一个变量
#       删除某个元素

nums = [1, 2, 3, 4, 5, 6]
del nums[1]
print(nums)

del nums
print(nums)  # NameError: name 'nums' is not defined 因为删除完了

num = 999
del num
print(num)  # 也是删除完了，导致没有这个变量


#   pop() -- 移除并返回列表中指定索引对应元素
#   语法：
#       l.pop(index = -1)
#   参数：
#       index -- 需要被删除返回的元素索引
#       -1 ： 也就是对应列表最后一个元素
#   返回值：
#       被删除的元素
#   注意：
#       会直接修改原数组，注意索引越界

numl = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = nums.pop()
print(res, nums)  # 6 [1, 3, 4, 5]

resul = numl.pop(2)
print(resul, numl)  # 3 [1, 2, 4, 5, 6, 7, 8, 9]


#   remove() -- 移除列表中指定元素
#   语法：
#       l.remove(object)
#   参数：
#       object -- 需要被删除返回的元素索引
#   返回值：
#       None
#   注意：
#       会直接修改原数组
#       如果元素不存在，会报错
#       如果存在多个元素， 则只会删除最左边一个
#       注意循环内删除列表元素带来的坑

numl = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numl.remove(5)
print(result, numl)  # None  [1, 2, 3, 4, 6, 7, 8, 9]

numll = [1, 2, 2, 3, 4, 5, 6, 7]
re = numll.remove(2)
print(re, numll)  # 2  [1, 2, 3, 4, 5, 6, 7]  -- 只会删除最左边的一个元素

