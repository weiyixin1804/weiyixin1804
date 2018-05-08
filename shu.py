while True:
    num=int(input('请输入你的真实体重:'))
    if num>=150:
        print('咦，真壮!')
    elif num<=90:
        print('咦，骗谁哩!')
    else:
        print('不胖不瘦，刚刚好')
