def xoa_Khoang_Trang(s):
    if len(s) == 0:
        return 'Hãy nhập ít nhất một kí tự'
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ',' ')
    return s

s = input('Nhập một chuỗi bất kì: ')
print(xoa_Khoang_Trang(s))