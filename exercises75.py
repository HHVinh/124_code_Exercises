def hien_Thi_Chuoi(s):
    for viTri, giaTri in enumerate(s): #enumerate(chuỗi,start mặc định = 0)
        print(viTri, giaTri)

s = input('Nhập dữ liệu bất kì: ').split()

hien_Thi_Chuoi(s)


