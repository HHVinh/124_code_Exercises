def thay_Duoi_Chuoi(s):
    if s[len(s)-3:] == 'ing':   # Hoặc dùng s[::-3] hoặc s[-3:]
        s = s[:-3] + 'ly'
    else:
        s += 'ing'
    return s

s = input('Nhập chuỗi bất kì: ')

print(thay_Duoi_Chuoi(s))

