try:
    a = int(input('Nhập số nguyên từ 1 đến 9: '))
    if a >0 and a <10:
        for hang in range(a):
            for cot in range(a - hang,0,-1):
                print(cot,end=' ')
            print()
    else:
        print('Số nguyên phải từ 1 đến 9')        
except:
    print('Dữ liệu đầu vào không hợp lệ')