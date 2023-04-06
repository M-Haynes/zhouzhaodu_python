# 字符串的一般操作


# -----------------   字符串拼接  -----------------------
# 方式一 -- 使用 + 号
result = "Wangzha" + "shunzi"
print(result)

# 方式二 -- 使用空格 ，但是不能换行
result1 = "wangzha" "shunzi"
print(result1)

# 方式三 -- % 分号连接
# “a % s”%(a+b)
result3 = "wangzha % s" % "shunzi"
print(result3)

result4 = "s % s" % ("woshi"+"niba")
print(result4)

result5 = "woshi % s, % d" % ("123", 123)
print(result5)

# 方式四 -- 字符串乘法
# ”abc“ * 3 -> "abcabcabc"
print("sz\t" * 10)  # tab空格
print("sx\n" * 3)  # 换行


# --------------------  字符串的切片 -----------------------
# 字符串取某个值

# 字符串的排序从0开始，要取某一个字符 -> name[序号]
# 反向取值则从 -1 开始
name = "abcde"

# 字符串的第三位是：c
print("字符串的第三位是：%s" % name[2])

# 字符串的最后一位是：e
print("字符串的最后一位是：%s" % name[-1])


# 字符串取某段切片
# name[起始, 结束，步长]
    # 取值范围：[起始， 结束) -- 包含起始，不包含结束
    # 起始默认值：0  结束默认值：len(name)  步长默认为：1
    # 获取顺序：步长 > 0  从左边到右边  步长 < 0  从右往左  注意：不能从头部调到尾部，或者尾部跳到头部

    # 反转字符串： 字符串[::-1]

name = "abcdefg"

# 去整个字符串
print(name[::])
print(name[0:len(name):1])

# 反转字符串
print(name[len(name):0: -1])  # 注意 这里取不到第一位a
print(name[::-1])  # 这里能取到第一位a





