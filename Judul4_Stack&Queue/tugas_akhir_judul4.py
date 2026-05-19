class QueueArray:
    def __init__(self, max_size=5):
        self.MAX = max_size
        self.q = [None] * self.MAX
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        if self.is_empty():
            return False

        jumlah_data = self.rear - self.front + 1
        return jumlah_data == self.MAX

    def enqueue(self, data):
        if self.is_full():
            print("Antrean sudah penuh, tidak bisa menambahkan antrean lagi")
            return

        elif self.is_empty():
            self.front = 0

        else:
            self.rear += 1
            self.q[self.rear] = data
            print(f"{data} berhasil masuk ke antrean")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        data = self.q[self.front]
        print(f"{data} telah dilayani")

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

    def display(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        print("Daftar antrean:")
        nomor = 1

        for i in range(self.front, self.rear + 1):
            print(f"{nomor}. {self.q[i]}")
            nomor += 1


def main():
    queue = QueueArray()
    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM ANTREAN LAYANAN BPJS ===")
        print("1. Tambah antrean")
        print("2. Layani antrean")
        print("3. Tampilkan antrean")
        print("4. Cek kondisi antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Masukkan nama pasien: ")
            queue.enqueue(nama)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.display()

        elif pilih == 4:
             if queue.is_empty():
                print("Antrean BPJS sedang kosong")

             elif queue.is_full():
                print("Antrean BPJS penuh")

             else:
                print("Antrean BPJS masih tersedia")
        elif pilih == 5:
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()