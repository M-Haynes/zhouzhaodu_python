# 反转字符串
    # 源字符串
        # "社会我杜哥，人狠话不多"
    # 反转后
        # “多不话狠人，哥杜我会社”

notice = "社会我杜哥，人狠话不多"
result = ""
result2 = ""
for c in notice:  
    result += c
    result2 = c + result2
print(result,end= "/n")
print(result2, end= "/n")
