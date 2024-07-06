# Nhập 3 số a, b, c 
print('Nhập lần lượt số a, số b, số c cách nhau bởi 1 khoảng trắng:')
try:
    a, b, c = map(float,input().split()) # Dùng map và float để chuyển thành số thực
    # Quy định a,b,c là 3 cạnh của 1  tam giác
    if a + b > c and a + c >b and b + c > a:
    
        if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
            loaiTamGiac = 'vuông'

        elif a==b and b==c:
            loaiTamGiac = 'đều'

        elif a==b or b==c or a==c:
            loaiTamGiac = 'cân'
        
        elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
            loaiTamGiac = 'tù'
        else:
            loaiTamGiac = 'nhọn'

        print('{} {} {} là 3 cạnh của tam giác {}'.format(a,b,c,loaiTamGiac))

    else:
        print('{}, {}, {} không là 3 cạnh của tam giác'.format(a,b,c))
except:
    print('Dữ liệu chưa phù hợp. Vui lòng nhập lại')
    
