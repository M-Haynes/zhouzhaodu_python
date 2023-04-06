# python 输入

# input功能 表示 会将用户输入的内容当做“字符串”，传递给接收的变量
content = input("请输入:")
print(type(content))
print(content)


# eval函数：会将用户输入的内容当做“代码”进行处理
con = input("请输入：")
res = eval(con)  # 将输入的值作为代码处理，和上面相比（输入abc，这里会出现错误，但是1+1 不会）
print(res)




