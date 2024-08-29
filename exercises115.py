def dict_So_Chinh_Phuong(n):
    dictKetQua = {i:i*i for i in range(n)}
    return dictKetQua

try:
    n = int(input('Nhập một số nguyên dương bất kì: '))
    if n < 0:
        print('Hãy nhập số dương')
    else:
        dictKetQua = dict_So_Chinh_Phuong(n)
        print(dictKetQua)
except:
    print('Dữ liệu đầu vào không hợp lệ')