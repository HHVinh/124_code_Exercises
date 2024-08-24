def tim_Gia_Tri(x,giaTri):
    viTri = tuple(vt for vt, gt in enumerate(x) if gt == giaTri)
    return viTri

x = tuple(input('Nhập các giá trị của tuple: ').split())
giaTri = input('Nhập một giá trị bất kì bạn muốn tìm: ')

ketQua = tim_Gia_Tri(x, giaTri)
print(ketQua)