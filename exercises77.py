def so_Nho_Nhat(s):
    soNhoNhat = s[0]
    for i in s:
        if i < soNhoNhat:
            soNhoNhat = i
    return soNhoNhat

s = input('Nhập dãy số bạn muốn tìm số nhỏ nhất: ').split()
if len(s) ==0:
    print('Hãy nhập ít nhất một số bất kì')
else:
    try:
        dsSo = list(map(float,s))
        ketQua = so_Nho_Nhat(dsSo)
        print(f'Số nhỏ nhất trong dãy số của bạn là: {ketQua}')
    except:
        print('Dữ liệu đầu vào không hợp lệ')