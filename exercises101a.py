def tuple_So_Nguyen(tupleX):
    soNguyen = int(''.join(tupleX))
    return soNguyen

tupleX = tuple(input('Hãy nhập các số bất kì: ').split())
kiemTraDauVao = all(ptu.isdigit() for ptu in tupleX)

if kiemTraDauVao:
    ketqua = tuple_So_Nguyen(tupleX)
    print(ketqua)
else:
    print('Dữ liệu đầu vào không hợp lệ')