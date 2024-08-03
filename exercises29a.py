try:
    a = int(input('Nhập số thứ nhất: '))
    b = int(input('Nhập số thứ hai: '))
    if a > b:
            print('Số thứ nhất phải nhỏ hơn số thứ hai')
    else:
        dem = 0
        for i in range(a, b+1):
            if i % 5 == 0:
                dem +=1
                if dem > 10:
                    print("\n Đã in đủ 10 số rồi")
                    break
                print(i,end=' ')
        else:
            if dem == 0:
                print('Không có số chia hết cho 5')
            else:
                print('\n Đã in hết các số chia hết cho 5')
except:
    print('Dữ liệu đầu vào không hợp lệ')                 

