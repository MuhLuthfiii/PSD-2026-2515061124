class Vector:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.data = [None] * self.capacity

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def push_back(self, value):
        if self.length == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.length] = value
        self.length += 1

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        return None

    def set(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value

    def delete(self, index):
        if 0 <= index < self.length:
            for i in range(index, self.length - 1):
                self.data[i] = self.data[i + 1]
            self.length -= 1

    def size(self):
        return self.length

    def display(self):
        if self.length == 0:
            print("Belum ada transaksi.")
        else:
            print("\n=== RIWAYAT TRANSAKSI ===")
            for i in range(self.length):
                t = self.data[i]
                print(f"{i}. [{t['tipe']}] Rp{t['jumlah']} - {t['keterangan']}")


# ===== MENU =====
def menu():
    print("\n=== E-WALLET KANTONGKU ===")
    print("1. Tambah Transaksi")
    print("2. Lihat Riwayat")
    print("3. Edit Transaksi")
    print("4. Hapus Transaksi")
    print("5. Hitung Saldo")
    print("6. Keluar")


def main():
    transaksi = Vector()

    while True:
        menu()
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            tipe = input("Tipe (masuk/keluar): ").lower()
            try:
                jumlah = int(input("Jumlah: "))
                ket = input("Keterangan: ")
                transaksi.push_back({
                    "tipe": tipe,
                    "jumlah": jumlah,
                    "keterangan": ket
                })
                print("Transaksi berhasil ditambahkan!")
            except ValueError:
                print("Jumlah harus angka!")

        elif pilih == 2:
            transaksi.display()

        elif pilih == 3:
            transaksi.display()
            try:
                idx = int(input("Index yang diubah: "))
                tipe = input("Tipe baru: ").lower()
                jumlah = int(input("Jumlah baru: "))
                ket = input("Keterangan baru: ")
                transaksi.set(idx, {
                    "tipe": tipe,
                    "jumlah": jumlah,
                    "keterangan": ket
                })
                print("Transaksi diperbarui!")
            except:
                print("Input tidak valid!")

        elif pilih == 4:
            transaksi.display()
            try:
                idx = int(input("Index yang dihapus: "))
                transaksi.delete(idx)
                print("Transaksi dihapus!")
            except:
                print("Input tidak valid!")

        elif pilih == 5:
            saldo = 0
            for i in range(transaksi.size()):
                t = transaksi.get(i)
                if t["tipe"] == "masuk":
                    saldo += t["jumlah"]
                elif t["tipe"] == "keluar":
                    saldo -= t["jumlah"]
            print(f"Saldo saat ini: Rp{saldo}")

        elif pilih == 6:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()