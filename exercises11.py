#Khoi lenh co the phat sinh loi
try:
#Mo file voi mode='r' de doc file

    with open('bai11Vao.txt', 'r') as fileInp:
    #Doc 1 dong du lieu tu file va luu vao bien ten

        #Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
        ten = fileInp.readline().rstrip('\n')

        #Doc 1 dong du lieu tu file va luu vao bien tuoiHienTai
        tuoiHienTai = int(fileInp.readline())

    #Mo file voi mode='w' de ghi file
    with open('bai11Ra.txt', 'w') as fileOut:

        #Ghi noi dung vao file theo mau
        fileOut.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))

#Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
except FileNotFoundError:
    with open('bai11Ra', 'w') as fileOut:

        #Xuat thong bao loi
        fileOut.write('Khong tim thay file input!')


#Khoi lenh duoc thuc thi khi xay ra loi "Sai dinh dang dau vao"

except:
    with open('bai11Ra.txt', 'w') as fileOut:

        #Xuat thong bao loi
        fileOut.write('Dinh dang dau vao khong hop le!')