with open('bai23aVao.txt','w') as fileInp:
    fileInp.write('3 4 5\n')
try:
    with open('bai23aVao.txt','r') as fileInp:
        dongDauTien = fileInp.readline().strip()
        a,b,c = map(float,dongDauTien.split())
    
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
            thongBao = f'Tam giác có 3 cạnh {a} {b} {c} là tam giác {loaiTamGiac}'
        else:
            thongBao = f'{a} {b} {c} không là 3 cạnh của tam giác'
except:
    thongBao = 'Dữ liệu đầu vào không hợp lệ'

with open('bai23aRa.txt','w') as fileOut:
    fileOut.write(thongBao)

    