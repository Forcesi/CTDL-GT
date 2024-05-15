def So(x, y):
    # Định nghĩa hàm để tính tổng các ước số của một số
    def tong_cac_uoc_so(n):
        tong_uoc = 1  # Bắt đầu từ 1 vì 1 là ước số của mọi số
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                tong_uoc += i
                if i != n // i:  # Thêm cặp ước số
                    tong_uoc += n // i
        return tong_uoc

    # Lặp qua phạm vi từ x đến y
    for n in range(x, y + 1):
        s = tong_cac_uoc_so(n)
        if s < n:
            print(f"{n} là số thiếu sót vì tổng các ước số của nó là {s} nhỏ hơn {n}.")
        elif s == n:
            print(f"{n} là số hoàn hảo vì tổng các ước số của nó là {s} bằng {n}.")
        else:
            print(f"{n} là số dư thừa vì tổng các ước số của nó là {s} lớn hơn {n}.")

So(6, 12)
