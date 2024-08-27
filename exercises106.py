def max_Min_Sum(danhSach):
    gtMax = max(set(danhSach))
    gtMin = min(set(danhSach))
    tongGt = sum(set(danhSach))
    return gtMax, gtMin, tongGt

try: 
    danhSach = set(map(float,input('Nhập các số nguyên dương bất kì: ').split()))
    if len(danhSach) == 0:
        print('Danh sách rỗng')
    else:
        gtriMax, gtriMin, tongGtri = max_Min_Sum(danhSach)
        print('Giá trị cao nhất là: ',gtriMax)
        print('Giá trị thấp nhất là: ',gtriMin)
        print('Tổng các giá trị cao nhất là: ',tongGtri)
except:
    print('Dữ liệu đầu vào chưa hợp lệ')
