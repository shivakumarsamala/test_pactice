for i in range(1,101):
    if (i%5 == 0) & (i%3 == 0):
        print('Bar & Float')
    elif i%5== 0:
        print('Bar')
    elif i%3 == 0:
        print('Float')
    else:
        print(i)