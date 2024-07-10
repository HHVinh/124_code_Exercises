#Khoi lenh co the phat sinh loi
try:
   #Nhap hai so tu ban phim
   #Ep kieu du lieu sang so nguyen
   print('Nhập số nguyên thứ nhất:')
   a = int(input())
   print('Nhập số nguyên thứ hai:')
   b = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop a>b
   if a>b:
       tong = 0
       for i in range(b, a+1):
            tong = tong + i
       print('Tổng = {}'.format(tong))
       
   else:   
       tong = 0
       #Su dung vong lap for voi a <= i <= b
       for i in range(a, b+1):
           #Cong don cac gia tri i de tinh tong
           tong += i # Viết tắt của tong = tong + i
       print('Tổng = {}'.format(tong))
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")
