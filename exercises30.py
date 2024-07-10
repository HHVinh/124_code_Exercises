a = int(input('Nhập 1 số nguyên muốn tạo thành tam giác số: '))
if a < 1 or a > 9:
    thongBao = 'Nhập số nguyên từ 1 đến 9'
else:
    for i in range(1, a+1):
        line = ""
        for j in range(1, i+1):
            line = '{} {}'.format(line,j)
        print(line)

        
    