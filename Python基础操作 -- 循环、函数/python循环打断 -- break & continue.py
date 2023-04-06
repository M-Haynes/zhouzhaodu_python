# 循环打断，对else的影响
    # 如果循环正常执行完毕，则会执行else部分
    # 如果中途是因为打断而退出循环，则不会执行else部分

# break 打断本次循环，跳出整个循环，多层循环的情况指调出一个循环
# continue 结束本次循环，继续执行下次循环

for i in range(1,10):
    if i == 6:
        break
    print(i)

    # 这里只会打印到5

for i in range(1,10):
    if i == 6:
        continue
    print(i)

    # 这里除了6不会打印，其他数字都会打印

