def tinh_Tong(n):
    tachChuoi = n.split()
    tong_Cac_So = 0
    dem = 0
    for i in tachChuoi:
        if i.isdigit():
            tong_Cac_So += float(i)
            dem += 1
    if dem == 0:
        return 0, 0
    trungBinh = tong_Cac_So/dem
    return tong_Cac_So, trungBinh

n = input('Nhập các kí tự bất kì: ')
tong, trungBinh = tinh_Tong(n)

print(tong)
print(trungBinh)