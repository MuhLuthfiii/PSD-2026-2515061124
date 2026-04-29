A. Judul Program

Sistem Transaksi E-Wallet Berbasis Vector (Dynamic Array)

B. Deskripsi Singkat

Program ini merupakan implementasi sistem sederhana yang digunakan untuk mencatat riwayat transaksi pada dompet digital (e-wallet). Pengguna dapat menambahkan transaksi (pemasukan atau pengeluaran), melihat riwayat transaksi, mengubah data transaksi, menghapus transaksi, serta menghitung saldo akhir berdasarkan seluruh data yang tersimpan.

Struktur data yang digunakan dalam program ini adalah Vector (Dynamic Array) yang diimplementasikan secara manual menggunakan Python. Vector memungkinkan penyimpanan data yang bersifat dinamis, di mana kapasitas memori dapat bertambah secara otomatis ketika jumlah data melebihi kapasitas awal. Operasi utama yang diterapkan meliputi insert (push_back), delete, update (set), dan access (get) dengan kompleksitas waktu yang sesuai karakteristik dynamic array.

C. Source Code dan Penjelasan

<img width="1556" height="5270" alt="ss TA SD" src="https://github.com/user-attachments/assets/13ca086d-d344-4141-b591-654632375a6e" />


Penjelasan Kode Program 
1. Class Vector (Inisialisasi Awal)
def __init__(self):
    self.capacity = 2
    self.length = 0
    self.data = [None] * self.capacity
- self.capacity: Digunakan untuk mengatur kapasitas awal vector (alokasi memori awal).
- self.length Digunakan untuk jumlah data aktual (masih kosong).
- self.data = [None] * self.capacity: Digunakan untuk membuat array dengan ukuran sesuai kapasitas.

2. Fungsi Resize 
- def resize(self, new_capacity): Digunakan untuk Mendefinisikan fungsi untuk memperbesar kapasitas vector.
- new_data = [None] * new_capacity: Digunakan untuk Membuat array baru dengan kapasitas lebih besar.
- for i in range(self.length):
    new_data[i] = self.data[i]: Digunakan untuk Menyalin seluruh data lama ke array baru.
- self.data = new_data: Digunakan untuk mengganti array lama dengan array baru.
- self.capacity = new_capacity: Digunakan untuk mengganti array lama dengan array baru.

3. Fungsi push_back 
- def push_back(self, value): Digunakan sebagai Fungsi untuk menambahkan data ke akhir vector.
- if self.length == self.capacity: Digunakan untuk Mengecek apakah vector sudah penuh.
- self.resize(self.capacity * 2): Digunakan Jika penuh maka kapasitas diperbesar 2x lipat.
- self.data[self.length] = value: Digunakan untuk Menyimpan data di posisi terakhir.
- self.length += 1: Digunakan untuk Menambah jumlah elemen.

4. Fungsi get
- def get(self, index): Digunakan untuk Mengambil data berdasarkan index.
- if 0 <= index < self.length: Digunakan untuk memvalidasi agar index tidak keluar batas.
- return self.data[index]: Digunakan untuk Mengembalikan data sesuai index.
- return None: Digunakan jika index tidak valid maka kembalikan None.

5. Fungsi set (Update Data)
- def set(self, index, value): Digunakan untuk Mengubah data pada posisi tertentu.
- if 0 <= index < self.length:
    self.data[index] = value: Digunakan Jika index valid maka data diganti dengan nilai baru.

6. Fungsi delete (Hapus Data)
- def delete(self, index): Digunakan untuk Menghapus elemen berdasarkan index.
- if 0 <= index < self.length: Digunakan untuk memvalidasi index.
- for i in range(index, self.length - 1):
    self.data[i] = self.data[i + 1]: Digunakan untuk menggeser semua elemen setelah index ke kiri.
- self.length -= 1: Digunakan untuk mengurangi jumlah data.

7. Fungsi size (Jumlah Data)
- def size(self):
    return self.length
Mengembalikan jumlah elemen dalam vector.

8. Fungsi display (Menampilkan Data)
- def display(self):
Menampilkan seluruh isi vector.
- if self.length == 0:
Mengecek apakah kosong.
- print("Belum ada transaksi.")
Jika kosong → tampilkan pesan.
- for i in range(self.length):
Loop semua data.
- t = self.data[i]
Mengambil data transaksi.
- print(f"{i}. [{t['tipe']}] Rp{t['jumlah']} - {t['keterangan']}")
Menampilkan data dalam format rapi.

9. Fungsi Menu
- def menu():
Menampilkan pilihan menu ke user.
- print("1. Tambah Transaksi")
...
Menampilkan opsi program.

10. Fungsi Main (Program Utama)
- def main():
Fungsi utama pengendali program.
- transaksi = Vector()
Membuat object vector untuk menyimpan data.
- while True:
Loop agar program terus berjalan.

11. Input Pilihan User
- pilih = int(input("Pilih: "))
User memilih menu.

12. Tambah Transaksi
- if pilih == 1:
Kondisi menu tambah.
- tipe = input("Tipe (masuk/keluar): ").lower()
Input jenis transaksi.
- jumlah = int(input("Jumlah: "))
Input nominal.
- transaksi.push_back({...})
Data dimasukkan ke vector.

13. Tampilkan Data
- elif pilih == 2:
    transaksi.display()
Menampilkan seluruh transaksi.

14. Edit Data
- elif pilih == 3:
Mengubah data berdasarkan index.
- transaksi.set(idx, {...})
Update data di vector.

15. Hapus Data
- elif pilih == 4:
Menghapus transaksi.
- transaksi.delete(idx)
Menghapus dan menggeser elemen.

16. Hitung Saldo
- elif pilih == 5:
saldo = 0
Inisialisasi saldo.
- for i in range(transaksi.size()):
Loop semua transaksi.
- t = transaksi.get(i)
Ambil data.
- if t["tipe"] == "masuk":
    saldo += t["jumlah"]
Tambah saldo.
- elif t["tipe"] == "keluar":
    saldo -= t["jumlah"]
Kurangi saldo.

17. Keluar Program
- elif pilih == 6:
    break
Menghentikan program.

18. Menjalankan Program
- if __name__ == "__main__":
    main()
Entry point program.
Menjalankan fungsi utama.


d. Output Program

(Silakan screenshot hasil running program dari terminal/console kamu)

🖥️ Contoh Output
=== E-WALLET HISTORY ===
1. Tambah Transaksi
2. Lihat Riwayat
3. Edit Transaksi
4. Hapus Transaksi
5. Hitung Saldo
6. Keluar

Pilih: 1
Tipe: masuk
Jumlah: 100000
Keterangan: gaji

Pilih: 1
Tipe: keluar
Jumlah: 25000
Keterangan: makan

Pilih: 2
=== RIWAYAT TRANSAKSI ===
0. [masuk] Rp100000 - gaji
1. [keluar] Rp25000 - makan

Pilih: 5
Saldo saat ini: Rp75000
🧾 Penjelasan Output
Program berhasil menerima input transaksi
Data tersimpan dalam vector
Riwayat transaksi ditampilkan sesuai input
Perhitungan saldo:
100000 (masuk)
-25000 (keluar)
total = 75000
Tidak terjadi error → program berjalan dengan baik
🔥 Kesimpulan Singkat (Opsional untuk Penutup)

Program ini membuktikan bahwa struktur data Vector (dynamic array) dapat digunakan untuk membangun sistem riil seperti pencatatan transaksi. Kelebihan utamanya adalah fleksibilitas ukuran data, namun memiliki kekurangan pada operasi penghapusan karena membutuhkan pergeseran elemen.
