import math

# 正弦函数
# math.sin(x) -- x 参数，所接收的，是一个弧度，角度的话要转化成弧度
# math.cos(x) -- 余弦
# math.tan(x) -- 正切
# math.asin(x) -- 反正弦
# math.acos(x) -- 反余弦
# math.atan(x) -- 反正切
# pi = 180

# 角度转弧度： 角度/180 *pi
# math.degrees()  弧度 -> 角度
# math.radians(x) 角度 -> 弧度


result = math.sin(30)
print(result)

hudu = 30/180 * math.pi
result1 = math.sin(hudu)
print(result1)


