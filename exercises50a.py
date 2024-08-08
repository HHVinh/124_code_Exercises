def tinh_Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return tinh_Fibonacci(n-1) + tinh_Fibonacci(n -2)

try:
    n = int(input('Nhập số tự nhiên cần tính: '))
    if n <1:
        print('Hãy nhập số nguyên dương')
    else:
        ketQua  = tinh_Fibonacci(n)
        print(f'Số Fibonacci của {n} = {ketQua}')
except:
    print('Dữ liệu đầu vào không hợp lệ')