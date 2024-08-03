try:
    a = int(input('Nhập số nguyên từ 1 đến 9: '))
    if a <1 or a >9:
        print('Nhập lại')
    else:
        batDau = 0
        for i in range(a):
            khoangTrang = ' '*((a - i)*2-1)
            print(khoangTrang,end=' ')
            for j in range(2*i+1):
                print(batDau,end=' ')
                batDau += 1
                if batDau >9:
                    batDau = 0
            print()
except:
    print('Dữ liệu không hợp lệ')
