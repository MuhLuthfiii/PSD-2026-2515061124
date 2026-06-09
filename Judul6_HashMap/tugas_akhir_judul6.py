class Node:
    def __init__(self, key, nama, saldo):
        self.key = key
        self.nama = nama
        self.saldo = saldo
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, nama, saldo):
        index = self.hash_function(key)

        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.nama = nama
                current.saldo = saldo
                return

            current = current.next

        new_node = Node(key, nama, saldo)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)

        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current

            current = current.next

        return None

    def topup(self, key, nominal):
        akun = self.search(key)

        if akun is not None:
            akun.saldo += nominal
            return True

        return False
    
    def withdraw(self, key, nominal):
        akun = self.search(key)

        if akun is not None:
            akun.saldo -= nominal
            return True
        return False

    def remove_key(self, key):
        index = self.hash_function(key)

        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\n=== DATA AKUN E-WALLET ===")

        for i in range(self.SIZE):
            print(f"{i}: ", end="")

            current = self.table[i]

            while current is not None:
                print(
                    f"[ID:{current.key}, "
                    f"Nama:{current.nama}, "
                    f"Saldo:{current.saldo}] -> ",
                    end=""
                )

                current = current.next

            print("None")


def main():
    ewallet = HashMapSeparateChaining()

    while True:
        print("\n=== MENU E-WALLET ===")
        print("1. Tambah Akun")
        print("2. Cari Akun")
        print("3. Top Up Saldo")
        print("4. WithDraw Saldo")
        print("5. Hapus Akun")
        print("6. Tampilkan Data")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                id_akun = int(input("Masukkan ID Akun : "))
                nama = input("Masukkan Nama : ")
                saldo = int(input("Masukkan Saldo Awal : "))

                ewallet.insert(id_akun, nama, saldo)

                print("Akun berhasil ditambahkan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                id_akun = int(input("Masukkan ID Akun : "))

                akun = ewallet.search(id_akun)

                if akun is not None:
                    print("\nData ditemukan")
                    print(f"ID Akun : {akun.key}")
                    print(f"Nama : {akun.nama}")
                    print(f"Saldo : Rp{akun.saldo}")
                else:
                    print("Data tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            try:
                id_akun = int(input("Masukkan ID Akun : "))
                nominal = int(input("Nominal Top Up : "))

                if ewallet.topup(id_akun, nominal):
                    print("Top up berhasil")
                else:
                    print("Akun tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")
        
        elif pilih == 4:
             try:
                id_akun = int(input("Masukkan ID Akun : "))
                nominal = int(input("Nominal WithDraw : "))

                if ewallet.withdraw(id_akun, nominal):
                    print("WithDraw berhasil")
                else:
                    print("Akun tidak ditemukan")

             except ValueError:
                print("Input tidak valid!")
    
                

        elif pilih == 5:
            try:
                id_akun = int(input("Masukkan ID Akun : "))

                if ewallet.remove_key(id_akun):
                    print("Akun berhasil dihapus")
                else:
                    print("Akun tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 6:
            ewallet.display()

        elif pilih == 7:
            print("Program selesai")
            break

        else:
            print("Pilihan tidak tersedia")


if __name__ == "__main__":
    main()