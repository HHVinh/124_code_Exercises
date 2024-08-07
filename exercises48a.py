def tong_So_Chan(n):
    soChan = 0
    while n > 0: 
        if (n % 10) % 2 == 0:
            soChan += n % 10
        n //= 10
    return soChan
def tong_So_Le(n):
    soLe = 0
    while n > 0:
        if (n % 10) % 2 != 0:
            soLe += n % 10
        n //= 10
    return soLe
def tinh_Nhan(soChan,soLe):
    return soChan * soLe
try:
    n = int(input('Nhập số tự nhiên cần tính: '))
    if n <= 0:
        print('Nhập số nguyên lớn hơn 0')
    else:
        soChan = tong_So_Chan(n)
        soLe = tong_So_Le(n)
        print(f'Kết quả của tính là: {tinh_Nhan(soChan,soLe)}')
except:
    print('Dữ liệu đầu vào không hợp lệ')
