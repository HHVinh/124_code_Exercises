try:
    a = int(input('Nhập số nguyên từ 1 đến 9: '))
    if a <1 or a>10:
        print('Nhập lại số nguyên từ 1 đến 9!')
    else:
        for hang in range(1,a+1):
            for cot in range(1,hang+1):
                print(cot,end=' ')
            print()    
except:
    print('Dữ liệu đầu vào không hợp lệ')