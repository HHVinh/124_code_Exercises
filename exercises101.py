def tuple_to_int(tupleX):
   number = int(''.join(tupleX))
   return number

tupleX = tuple(input().split())
kt_dau_vao = all(ptu.isdigit() for ptu in tupleX)

if kt_dau_vao:
   ketQua = tuple_to_int(tupleX)
   print(ketQua)
else:
   print("Dinh dang dau vao khong hop le!")
