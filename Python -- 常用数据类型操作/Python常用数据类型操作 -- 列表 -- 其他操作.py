# Sorted(iterable, key = None, reverse = False)
#   可以对所有可迭代对象进行排序
#   参数：
#       iterable -- 可迭代对象
#       key -- 排序关键字， 值为一个函数，此函数只有一个参数且返回一个值
#       reverse -- 控制升序降序，默认为False -- 升序
#   返回值： 一个已经排序号的列表 -- 列表类型
import random

s = "akcdnamasdnasbd"
res = sorted(s)
print(res)  # ['a', 'a', 'a', 'a', 'b', 'c', 'd', 'd', 'd', 'k', 'm', 'n', 'n', 's', 's']

res = sorted(s, key=lambda x: x.lower())
print(res)  # ['a', 'a', 'a', 'a', 'b', 'c', 'd', 'd', 'd', 'k','m', 'n', 'n','s','s']

print("#"*100)
res = sorted(s, key=lambda x: x.upper())
print(res)  # ['a', 'a', 'a', 'a', 'b', 'c', 'd', 'd', 'd', 'k', 'm', 'n', 'n', 's', 's']
print("$"*100)
res = sorted(s, key=lambda x: x.isdigit())
print(res)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("%"*100)
res = sorted(s, key=lambda x: x.isalpha())
print(res)  # ['a', 'k', 'c', 'd', 'n', 'a', 'm', 'a', 's', 'd', 'n', 'a', 's', 'b', 'd']

res = sorted(s, reverse = True)
print(res) # ['s', 's', 'n', 'n', 'm', 'k', 'd', 'd', 'd', 'c', 'b', 'a', 'a', 'a', 'a']


# list.sort( key = None, reverse = False)  -- 只能操作列表
#   参数：
#       key -- 排序关键字， 值为一个函数，此函数只有一个参数且返回一个值用来进行比较
#       reverse -- 控制升序排序，默认为False
#   注意： 返回的是经过修改的原数据

l = [1, 2, 4, 5, 9, 3, 45, 12]
res = l.sort(reverse= True)  # 注意： 这里res 是没有值的
print(res,l)  # None [45, 12, 9, 5, 4, 3, 2, 1]


# --------------------------乱序 和 反转--------------------------------------
# 乱序
#   可以随机打乱一个列表
#       导入random模块 -- import random
#           random.shuffle(list)

k = [1, 2, 4, 5, 9, 3, 45, 12]
ress = random.shuffle(k)
print(ress, k)  # None [2, 1, 9, 12, 4, 5, 45, 3]


# 反转
#   l.reverse()
k = [1, 2, 4, 5, 9, 3, 45, 12]
ress = k.reverse()
print(ress, k)  # None [12, 45, 3, 9, 5, 4, 2, 1]



# 切片反转
#       l[::-1]  # 不改变原始数据本身

k = [1, 2, 4, 5, 9, 3, 45, 12]
ress = k[:: -1]
print(ress, k)  # [12, 45, 3, 9, 5, 4, 2, 1] [1, 2, 4, 5, 9, 3, 45, 12]

