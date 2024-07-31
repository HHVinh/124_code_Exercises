
try:
    # Nhập 3 số a, b, c và chuyển đổi thành số thực
    a, b, c = map(float, input('Nhập 3 số a, b, c cần kiểm tra: ').split())

    # Kiểm tra điều kiện tam giác
    if a + b > c and a + c > b and b + c > a:
        print(f'{a}, {b}, {c} là 3 cạnh của tam giác')
    else:
        print(f'{a}, {b}, {c} không phải là 3 cạnh của tam giác')
except ValueError:
    # Xử lý lỗi khi không thể chuyển đổi giá trị nhập vào thành float
    print('Lỗi: Vui lòng nhập đúng 3 số thực, cách nhau bằng khoảng trắng.')
