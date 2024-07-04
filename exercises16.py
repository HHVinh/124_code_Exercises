try:
    print('Nhập tên bạn thứ 1:')
    tenA = input()
    print('Nhập chiều cao bạn thứ 1:')
    chieuCao1 = int(input())

    print('Nhập tên bạn thứ 2:')
    tenB = input()
    print('Nhập chiều cao bạn thứ 1:')
    chieuCao2 = int(input())

    if chieuCao1 > chieuCao2:
        print(tenA + " cao hơn " + tenB)
    elif chieuCao1 < chieuCao2:
        print(tenB + " cao hơn " + tenA)
    else:
        print('Chiều cao 2 bạn bằng nhau')
except:
    print("Dữ liệu chưa phù hợp")