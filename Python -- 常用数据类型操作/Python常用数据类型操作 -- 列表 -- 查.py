# 获取单个元素
# items[index]
#       注意负索引 -- -1 表示取值最后一个
num = range(10)
res = num[5]
print(res)  # 5


# 获取元素索引
# index() -- 是从左往右查找
# 可以限定区间进行查找 index(value, start, end, step)

idx = num.index(5)
print(idx)  # 5

num = [1,1,2,3,4,7,6,5,4,43,3,8]
idxx = num.index(3)
print(idxx)  # 4 -- 这里只有会返回第四位的索引


# 获取指定元素的个数
# count()

c = [1,1,2,3,4,53,32,4,5,6,7,3,2,1]
print(c.count(3))  # 2 -- 注意： 这里的33是一个元素，不是3

# 获取多个元素
# 切片
#       items[start: end : step]
x = [1, 1, 2, 3, 4, 7, 6, 5, 4, 43, 3, 8]
y = x[::]  # 这里表示全拷贝
y = x[1:4:2]  # 这里表示从第二个开始,以2为步长
pic = x[::-1] # 表示反转整个列表
