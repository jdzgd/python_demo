flag = True
if flag is not False:
    try:
        num = int(input('请输入一个整数: '))
    except ValueError as e:
        print("输入错误！", e)
    if num == 0:
        print('你输入的是0')
        exit()

    num = num % 2
    if num == 0:
        print('你输入的是一个偶数')
    else:
        print('你输入的是一个奇数')
