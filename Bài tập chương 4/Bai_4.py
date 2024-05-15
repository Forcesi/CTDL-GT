def HauTo(bt):
    stack_toan_hang = []
    stack_toan_tu = []
    bieu_thuc_hau_to = ""

    for ky_tu in bt:
        if ky_tu.isdigit():
            stack_toan_hang.append(ky_tu)
        else:
            stack_toan_tu.append(ky_tu)

    while stack_toan_hang:
        bieu_thuc_hau_to += stack_toan_hang.pop(0)
        if stack_toan_tu:
            bieu_thuc_hau_to += stack_toan_tu.pop(0)

    return bieu_thuc_hau_to

# Sử dụng
bieu_thuc_trung_to = "35+7*"
bieu_thuc_hau_to = HauTo(bieu_thuc_trung_to)
print(f"Biểu thức hậu tố: {bieu_thuc_hau_to}")