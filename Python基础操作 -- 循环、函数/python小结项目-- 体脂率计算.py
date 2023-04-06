# 功能分析
#   1 输入：升高、体重、年龄、性别
#   2 处理数据：（1）计算体质率，（2）判定体脂率，是否在正常的标准范围内
#   3 输出： 告诉用户，是否正常

#   计算体脂率公式： BMI = 体重（kg）/ (身高*身高)（米）
                # 体脂率 = 1.2*BMI+0.23*年龄 -5.4-10.8*性别（男：1 女：0）
                # 正常成年人的体质率分别是在男性15%~18% 和女性25%~28%


# 输入
personHeight = input("请输入身高（m）：")
personWeight = input("请输入体重（kg：")
personAge = input("请输入年龄：")
personSex = input("请输入性别(男：1 女：0)：")

# 装换类型
personHeight = float(personHeight)
personWeight = float(personWeight)
personAge = float(personAge)
personSex = float(personSex)

# 计算公式
BMI = personWeight / (personHeight * personHeight)
TZL = 1.2 * BMI + 0.23 * personAge - 5.4 - 10.8 * personSex

# 判断体脂率
# 正常成年人的体质率分别是在男性15%~18% 和女性25%~28%

# TZL MIN MAX
minNum = 0.15 + 0.10 * (1 - personSex)
maxNum = 0.18 + 0.10 * (1 + personSex)

result = minNum < TZL < maxNum

# 输出
print("你的体脂率，是否符合标准")

