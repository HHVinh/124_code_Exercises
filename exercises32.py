#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())
    
    #Su dung cau truc re nhanh xu ly truong hop n < 0
    if n<0:
        print("Vui long nhap so tu nhien!")
    else: 
        #Ma ascii cua ky tu 'A'
        maAscii = 65
        #Su dung vong lap for de suyet cac dong
        for i in range(n):
            #Tinh toan khoang trang dau moi dong
            khoangTrangDauDong = " "*((n-i)*2-1)
            print(khoangTrangDauDong, end='')
            #Su dung vong lap for de in cac ky tu tren mot dong
            for j in range(2*i+1):
                #Chuyen tu ma ascii sang ky tu
                chuCai = chr(maAscii)
                print(chuCai, end=" ")
                #Tang ma ascii len 1 de duyet ky tu tiep theo
                maAscii += 1
                #Neu ky tu vuot qua chu Z thi quay lai ky tu A ban dau
                if chr(maAscii) > 'Z':
                    maAscii = 65
            print()

#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")