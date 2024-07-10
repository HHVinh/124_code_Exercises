import math
try:
    with open('bai24Vao.txt', 'r') as fileInp:
        dongDauTien = fileInp.readline().strip()

        if dongDauTien == '1':
            dongThuHai = fileInp.readline()
            a,b = map(float, dongThuHai.split())

            if a == 0:
                if b == 0:
                    thongBao = 'Phương trình có vô số nghiệm'
                else:
                    thongBao = 'Phương trình vô nghiệm'
            else:
                thongBao = 'Phương trình có một nghiệm duy nhất:\nx = {}'.format(-b/a)
        elif dongDauTien == '2':
            dongThuHai = fileInp.readline()
            a,b,c = map(float, dongThuHai.split())
            
            if a == 0:
                if b == 0:
                    if c == 0:
                        thongBao = 'Phương trình có vô số nghiệm'
                    else:
                        thongBao = 'Phương trình vô nghiệm'
                else:
                    thongBao = 'Phương trình có 1 nghiệm duy nhất: \n x = {}'.format(-c/b)
            else:
                # Tính Delta
                delta = a*a - 4*a*c
                # Kiểm tra các trường hợp của delta
                if delta > 0:
                    x1 = float((-b + math.sqrt(delta))/(2*a))
                    x2 = float((-b - math.sqrt(delta))/(2*a))
                    thongBao = 'Phương trình có 2 nghiệm phân biệt là: \nx1 = {} \nx2 ={}'.format(x1,x2)
                elif delta == 0:
                    x = -b/(2*a)
                    thongBao = 'Phương trình có nghiệm kép: \n x1 = x2 = {}'.format(x)
                else:
                    thongBao = 'Phương trình vô nghiệm'
        else:
            thongBao = 'Vui lòng chọn 1 hoặc 2'  

except FileNotFoundError:
    thongBao = 'Không tìm thấy file'
except:
    thongBao = 'Định dạng đầu vào không hợp lệ'    

with open('bai24Ra.txt','w') as fileOut:
    fileOut.write(thongBao)
