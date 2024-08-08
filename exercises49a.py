def giai_Thua(n):
    if n == 0:
        return 1
    return n * giai_Thua(n - 1)
try:
    n = int(input('Nhập một số tự nhiên bất kì cần tính giai thừa: '))
    if n < 0:
        print('Nhập một số nguyên từ 0 trở lên')
    else:
        ketQua = giai_Thua(n)
        print(f'Giai thừa của {n} = {ketQua}')
except:
    print('Dữ liệu đầu vào không hợp lệ')