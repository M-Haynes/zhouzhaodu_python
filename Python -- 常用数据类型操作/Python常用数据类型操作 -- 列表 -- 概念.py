# 概念
#   有序的可变的元素集合

# 列表推导式
#   从一个list 推导出另外一个list
#   方式：
#       映射解析 -- 一对一变更
#       过滤 -- 从多到少
#   语法：
#       [表达式 for 变量 in 列表]
#       [表达式  for 变量 in 列表 if 条件]


nums = [1, 2, 3, 4, 5]

# 原始方式
resultlist = []
for num in nums:
    resultnum = num ** 2
    resultlist.append(resultnum)
print(resultlist)  # [1, 4, 9, 16, 25]


# 列表推导式
resultlist = [num**2 for num in nums]
print(resultlist)  # [1, 4, 9, 16, 25]

# 由少到多
resultlist = [num**2 for num in nums for num2 in nums]
print(resultlist)  # [1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 9, 9, 9, 9, 9, 16, 16, 16, 16, 16, 25, 25, 25, 25, 25]

resultlist = [num**2 for num in nums if num % 2 != 0]
print(resultlist)  # [1, 9, 25]