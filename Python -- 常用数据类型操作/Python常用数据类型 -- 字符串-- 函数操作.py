# 使用方式
    # 直接使用
    # 对象方法： 对象.方法(参数)

# --------------  字符串 查找计算 ------------------
# len
#   作用：计算字符串字符个数
#   语法：len(name)
#   参数：字符串
#   返回值： 字符串个数 -- 整型
#   注意：转义字符 ”\t“ 只算一个字符， 一个汉字也只算一个字符

name = "abcde"
len_name = len(name)
print(len_name)

name = "我是\n"
len_name2 = len(name)
print(len_name2)


# find()
#   作用：查找子串索引(下标)位置
#   语法：find(sub, start = 0, end = len(str))
#   参数：sub -- 需要检索的字符串
#        start -- 检索的起始位置，可省略，默认为0
#        end -- 检索的结束位置， 可省略，默认为len(str)
#   返回值：找到了 --  指定索引 -- 整型 ， 找不到 -- -1
#           注意： 从左往右进行查找，找到后立即停止

name = "wo shi sz"
num = name.find("sz")   # 对象.方法(参数)
num1 = name.find("s", 4)  # 4表示从第四位开始查找
print(num, num1)


# rfind()
#   功能使用，同find
#   区别：
#       从右往左进行查找

name = "wo shi sz"
num = name.find("s")   # 对象.方法(参数)
num1 = name.rfind("s")  # 表示从右往左进行查找
print(num, num1)


# index
#   作用： 获取子串索引位置
#   语法：index(sub,start = 0, end = len(str))
#   参数：
#       sub: 需要检索的字符串
#       start： 检索的起始位置，可省略，默认是0
#       end： 检索的结束位置，可省略，默认是len(str)
#   返回值：
#       找到了 -> 指定索引，整型
#       没找到 -> 异常, 报错
#       注意：从左到右查找，找到后立即停止

name = "wo shi sz"
num4 = name.index("sz")
print(num4)


# rindex()
#   作用：和index一样
#   区别：从右往左查找
name = "wo shi sz"
num5 = name.rindex("sz")
print(num5)


# count
#   作用：计算某个子字符串的出现个数
#   语法： count(sub, start = 0, end = len(str))
name = "wo shi ni de "
print(name.count("i"))


# -------------------- 字符串函数 转换操作 ---------------------------
# replace()
#   作用：使用给定新字符串，替换原字符串的 旧字符串
#   语法：replace(old, new[, count])
#   参数：
#       old: 需要被替换的旧字符串
#       new：替换后的新字符串
#       count：替换的个数，可省略，表示替换全部
#   返回值：
#       替换后的结果字符串
#   注意：并不会修改原字符串本身
name = "wo shi ni de "
result = name.replace("i","w",1)
print(result)
print(name)


# capitalize()
#   作用：将字符串首字母变为大写
#   参数：无
#   返回值：首字符大写后的新字符串
#   注意：并不会修改原字符串本身
name = "wo shi de"
result3 = name.capitalize()
print(result3)


# title()
#   作用：将字符串 每个单词的 首字符 变为大写
#   语法：title()
#   参数：无
#   返回值：每个单词首字符大写后的新字符串
#   注意：并不会修改原字符串本身

name = "wo shi  ni de"
result5 = name.title()
print(result5)

name = "wo shi ni-ze￥de%da*qda"
result6 = name.title()  # 只要后面不是字符，都默认为是第一位
print(result6)


# lower()
#   作用： 将字符串每个字符都变为小写
name = "wo shi Ni-Ze￥De%Ba*qda"
result7 = name.lower()  # 只要后面不是字符，都默认为是第一位
print(result7)


# upper()
#   作用： 将字符串的 每个字符 都变为 大写

name = "wo shi  ni de"
result5 = name.upper()
print(result5)


# -------------------------  字符串函数  填充压缩 ------------------------
# ljust()
#   作用： 根据指定字符（1个），将原字符串填充够指定长度
#   l：表示原字符串靠左
#   语法：ljust(width, fillchar)
#   参数：
#       width： 指定结果字符串的长度
#       fillchar: 如果原字符串长度 < 指定长度时， 填充过去的字符
#   返回值：填充完毕的字符串
#   注意：
#       不会修改原字符串，填充字符的长度为1， 即fillchar 只能时一个（例如：’x‘， 而不能是”xx“）
#       只有原字符串长度 < 指定结果长度时，才会填充

