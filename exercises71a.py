def digit_Chart_Symbol(s):
    digit = ''
    chart = ''
    symbol = ''
    for i in s:
        if i.isdigit():
            digit += i
        elif i.islower() or i.isupper():
            chart += i
        else:
            symbol += i
    chuoiKetQua = digit + chart + symbol
    return len(digit), len(chart), len(symbol), chuoiKetQua

s = input('Nhập chuỗi kí tự bất kì: ')

slSo, slChuoi, slKiTu, chuoiKetQua = digit_Chart_Symbol(s)

print(slSo)
print(slChuoi)
print(slKiTu)
print(chuoiKetQua)

