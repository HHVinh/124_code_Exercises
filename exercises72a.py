def dem_Tu(s):
    dem = 0
    tachTu = s.split()
    for i in tachTu:
        chu = False
        so = False
        for a in i:
            if a.isdigit():
                so = True
            if a.isalpha():
                chu = True
        if chu == True and so == True:
            dem += 1
    return dem

s = input('Nhập chuỗi kí tự bất kì: ')
print(dem_Tu(s))

        
