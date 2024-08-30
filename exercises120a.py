def tao_Dict(s):
    dictKetQua = {}
    for kyTu in s:
        if kyTu in dictKetQua:
            dictKetQua[kyTu] +=1
        else:
            dictKetQua[kyTu] = 1
    return dictKetQua

s = input('Nhập chuỗi dữ liệu bất kì: ')
dictKetQua = tao_Dict(s)
print(dictKetQua)