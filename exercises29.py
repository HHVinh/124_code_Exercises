a = int(input('Nhập số nguyên thứ 1:'))
b = int(input('Nhập số nguyên thứ 2:'))

if a > b:
    thongBao = 'Số thứ 1 phải nhỏ hơn số thứ 2'
else:
    soLuong = 0
    for i in range(a, b + 1):
        if i % 5 == 0:
            print(i)
            soLuong += 1
        if soLuong == 10:
            thongBao = 'Đã in đủ 10 số chia hết cho 5'
            break
    else:
        if soLuong == 0:
            thongBao = 'Không có số nào chia hết cho 5'
        else:
            thongBao = f'Đã in {soLuong} số chia hết cho 5'

print(thongBao)
