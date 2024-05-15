def GiaTri(bt):
    stack_toan_hang = []
    stack_toan_tu = []

    for ky_tu in bt:
        if ky_tu.isdigit():
            stack_toan_hang.append(int(ky_tu))
        else:
            toan_hang2 = stack_toan_hang.pop()
            toan_hang1 = stack_toan_hang.pop()
            if ky_tu == '+':
                ket_qua = toan_hang1 + toan_hang2
            elif ky_tu == '-':
                ket_qua = toan_hang1 - toan_hang2
            elif ky_tu == '*':
                ket_qua = toan_hang1 * toan_hang2
            else:
                ket_qua = toan_hang1 / toan_hang2
            stack_toan_hang.append(ket_qua)

    return stack_toan_hang.pop()

# Sử dụng
bieu_thuc = "135+79-*"
gia_tri = GiaTri(bieu_thuc)
print(f"Giá trị của biểu thức '{bieu_thuc}' là: {gia_tri}")