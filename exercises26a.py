while True:
    try:
        a = int(input('Nhập số nguyên a: '))
        b = int(input('Nhập số nguyên b: '))
        break
    except:
        print('Dữ liệu đầu vào không hợp lệ. Nhập lại:')
if a > b:
    print('Hãy nhập số a nhỏ hơn số b')
else:
    ketQua = 0
    for i in range(a,b+1):
        ketQua = ketQua + i
    print(f'Tổng các số từ {a} đến {b} là {ketQua}')

