def xoa_Chuoi(s):
    if len(s) == 0:
        return 'Hãy nhập dữ liệu ít nhất 1 kí tự'
    elif len(s) % 2 != 0:
        return s[1::2]
    return s[::2]

try:    
    s = input('Nhập chuỗi dữ liệu: ')
    print(xoa_Chuoi(s))
except:
    print('Dữ liệu đầu vào không hợp lệ')