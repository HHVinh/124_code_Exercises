#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())
    
    #Su dung cau truc re nhanh xu ly truong hop n < 0
    if n<0:
        print("Vui long nhap so tu nhien!")
    else:
        ketQua = 1
        #Su dung vong lap for duyet cac so tu 1 toi n
        for i in range(1, n+1):
            ketQua *= i 
        print(ketQua)
        
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")