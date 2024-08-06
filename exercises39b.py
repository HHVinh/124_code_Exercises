try:
    a = int(input('Nhập số tự nhiên cần kiểm tra: '))
    if a <1:
        print('Hãy nhập số tự nhiên lớn hơn 0')
    else:
        uoc = 0
        for i in range(1,(a//2)+1):
            if a % i ==0:
                uoc +=i
                #print(uoc)
        if uoc == a:
            print(f'{a} là số hoàn hảo')
        else:
            print(f'{a} không là số hoàn hảo')       
except:
    print('Dữ liệu đầu vào không hợp lệ')