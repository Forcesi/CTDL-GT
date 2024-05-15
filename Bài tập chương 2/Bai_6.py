def Tru(a, b):
    # Chuyển mảng sang dạng số nguyên
    a = int(''.join(map(str, a)))
    b = int(''.join(map(str, b)))

    # Thực hiện phép trừ
    result = a - b

    # Chuyển kết quả thành chuỗi và loại bỏ số 0 không liên quan ở đầu
    result_str = str(result).lstrip('0')

    # Nếu kết quả rỗng, trả về '0'
    if not result_str:
        result_str = '0'

    # Chuyển kết quả thành mảng
    result_list = list(map(int, result_str))

    return result_list

a = [7, 5, 3]
b = [3, 2, 4]
result = Tru(a, b)
print(result)  