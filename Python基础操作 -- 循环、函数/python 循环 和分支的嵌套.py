
# 循环内 嵌套if

# 打印1-100之间，所有3的倍数
# 1,先造一个集合
nums = range(1,101)
# 2，遍历集合
for num in nums:
    # 3，在遍历的过程当中，来判定这个集合里面的元素，是否，可以被3 整除
    if num % 3 == 0:
        print(num)


# 循环内嵌套循环
    # 外循环一次
    # 内循环，循环所有

# 例子
for i in range(1, 6):
    for j in range(1, 3):
        print(j)
    