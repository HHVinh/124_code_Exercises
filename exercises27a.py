while True:
    try:
        a,b = map(int,input('Nhập số nguyên a và b: ').split())
        break
    except:
        print('Dữ liệu đầu vào không hợp lệ')

if a > b:
    print('Nhập lại, số a phải nhỏ hơn số b!')
else:
    ketQua = 0
    i = a
    while i <= b:
        ketQua += i
        i +=1
    print(f'Kết quả tính tồng của các số từ {a} đến {b} là {ketQua}')