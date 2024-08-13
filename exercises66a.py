def tu_Dai_Nhat(s):
    tuDaiNhat = ''
    dsCacTu = s.split()
    for i in dsCacTu:
        if (len(i)> len(tuDaiNhat)) or (len(i)==len(tuDaiNhat)) and i < tuDaiNhat:
            tuDaiNhat = i
    return tuDaiNhat

s = input('Nhập chuỗi bất kì: ')
print(tu_Dai_Nhat(s))