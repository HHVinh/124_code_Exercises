def trung_Binh_Cong(trungBinh):
    trungBinhCong = sum(trungBinh) / len(trungBinh)
    soNhoHonTB = [i for i in trungBinh if i < trungBinhCong]
    soLonHonTB = [i for i in trungBinh if i >= trungBinhCong]
    return trungBinhCong, soNhoHonTB, soLonHonTB

trungBinh = input('Hãy  nhập dãy số bất kì: ').split()

if len(trungBinh) == 0:
    print('Hãy nhập ít nhất một số bất kì')
else:
    try:
        dsSoTB = list(map(float, trungBinh))
        ketQua1, ketQua2, ketQua3 = trung_Binh_Cong(dsSoTB)

        print('Trung bình dãy số trên là: ',ketQua1)
        print('Các số nhỏ hơn TBC là: ',*ketQua2)
        print('Các số lớn hơn TBC là: ',*ketQua3)
    except:
        print('Dữ liệu đầu vào chưa hợp lệ')
