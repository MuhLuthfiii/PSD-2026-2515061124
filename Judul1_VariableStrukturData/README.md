# A. Judul Program

Sistem Transaksi E-Wallet Berbasis Vector (Dynamic Array)

# B. Deskripsi Singkat

Program ini merupakan implementasi sistem  yang digunakan untuk  transaksi pada E-Wallet. Pengguna dapat menambahkan transaksi (pemasukan atau pengeluaran), melihat riwayat transaksi, mengubah data transaksi, menghapus transaksi, serta menghitung saldo akhir berdasarkan seluruh data yang tersimpan.

Struktur data yang digunakan dalam program ini adalah Vector (Dynamic Array) yang diimplementasikan secara manual menggunakan Python. Vector memungkinkan penyimpanan data yang bersifat dinamis, di mana kapasitas memori dapat bertambah secara otomatis ketika jumlah data melebihi kapasitas awal. Operasi utama yang diterapkan meliputi insert (push_back), delete, update (set), dan access (get) dengan kompleksitas waktu yang sesuai karakteristik dynamic array.

# C. Source Code dan Penjelasan

<img width="1556" height="5270" alt="ss TA SD" src="https://github.com/user-attachments/assets/13ca086d-d344-4141-b591-654632375a6e" />



# Penjelasan Kode Program 
# 1. Class Vector (Inisialisasi Awal)
def __init__(self):
    self.capacity = 2
    self.length = 0
    self.data = [None] * self.capacity
- self.capacity: Digunakan untuk mengatur kapasitas awal vector (alokasi memori awal).
- self.length Digunakan untuk jumlah data aktual (masih kosong).
- self.data = [None] * self.capacity: Digunakan untuk membuat array dengan ukuran sesuai kapasitas.

# 2. Fungsi Resize 
- def resize(self, new_capacity): Digunakan untuk Mendefinisikan fungsi untuk memperbesar kapasitas vector.
- new_data = [None] * new_capacity: Digunakan untuk Membuat array baru dengan kapasitas lebih besar.
- for i in range(self.length):
    new_data[i] = self.data[i]: Digunakan untuk Menyalin seluruh data lama ke array baru.
- self.data = new_data: Digunakan untuk mengganti array lama dengan array baru.
- self.capacity = new_capacity: Digunakan untuk mengganti array lama dengan array baru.

# 3. Fungsi push_back 
- def push_back(self, value): Digunakan sebagai Fungsi untuk menambahkan data ke akhir vector.
- if self.length == self.capacity: Digunakan untuk Mengecek apakah vector sudah penuh.
- self.resize(self.capacity * 2): Digunakan Jika penuh maka kapasitas diperbesar 2x lipat.
- self.data[self.length] = value: Digunakan untuk Menyimpan data di posisi terakhir.
- self.length += 1: Digunakan untuk Menambah jumlah elemen.

# 4. Fungsi get
- def get(self, index): Digunakan untuk Mengambil data berdasarkan index.
- if 0 <= index < self.length: Digunakan untuk memvalidasi agar index tidak keluar batas.
- return self.data[index]: Digunakan untuk Mengembalikan data sesuai index.
- return None: Digunakan jika index tidak valid maka kembalikan None.

# 5. Fungsi set (Update Data)
- def set(self, index, value): Digunakan untuk Mengubah data pada posisi tertentu.
- if 0 <= index < self.length:
    self.data[index] = value: Digunakan Jika index valid maka data diganti dengan nilai baru.

# 6. Fungsi delete (Hapus Data)
- def delete(self, index): Digunakan untuk Menghapus elemen berdasarkan index.
- if 0 <= index < self.length: Digunakan untuk memvalidasi index.
- for i in range(index, self.length - 1):
    self.data[i] = self.data[i + 1]: Digunakan untuk menggeser semua elemen setelah index ke kiri.
- self.length -= 1: Digunakan untuk mengurangi jumlah data.

# 7. Fungsi size (Jumlah Data)
- def size(self):
    return self.length: Digunakan untuk Mengembalikan jumlah elemen dalam vector.

# 8. Fungsi display (Menampilkan Data)
- def display(self): Digunakan untuk Menampilkan seluruh isi vector.
- if self.length == 0: Digunakan untuk Mengecek apakah kosong.
- print("Belum ada transaksi."): Digunakan kika kosong maka tampilkan pesan.
- for i in range(self.length): Untuk Loop semua data.
- t = self.data[i]: Digunakan untuk Mengambil data transaksi.
- print(f"{i}. [{t['tipe']}] Rp{t['jumlah']} - {t['keterangan']}"): Digunakan untuk Menampilkan data dalam format rapi.

# 9. Fungsi Menu
- def menu():: Digunakan untuk Menampilkan pilihan menu ke user.
- print("1. Tambah Transaksi"): Digunakan untuk Menampilkan opsi program.

# 10. Fungsi Main (Program Utama)
- def main():: Digunakan sebagai Fungsi utama pengendali program.
- transaksi = Vector(): Digunakan untuk Membuat object vector untuk menyimpan data.
- while True:: Digunakan untuk Loop agar program terus berjalan.

# 11. Input Pilihan User
- pilih = int(input("Pilih: ")): Digunakan seobagai pilihan User dalam memilih menu.

