#Khoi lenh co the phat sinh loi
try:
   #Nhap hai so tu ban phim
   #Ep kieu du lieu sang so nguyen
   a = int(input())
   b = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop a>b
   if a>b:
       print("So thu nhat lon hon so thu hai!")
   else:   
       #Khoi tao gia tri cho bien tong
       tong = 0
       #Khoi tao gia tri cho bien chay i
       i = a
       #Su dung vong lap while voi dieu kien i <= b
       while i <= b:
           #Cong don cac gia tri i de tinh tong
           tong += i
           #Tang gia tri cua bien chay len 1
           i += 1
       print(tong)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")
