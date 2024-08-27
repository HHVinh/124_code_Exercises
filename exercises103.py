def them_tuple(tupleX, tupleY, k):
   ketQua = tupleX[:k] + tupleY + tupleX[k:]
   return ketQua

tupleX = tuple(input('Nhập tupleX: ').split())
tupleY = tuple(input('Nhập tupleY: ').split())

try:
   k = int(input('Nhập vị trí chèn Y vào X: '))
   if k < 0 or k > len(tupleX):
       print("Vui long nhap k nguyen duong va nho hon hoac bang so phan tu cua tuple X!")
   else:
       ketQua = them_tuple(tupleX, tupleY, k)
       print(ketQua)
except:
   print("Dinh dang dau vao khong hop le!")
