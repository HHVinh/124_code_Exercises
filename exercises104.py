def sap_Xep_Tuple(tupleX):
    ketQua1 = sorted(tupleX, reverse=True)
    ketQua2 = sorted(tupleX, reverse=False)
    return ketQua1, ketQua2

try:
    tupleX = tuple(map(float,input('Nhập các giá trị của tuple cần sắp xếp: ').split()))
    ketQua1, ketQua2 = sap_Xep_Tuple(tupleX)

    print('Tuple đã được sắp xếp giảm dần: ',ketQua1)
    print('Tuple đã được sắp xếp tăng dần: ',ketQua2)

except:
    print('Dữ liệu đầu vào chưa hợp lệ')
