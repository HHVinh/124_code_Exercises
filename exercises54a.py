def noi_Chuoi(a,b):
    if len(a) < 5:
        a = a*3
    if len(b) < 5:
        b = b*3
    return a + b

try:
    a = input('Nhập vào chuỗi thứ nhất: ')
    b = input('Nhập vào chuỗi thứ hai: ')
    print(noi_Chuoi(a,b))
except:
    print('Dữ liệu đầu vào không hợp lệ')
