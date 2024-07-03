#Mo file voi mode='r' de doc file
with open('bai10Vao.txt', 'r') as fileInp:

#Doc 1 dong du lieu tu file va luu vao bien ten
#Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
    ten = fileInp.readline().rstrip('\n')

#Doc 1 dong du lieu tu file va luu vao bien tuoiHienTai
    tuoiHienTai = int(fileInp.readline().rstrip('\n'))

#Mo file voi mode='w' de ghi file
    with open('bai10Ra.txt', 'w') as fileOut:

#Ghi noi dung vao file theo mau
        fileOut.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))