# 12. Tambah Transaksi
- if pilih == 1: Digunakan untuk Kondisi menu tambah.
- tipe = input("Tipe (masuk/keluar): ").lower(): Digunakan untuk menginput jenis transaksi.
- jumlah = int(input("Jumlah: ")): Digunakan untuk menginputkan nominal.
- transaksi.push_back({...}): Digunakan agar Data dimasukkan ke vector.

# 13. Tampilkan Data
- elif pilih == 2:
    transaksi.display(): Digunakan untuk Menampilkan seluruh transaksi.

# 14. Edit Data
- elif pilih == 3: Digunakan untuk Mengubah data berdasarkan index.
- transaksi.set(idx, {...}): Digunakan untuk mengupdate data di vector.

# 15. Hapus Data
- elif pilih == 4: Untuk Menghapus transaksi.
- transaksi.delete(idx): Untuk Menghapus dan menggeser elemen.

# 16. Hitung Saldo
- elif pilih == 5:
saldo = 0: Digunakan untuk menginisialisasikan saldo.
- for i in range(transaksi.size()): Digunakan untuk Loop semua transaksi.
- t = transaksi.get(i): Digunakan untuk mengambil data.
- if t["tipe"] == "masuk":
    saldo += t["jumlah"]: Digunakan untuk menambah saldo.
- elif t["tipe"] == "keluar":
    saldo -= t["jumlah"]: Digunakan untuk mengurangi saldo.

# 17. Keluar Program
- elif pilih == 6:
    break: Untuk menghentikan program.

# 18. Menjalankan Program
- if __name__ == "__main__":
    main(): Digunakan untuk meng-entry point program menjalankan fungsi utama.


# D. Output Program

<img width="325" height="276" alt="Screenshot 2026-04-29 223505" src="https://github.com/user-attachments/assets/eb177d54-a7a3-4a70-8325-b46e5477b0fd" />
<img width="251" height="250" alt="Screenshot 2026-04-29 223525" src="https://github.com/user-attachments/assets/ddd95b7e-efd9-4cb5-bc6e-bd288b92beaa" />
<img width="264" height="166" alt="Screenshot 2026-04-29 223613" src="https://github.com/user-attachments/assets/dd6a229d-6eab-44d2-9d8e-a371d157074e" />
<img width="263" height="202" alt="Screenshot 2026-04-29 223647" src="https://github.com/user-attachments/assets/60e8fd4d-e1a2-4cd1-9036-3ca10f24c64f" />
<img width="307" height="195" alt="Screenshot 2026-04-29 223657" src="https://github.com/user-attachments/assets/b8419ac7-17b9-4928-be6e-e534dbb76eea" />

# Penjelasan Output
Output dari program ini menunjukkan bagaimana sistem transaksi dompet digital bekerja melalui interaksi langsung dengan pengguna. Ketika program dijalankan, tampilan awal yang muncul adalah menu utama yang berisi beberapa pilihan, seperti menambahkan transaksi, melihat riwayat, mengedit data, menghapus data, menghitung saldo, hingga keluar dari program. Menu ini akan terus ditampilkan karena program menggunakan perulangan, sehingga pengguna bisa melakukan beberapa operasi sekaligus tanpa perlu menjalankan ulang program.

Saat pengguna memilih untuk menambahkan transaksi, sistem akan meminta beberapa data seperti jenis transaksi (masuk atau keluar), jumlah uang, serta keterangan tambahan. Setelah semua data diinput, program akan memberikan notifikasi bahwa transaksi berhasil disimpan. Data tersebut kemudian dimasukkan ke dalam vector, yang dapat menyesuaikan kapasitasnya secara otomatis jika data yang disimpan semakin banyak. 

Ketika pengguna ingin melihat riwayat transaksi, sistem akan menampilkan seluruh data yang sudah tersimpan secara berurutan berdasarkan indeks. Informasi yang ditampilkan meliputi nomor urut, jenis transaksi, jumlah uang, dan keterangan. Jika belum ada data yang tersimpan, program akan memberikan informasi bahwa data masih kosong, sehingga pengguna tidak kebingungan.

Pada fitur pengeditan data, pengguna dapat memilih transaksi tertentu berdasarkan indeks, lalu menggantinya dengan data yang baru. Setelah proses ini selesai, program akan menampilkan pesan bahwa data berhasil diperbarui. Perubahan ini langsung diterapkan pada data yang ada tanpa memengaruhi jumlah total data.

Sementara itu, pada fitur penghapusan, pengguna dapat menghapus data transaksi tertentu. Setelah data dihapus, sistem akan memberikan notifikasi bahwa penghapusan berhasil dilakukan. data setelah posisi yang dihapus akan bergeser ke depan agar susunan data tetap rapi, dan jumlah data dalam vector akan berkurang.

Untuk fitur perhitungan saldo, sistem akan membaca seluruh transaksi yang tersimpan, kemudian menjumlahkan semua transaksi yang bersifat pemasukan dan mengurangi transaksi pengeluaran. Hasil akhirnya akan ditampilkan sebagai saldo saat ini. Dari sini terlihat bahwa program tidak hanya menyimpan data, tetapi juga mampu mengolah data tersebut menjadi informasi yang berguna.

Selain itu, program juga sudah dilengkapi dengan penanganan kesalahan input. Jika pengguna memasukkan data yang tidak sesuai, program akan menampilkan pesan kesalahan tanpa menghentikan jalannya program, sehingga tetap bisa digunakan dengan normal.

# E. Link Youtube
https://youtu.be/PDt_FSGFrUQ
