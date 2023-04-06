# if 语法&实例
    # 单分支判断
    # 双分支判断
    # 多分支判断
    # if嵌套
    # 注意

# 单分支判断  if ...
age = 17
if age >= 18:  # 0 表示否，其他值表示真
    print("你已经成年")

print("赶紧回家吃饭")

# 双分支  if ... else ...
if age >= 18:
    print("可以上网")
else:
    print("赶紧回家")

# 多分支判断  elif
score = 90
if 90 <= score <= 100:
    print("优秀")
elif 80 <= score <= 90:
    print("良好")
elif 70 <= score <= 60:
    print("及格")
else:
    print("不及格")

