def viet_So(n):
    dem = [i for i in range(n)]
    binhPhuong = [i*i for i in range(n)]
    return dem, binhPhuong

try:
    n = int(input('Nhập số tự nhiên bất kì: '))
    if n < 0:
        print('Hãy nhập số tự nhiên lớn hơn bằng 0')
    else:
        so, binhPhuong = viet_So(n)

        print(*so)
        print(*binhPhuong)
except:
    print('Dữ liệu đầu vào không hợp lệ: ')