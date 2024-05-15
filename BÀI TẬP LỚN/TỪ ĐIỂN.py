

class Nghia:
    def __init__(self, loai_tu: str, nghia: str, vidu: str) -> None:
        self.__loai_tu = loai_tu
        self.__nghia = nghia
        self.__vidu = vidu
    
    def get_nghia(self):
        return self.__nghia

    def get_loai_tu(self):
        return self.__loai_tu
    
    def get_vidu(self):
        return self.__vidu

    def __str__(self) -> str:
        return f'{self.__loai_tu}, {self.__nghia}, {self.__vidu}'

class Link_List_Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__next = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_next_node(self, node):
        self.__next = node

    def get_next_node(self):
        return self.__next

class Link_List_Meanings:
    def __init__(self) -> None:
        self.__first_node = None

    def set_first_node(self, node: Link_List_Node):
        self.__first_node = node

    def get_first_node(self):
        return self.__first_node

    def insert_node(self, value):
        temp = Link_List_Node(value)
        if self.__first_node is None:
            self.__first_node = temp
            return
        p = self.__first_node
        while p.get_next_node() is not None:
            p = p.get_next_node()
        p.set_next_node(temp)

class Muc_Tu:
    def __init__(self, tu: str) -> None:
        self.__tu = tu
        self.ds_nghia = Link_List_Meanings()
    
    def add_meaning(self, loai_tu, nghia, vidu):
        mean = Nghia(loai_tu, nghia, vidu)
        self.ds_nghia.insert_node(mean)

    def set_tu(self, tu):
        self.__tu = tu

    def get_tu(self):
        return self.__tu

    def __str__(self) -> str:
        output = f"{self.__tu}:\n"
        p = self.ds_nghia.get_first_node()
        while p is not None:
            mean = p.get_value()
            output += f'\t+{mean.get_loai_tu()} {mean.get_nghia()} {mean.get_vidu()}\n'
            p = p.get_next_node()
        return output


class Tu_Dien:
    def __init__(self) -> None:
        self.__tu_dien = []

    def set_tu_dien(self, tu_dien: list):
        self.__tu_dien = tu_dien

    def get_tu_dien(self):
        return self.__tu_dien

        # hàm thêm từ xác định vị trí cần thêm
    def them_tu(self, tu: Muc_Tu):
        if len(self.__tu_dien) == 0:
            self.__tu_dien.append(tu)
            return True

        for i in range(len(self.__tu_dien)):
            t = self.__tu_dien[i]
            if tu.get_tu() < t.get_tu():
                self.__tu_dien = self.__tu_dien[:i] + [tu] + self.__tu_dien[i:]
                return True

            if tu.get_tu() == t.get_tu():
                p = t.ds_nghia.get_first_node()
                while p is not None:
                    if p.get_value().get_nghia() != tu.ds_nghia.get_first_node().get_value().get_nghia():
                        t.ds_nghia.insert_node(tu.ds_nghia.get_first_node().get_value())
                        self.__tu_dien[i] = t
                        return True
                    else:
                        return False
                    
        self.__tu_dien.append(tu)
        return True
    
    def tim_tu(self, t: str):
        for tu in self.__tu_dien:
            if t.lower() == tu.get_tu().lower():
                return tu
        return None

    def xoa_tu(self, tu: str):
        w = self.tim_tu(tu)
        if w is None:
            print(f'{tu} is not exist in dictionary.')
        else:
            self.__tu_dien.remove(w)
            print(f'{tu} removed successfully!')

    def doc_file(self, path: str):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                # loại bỏ ký tự \ufeff ở đầu file khi sử dụng mã hóa utf-8 dùng để xác định thứ tự byte
                if line.startswith('\ufeff'):
                    line = line.lstrip('\ufeff')
                # chia dữ liệu thành 1 mảng được ngăn cách bởi /
                line = line.strip().split(' / ')
                # khởi tạo mục từ
                tu = Muc_Tu(line[0].lower())
                # khởi tạo nghĩa của mục từ
                nghia = Nghia(line[1].lower(), line[2].lower(), line[3])
                # thêm nghĩa vào danh sách nghĩa của mục từ
                tu.ds_nghia.insert_node(nghia)
                # Bắt đầu thêm từ vào từ điển
                self.them_tu(tu)
        
    def ghi_file(self, path: str):
        with open(path, "w", encoding='utf-8') as f:
            for tu in self.__tu_dien:
                p = tu.ds_nghia.get_first_node()
                while p is not None:
                    line = f'{tu.get_tu()} / {p.get_value().get_loai_tu()} / {p.get_value().get_nghia()} / {p.get_value().get_vidu()}\n'
                    f.write(line)
                    p = p.get_next_node()

def main():
    path = 'D:/CTDL&GT/TRẦN TIẾN ĐẠT_N21DCDT023/n21dcdt023_mang.txt'
    tu_dien = Tu_Dien()
    tu_dien.doc_file(path)
    while True:
        print("\nMenu:")
        print("1. Add a new entry to the dictionary: ")
        print("2. Remove a dictionary entry: ")
        print("3. Look up an entry: ")
        print("4. Save dictionary to file")
        print("5. Exit")

        choice = input("Enter your choice (1 - 5): ")

        if choice == "1":
            tu = input("Enter the word: ").lower()
            loai_tu = input("Enter the part_of_speech: ").lower()
            nghia = input("Enter the definition: ").lower()
            vidu = input("Enter the example: ")
            tu_moi = Muc_Tu(tu)
            tu_moi.add_meaning(loai_tu, nghia, vidu)
            if tu_dien.them_tu(tu_moi):
                print(f'{tu} được thêm vào từ điển thành công!')
            else:
                print(f'{tu} đã có trong từ điển không thể thêm nữa!')

        elif choice == "2":
            word = input("Enter the word to remove: ")
            tu_dien.xoa_tu(word)

        elif choice == "3":
            word = input("Enter the word to lookup: ")
            search = tu_dien.tim_tu(word)
            if search is not None:
                print(search)
            else:
                print(f'{word} is not exist in dictionary.')

        elif choice == "4":
            tu_dien.ghi_file(path)
            print('Write file successfully!')
        elif choice == "5":
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == '__main__':
    main()
