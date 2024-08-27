def liet_ke_ptu(danhSach):

# Set Constructor
    setPtu = set(danhSach)
    return setPtu

#Nhap danh sach tu ban phim
danhSach = input('Nhập các giá trị bất kì: ').split()

#Goi ham va truyen cac tham so can thiet
setPtu = liet_ke_ptu(danhSach)

#Unpacking arguments
print(*setPtu)