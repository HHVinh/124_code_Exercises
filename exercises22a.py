try:
    a,b,c = map(float,input('Nhập 3 độ dài cần kiểm tra: ').split())
    if a+b>c and a+c>b and b+c>a:
        if a*a + b*b == c*c or a*a + c*c == b*b or c*c +b*b == a*a:
            loaiTamGiac = 'vuông'
        elif a==b and b==c:
            loaiTamGiac = 'đều'
        elif a==b or b==c or a==c:
            loaiTamGiac = 'cân'
        elif a*a + b*b < c*c or a*a + c*c < b*b or c*c +b*b < a*a:
            loaiTamGiac = 'tù'
        else:
            loaiTamGiac = 'nhọn'
        print(f'Tam giác có 3 cạnh {a} {b} {c} là tam giác', loaiTamGiac)   
    else:
        print(f'{a} {b} {c} không là 3 cạnh của tam giác')
except:
    print('Dữ liệu đầu vào không hợp lệ')