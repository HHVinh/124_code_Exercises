try:
    #Mo file voi mode='r' de doc file
    with open('bai13Vao.txt', 'r') as fileInp:

        #Dung ham read() doc toan bo du lieu tu file
        toanBoFile = fileInp.read()

    #Dung ham splitlines() cat du lieu theo tung dong va luu thanh danh sach
    danhSachCacDong = toanBoFile.splitlines()

    #Dung ham join() noi cac dong du lieu lai cach nhau 1 khoang trang
    cauChaoHoanChinh = ' '.join(danhSachCacDong)

    #Mo file voi mode='w' de ghi file
    with open('bai13Ra.txt', 'w') as fileOut:

        #Ghi noi dung vao file
        fileOut.write(cauChaoHoanChinh)

#Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
except FileNotFoundError:
   with open('bai13Ra.txt', 'w') as fileOut:
       #Xuat thong bao loi
       fileOut.write('Khong tim thay file input!')