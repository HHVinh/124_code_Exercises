def phan_Tu_Duy_Nhat(s):
    cacPhanTu = [ i for i in s if s.count(i) == 1]
    return cacPhanTu

s  = input('Nhập dữ liệu bất kì: ').split()
dsPhanTDuyNhat = phan_Tu_Duy_Nhat(s)

print(*dsPhanTDuyNhat)
