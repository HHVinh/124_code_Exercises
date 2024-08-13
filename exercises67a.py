def khoang_Trang_Thua(s):
    tachChu = s.split()
    noiChu = ' '.join(tachChu)
    return noiChu

def hien_Thi_Cau(s):
    tachCau = s.split('.')
    for i in tachCau:
        i = khoang_Trang_Thua(i)
        print(i.title())

s = input('Nhập các câu bất kì: ')
hien_Thi_Cau(s)
