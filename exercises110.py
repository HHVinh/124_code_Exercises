def kt_tap_con(setX, setY):
   return setY <= setX

#Nhap set tu ban phim
setX = set(input('Nhập dữ liệu set1: ').split())
setY = set(input('Nhập dữ liệu set2: ').split())

#Goi ham va truyen cac tham so can thiet
kiemTra = kt_tap_con(setX, setY)

print(kiemTra)