# rjust()
#   作用：根据指定字符（1个），将原字符串填充够指定长度
#    r：表示原字符串靠右，其他同 ljust 一样

name = "abc"
print(name.ljust(6, "X"))   # abcXXX
print(name.rjust(6, "X"))   # XXXabc


# center()
#   作用：根据指定字符（1个），将原字符串填充够指定长度
#    center： 表示原字符串居中 ， 其他同 ljust一样

name = "abc"
print(name.center(6, "X"))   # XabcXX


# lstrip()
#   作用： 移除所有原字符串指定字符(默认为空白字符)
#   l: 表示仅仅只移除左侧,
#   语法： lstrip(chars)
#   参数：
#       chars -- 需要移除的字符串集 -- 例如"wo" 表示移除左侧的所有w和o
#               表现形式为字符串：“abc” -> "a"|"b"|"c"
#   返回值： 移除完毕的结果字符串
#   注意： 这里\n 也会被压缩掉

name = " wo shi sz "
print("|" + name.lstrip() + "|")  # |wo shi sz |
print("|" + name + "|")  # | wo shi sz |

name1 = "wwwwwwwwwwoooooooo ni shi zs"
print("|" + name1.lstrip("wo") + "|")  # | ni shi zs|
print("|" + name1 + "|")  # |wwwwwwwwwwoooooooo ni shi zs|

# 对比
name2 = "wwwwwniwwwwwoooooooo  shi zs"
print("|" + name2.lstrip("wo") + "|")  # |niwwwwwoooooooo  shi zs|
print("|" + name2 + "|")  # |wwwwwniwwwwwoooooooo  shi zs|


# rstrip()
#   作用： 移除所有原字符串指定字符(默认为空白字符)
#   r: 表示仅仅只移除右侧,
#   语法： lstrip(chars)
#   参数：
#       chars -- 需要移除的字符串集 -- 例如"wo" 表示移除左侧的所有w和o
#               表现形式为字符串：“abc” -> "a"|"b"|"c"
#   返回值： 移除完毕的结果字符串
#   注意： 这里\n 也会被压缩掉

name = " wo shi sz  "
print("|" + name.rstrip() + "|")  # | wo shi sz|
print("|" + name + "|")  # | wo shi sz  |

name1 = " ni shi zs wwwwwwwwwwoooooooo"
print("|" + name1.rstrip("wo") + "|")  # | ni shi zs |
print("|" + name1 + "|")  # | ni shi zs wwwwwwwwwwoooooooo|

# 对比
name2 = " shi zs  wwwwwniwwwwwoooooooo"
print("|" + name2.rstrip("wo") + "|")  # | shi zs  wwwwwni|
print("|" + name2 + "|")  # | shi zs  wwwwwniwwwwwoooooooo|


# ------------------------------  字符串函数 分割拼接操作 ---------------------
# split()
#   作用：
#       将一个大的字符串分割成几个子字符串
#   语法：
#       split(sep, maxsplit)
#   参数：
#       sep 分隔符
#       maxsplit  最大的分割次数，可省略，有多少分割多少
#   返回值：
#       分割后的子字符串，组成的列表
#   注意： 不会修改元字符串本身

info = "sz-18-180-0558-3123112"
result = info.split('-')  # ['sz', '18', '180', '0558', '3123112']
print(result)
result7 = info.split('-', 3)  # ['sz', '18', '180', '0558-3123112']
print(result7)
print(info)


# partition()  # 总的分成三个部分
#   作用：根据指定的分隔符，返回（分隔符左侧内容，分隔符，分隔符右侧内容）
#   语法：
#        partition(sep)
#   参数：
#       sep 分隔符
#   返回值：
#       如果找到分割符
#           （分隔符左侧内容，分隔符，分隔符右侧内容）
#       如果没有找到分割符
#           （原字符，“”，“”） -- tuple 类型
#   注意： 不会修改元字符串本身

info = "sz-18-180-0558-3123112"
result9 = info.partition('-')  # ('sz', '-', '18-180-0558-3123112')
print(result9)
result10 = info.partition("|")  # ('sz-18-180-0558-3123112', '', '')
print(result10)


# rpartition()  # 总的分成三个部分
#   作用：根据指定的分隔符，返回（分隔符左侧内容，分隔符，分隔符右侧内容）
#       r 表示从右侧开始查找分割符
#   语法：
#        rpartition(sep)
#   参数：
#       sep 分隔符
#   返回值：
#       如果找到分割符
#           （分隔符左侧内容，分隔符，分隔符右侧内容）
#       如果没有找到分割符
#           （原字符，“”，“”） -- tuple 类型
#   注意： 不会修改元字符串本身

