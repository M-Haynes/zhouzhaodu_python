# abs（num）
    # 返回数值的绝对值

num = -10
print(abs(num))

# 最大值、最小值  -- max、min
print(max(
    1, 3, 456, 63, 2
))

print(min(
    2, 123, 2, 123, 432, 423
))
# 或
print(min([
    2, 3, 4, 523, 2, 1, 34
      ]))

# 四舍五入
# round(num[, n])
#  , n
#     表示四舍五入的位数
#     可以省略

p = 1.2319431
print(round(p, 2))  # 对第三位1进行四舍五入


# pow(x,y)
#  返回 x 的 y 次幂
#       x**y
print(pow(2, 4))
# 或
print(2**4)




# math模块函数

# 导入模块
import math
# math.函数名(参数)

# 上取整函数
# math.ceil(参数)
p = 3.1
print(math.ceil(p))  # 结果是4


# 下取整
# math.floor(参数)
print(math.floor(p))


# 开平方
# math.sqrt(参数)
print(math.sqrt(17))

# 求对数函数
# math.log(x,base)  # 以base为基础，x的对数
print(math.log(1000, 10))


