def tong_ptu(tupleX):
   ketQua = tuple(sum(ptu) for ptu in tupleX)
   return ketQua

try:
   n = int(input())
   listX = []
   for _ in range(n):
       listPtu = map(int, input().split())
       listX.append(tuple(listPtu))
   tupleX = tuple(listX)
   print(tupleX)
   ketQua = tong_ptu(tupleX)
   print(ketQua)
except:
   print("Dinh dang dau vao khong hop le!")
