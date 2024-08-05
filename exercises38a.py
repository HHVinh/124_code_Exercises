try:
    a = int(input('Nhập số cần hiện ước: '))
    if a < 1:
        print('Nhập một số nguyên lớn hơn 0')
    else:
        for i in range(1, a + 1):
            if a % i == 0:
                print(i, end=' ')
except ValueError:
    print('Dữ liệu nhập vào chưa hợp lệ')
