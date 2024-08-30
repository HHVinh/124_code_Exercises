def tao_Dict(gTri,soLan):
    dictKetQua = dict(zip(gTri,soLan))
    return dictKetQua

def chuyen_List(s):
    s = s.replace(' ','')
    gTri = set(s)
    soLan = [s.count(pTu) for pTu in gTri]
    return gTri, soLan

s = input('Nhập chuỗi dữ liệu bất kì: ')
gTri, soLan = chuyen_List(s)
dictKetQua = tao_Dict(gTri, soLan)

print(dictKetQua)
