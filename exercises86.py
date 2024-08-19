def ten_QuocTich(dong1,dong2):
    dsDong1 = [tu.strip() for tu in dong1.split(',')]
    dsDong2 = [tu.strip() for tu in dong2.split(',')]

    if len(dsDong1) != len(dsDong2):
        print('Dữ liệu 2 dòng chưa cùng số lượng phần tử')
    else:
        for i in range(len(dsDong1)):
            print(f'{dsDong1[i]} - {dsDong2[i]}')

dong1 = input('Nhập tên cách nhau bởi dấu ",": ') 
dong2 = input('Nhập tên cách nhau bởi dấu ",": ')            

ten_QuocTich(dong1,dong2)
