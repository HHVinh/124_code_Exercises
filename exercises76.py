def trung_Binh(s):
        tong = sum(s)
        dem = len(s)
        trungBinh = tong/dem
        return trungBinh
 
s = input('Nhập số bất kì: ').split()

if len(s) == 0:
        print('Danh sách rỗng')
else: 
    try:
        dsCacSo = list(map(float,s))
        trungBinh = trung_Binh(dsCacSo)

        print(trungBinh)
    except:
        print('Dữ liệu đầu vào không hợp lệ')