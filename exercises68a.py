def xoa_Dau_Cach(s):
    tachTu = s.split()
    noiCau = ' '.join(tachTu)
    return noiCau

def cau_Dai_Nhat(s):
    tachCau = s.split('.')
    cauDaiNhat = 0
    for i in tachCau:
        i = xoa_Dau_Cach(i)
        if len(i) > cauDaiNhat:
            cauDaiNhat = len(i)

    for i in tachCau:
        i = xoa_Dau_Cach(i)
        print(i.center(cauDaiNhat))

s = input('Nhập dữ liệu bất kì: ')
cau_Dai_Nhat(s)

