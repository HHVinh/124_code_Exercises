try:
    a = int(input('Nhập số nguyên lớn hơn 0: '))
    if a <1:
        print('Nhập số nguyên lớn hơn 0')
    else:
        maAscii = 65
        for i in range(a):
            khoangTrangDauDong = ' '*((a-i)*2-1)
            print(khoangTrangDauDong,end=' ')
            for j in range(2*i+1):
                chuCai = chr(maAscii)
                print(chuCai,end=' ')
                maAscii +=1
                if maAscii > 90:
                    maAscii = 65
            print()
except:
    print('Dữ liệu đầu vào không đúng')