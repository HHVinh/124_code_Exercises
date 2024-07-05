# Nhập 3 số a, b, c 
print('Nhập lần lượt số a, số b, số c cách nhau bởi 1 khoảng trắng:')
try:
    a, b, c = map(float,input().split()) # Dùng map và float để chuyển thành số thực

    if a + b > c and a + c >b and b + c > a:
        print('{}, {}, {} là 3 cạnh của tam giác'.format(a,b,c))
    else:
        print('{}, {}, {} không là 3 cạnh của tam giác'.format(a,b,c))
except:
    print('Dữ liệu chưa phù hợp. Vui lòng nhập lại')
    
