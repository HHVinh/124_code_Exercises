giaTri = input() #Nhap gia tri tu ban phim

try: #Khoi lenh co the phat sinh loi 
    soThapPhan = int(giaTri) #Ep kieu giaTri sang so nguyen
#Xuat cau voi dinh dang theo yeu cau de bai
# %d dong vai tro giu cho cho 1 gia tri so thap phan
# %o dong vai tro giu cho cho 1 gia tri so bat phan
    print('So thap phan %d trong he bat phan la %o' % (soThapPhan, soThapPhan))

except: #Khoi lenh duoc thuc thi khi loi xay ra
    print("Dinh dang dau vao khong hop le!") #In thong bao