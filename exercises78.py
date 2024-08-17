def so_Le(s):
    ketQua = [i for i in s if i % 2 != 0]
    return ketQua

s = input('Nhập dãy số bất kì:  ').split()
if len(s) == 0:
    print('Hãy nhập một số bất kì')
else:
    try:
        dsSo = list(map(int,s))
        ketQua = so_Le(dsSo)
        print(*ketQua, 'là các số lẻ trong chuỗi')
    except:
        print('Dữ liệu đầu vào chưa hợp lệ')