info = "sz-18-180-0558-3123112"
result11 = info.rpartition('-')  # ('sz-18-180-0558', '-', '3123112')
print(result11)
result12 = info.rpartition("|")  # ('', '', 'sz-18-180-0558-3123112')
print(result12)


# splitlines()
#   作用： 按照换行符(\r, \n) ,将字符串拆成多个元素，保存到列表中
#   语法：
#       splitlines(keepends)
#   参数：
#       keepends --  是否保留换行符，bool类型
#   返回值：
#       被换行符分割的多个字符串，作为元素组成的列表 --list 类型
#   注意： 不会修改原字符串
name = "wo \n shi \r zs"
ll = name.splitlines()  # ['wo ', ' shi ', ' zs']
print(ll)
ln = name.splitlines(True)  # ['wo \n', ' shi \n', ' zs']
print(ln)


# join()
#   作用：根据指定字符串，将给定的可迭代对象，进行拼接，得到凭借后的字符串
#   语法：
#       jion(iterable)
#   参数：
#       iterable -- 可迭代对象，字符串，元组、列表
#   返回值：
#       拼接好的字符串

items = ['wo ', ' shi ', ' zs']
res = "_".join(items)  # wo _ shi _ zs
print(res)


# -----------------------------------  字符串函数操作  判定 -----------------------------
# isalpha()
#   作用：字符串是否是所有的字符是否是字母  # 注意：空格也不是字母
#             不包含该数字，特殊符号，标点符号等等
#             至少有一个字符
#   语法：
#       isalpha()
#   参数：
#       无
#   返回值：
#       是否全是字母
#       bool 类型

name = "sz"
print(name.isalpha())  # True


# isdigit()
#   作用：字符串是否是所有的字符是否是数字  # 注意：空格也不是字母
#             不包含该字母，特殊符号，标点符号等等
#             至少有一个字符
#   语法：
#      isdigit()
#   参数：
#       无
#   返回值：
#       是否全是数字
#       bool 类型

name = "213"
print(name.isdigit())  # True


# isalnum()
#   作用：字符串是否是所有的字符都是数字或者字母  # 注意：空格也不是字母
#             不包含该字母，特殊符号，标点符号等等
#             至少有一个字符
#   语法：
#      isalnum()
#   参数：
#       无
#   返回值：
#       是否全是数字 或者 字母
#       bool 类型

name = "213abc"
print(name.isalnum())  # True


# isspace()
#   作用：字符串中是否所有的字符都是空白符
#             包括空格，缩进，换行等不可转义符
#             至少有一个字符
#   语法：
#      isspace()
#   参数：
#       无
#   返回值：
#       是否全是空白符
#       bool 类型

name = " "
print(name.isspace())  # True

name = ""
print(name.isspace())  # False

name = " A"
print(name.isspace())  # False

name = "\n"
print(name.isspace())  # True


# startswith()
#   作用：
#       判定一个字符串是否以某个前缀开头
#   语法：
#      startswith(prefix, start = 0, end = len(str))
#   参数：
#       prefix -- 需要判定的前缀字符串
#       start,end -- 判定开始和结束的位置
#   返回值：
#       是否以指定前缀开头
#       bool 类型

name = "1820-9-1: 某某报告.xls"
print(name.startswith("1820-9-1"))  # True
print(name.startswith("2018-2"))  # False
print(name.startswith('20', 2))  # True
print(name.startswith('20', 0, 4))  # False -- 因为不是以20开头的


# endswith()
#   作用：
#       判定一个字符串是否以某个后缀结尾
#   语法：
#      endswith(suffix, start = 0, end = len(str))
#   参数：
#       suffix -- 需要判定的后缀字符串
#       start,end -- 判定开始和结束的位置
#   返回值：
#       是否以指定后缀结尾
#       bool 类型

name_s = "1820-9-1: 某某报告.xls"
name_doc = "1820-9-1: 某某报告.doc"
print(name_s.endswith(',xls'))  # True
print(name_doc.endswith(',doc'))  # True


# 补充：
#   in
#       判定一个字符串，是否被另外一个字符串包含
#   not in
#       判定一个字符串，是否不被另外一个字符串包含