with open('bai24aVao.txt','w') as fileInp:
    fileInp.write('2\n')
    fileInp.write('-5 7.6 9')
import math
try:
    with open('bai24aVao.txt','r') as fileInp:
        dongDauTien = fileInp.readline().strip()
        
        if dongDauTien == '1':
            a,b = map(float,fileInp.readline().strip().split())
            if a != 0:
                x = -b/a
                thongBao = f'Phương trình có 1 nghiệm duy nhất là: x = {x}'
            else:
                if b ==0:
                    thongBao = 'Phương trình có vô số nghiệm'
                else:
                    thongBao = 'Phương trình vô nghiệm'
        elif dongDauTien == '2':
            a,b,c = map(float,fileInp.readline().strip().split())
            if a == 0:
                if b != 0:
                    x = -c/a
                    thongBao = f'Phương trình có 1 nghiệm duy nhất là: x = {x}'
                else:
                    if c ==0:
                        thongBao = 'Phương trình có vô số nghiệm'
                    else:
                        thongBao = 'Phương trình vô nghiệm'
            else:
                delTa = b*b - 4*a*c
                if delTa > 0:
                    x1 = (-b + math.sqrt(delTa))/(2*a)
                    x2 = (-b - math.sqrt(delTa))/(2*a)
                    thongBao = f'Phương trình có 2 nghiệm phân biệt là: x1 = {x1} và x2 = {x2}'
                elif delTa == 0:
                    x = -b/(2*a)
                    thongBao = f'Phương trình có 1 nghiệm duy nhất là: x = {x}'
                else:
                    thongBao = f'Phương trình vô nghiệm'
        else:
            thongBao = 'Vui lòng chọn 1 hoặc 2'
except FileNotFoundError:
    thongBao = 'Không tìm thấy file'
except:
    thongBao = 'Dữ liệu đầu vào không hợp lệ'

with open('Bai24aRa.txt','w') as fileOut:
    fileOut.write(thongBao)

