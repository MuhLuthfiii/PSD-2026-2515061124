# A. Judul Program
Program Simulasi Antrian BPJS Menggunakan Queue
# B. Deskripsi Singkat

Program ini dibuat untuk mensimulasikan sistem antrean  pada sebuah Layanan BPJS menggunakan konsep struktur data Queue. Pada program ini, Queue digunakan untuk mengatur antrean pasien secara berurutan berdasarkan prinsip FIFO (First In First Out), yaitu Pasien yang datang terlebih dahulu akan dilayani terlebih dahulu.

Program memiliki beberapa fitur utama seperti Menambahkan antrean pasien, Melayani antrean pasien, Menampilkan daftar antrean, Mengecek kondisi antrean kosong atau penuh, dan Membatasi jumlah antrean maksimal. Algoritma struktur data yang diterapkan pada program ini adalah Queue (FIFO). Queue digunakan untuk menyimpan data antrean pasien sehingga proses pelayanan menjadi lebih teratur sesuai urutan kedatangan.


# C. Source Code
<img width="1508" height="4206" alt="code" src="https://github.com/user-attachments/assets/3b452eb7-c4b0-46a4-a880-d218f3a458e9" />

# Penjelasan Source Code

# 1. Membuat Class QueueArray
- class QueueArray:

  Class QueueArray digunakan untuk membuat struktur data Queue sebagai tempat penyimpanan antrean pasien BPJS.
# 2. Constructor
- def __init__(self, max_size=5):

  Constructor digunakan untuk menentukan kapasitas maksimal antrean.

- self.MAX = max_size

  Variabel MAX digunakan untuk menentukan jumlah maksimal pasien dalam antrean.

- self.q = [None] * self.MAX

  Digunakan untuk membuat list kosong sebagai tempat penyimpanan data antrean.

- self.front = -1
  self.rear = -1

  front digunakan untuk menunjukkan posisi antrean paling depan.
  rear digunakan untuk menunjukkan posisi antrean paling belakang.

# 3. Fungsi is_empty()
- def is_empty(self):
    return self.front == -1

  Fungsi ini digunakan untuk mengecek apakah antrean kosong atau tidak. Jika front bernilai -1, berarti belum ada data dalam antrean.
  
# 4. Fungsi is_full()
- def is_full(self):
    return self.rear == self.MAX - 1

  Fungsi ini digunakan untuk mengecek apakah antrean sudah penuh. Jika posisi rear sudah mencapai kapasitas maksimal array, maka antrean tidak bisa ditambah lagi.

# 5. Fungsi enqueue()
- def enqueue(self, data):

  Fungsi enqueue() digunakan untuk menambahkan pasien ke dalam antrean.

- if self.is_full():

  Program akan mengecek terlebih dahulu apakah antrean sudah penuh.

- print("Antrean BPJS sudah penuh")

  Jika penuh, maka program akan menampilkan pesan bahwa antrean tidak bisa ditambahkan lagi.

- if self.is_empty():
    self.front = 0

  Jika antrean masih kosong, maka posisi front diubah menjadi 0.

- self.rear += 1
  self.q[self.rear] = data

  Digunakan untuk menambahkan data pasien ke posisi paling belakang antrean.

# 6. Fungsi dequeue()
- def dequeue(self):

  Fungsi dequeue() digunakan untuk memanggil pasien paling depan.

- if self.is_empty():

  Program akan mengecek apakah antrean kosong.

- data = self.q[self.front]

  Digunakan untuk mengambil data pasien yang berada di posisi paling depan.

- print(f"Pasien {data} sedang dipanggil")

  Program menampilkan nama pasien yang sedang dipanggil untuk pelayanan.

- self.front += 1

  Digunakan untuk memindahkan posisi antrean ke data berikutnya.

# 7. Fungsi display()
- def display(self):

  Fungsi ini digunakan untuk menampilkan seluruh data antrean pasien BPJS.

- for i in range(self.front, self.rear + 1):

  Perulangan digunakan untuk menampilkan seluruh isi antrean mulai dari depan hingga belakang.

# 8. Fungsi main()
- def main():

  Fungsi main() digunakan sebagai program utama untuk menjalankan menu antrean BPJS. Pada bagian ini pengguna dapat memilih menu seperti menambahkan antrean       pasien, memanggil pasien, menampilkan antrean, mengecek kondisi antrean, dan untuk keluar dari program

# 9. Validasi Input
- try:
    pilih = int(input("Pilih menu: "))
  except ValueError:

  Digunakan untuk mencegah error apabila pengguna memasukkan input selain angka.

# 10. Menjalankan Program
- if __name__ == "__main__":
    main()

  Bagian ini digunakan agar program utama dapat dijalankan ketika file Python dieksekusi.

# D. Outuput Program
<img width="323" height="163" alt="Screenshot 2026-05-19 224837" src="https://github.com/user-attachments/assets/1fea4155-5586-454a-908a-b6e52cd34d6f" />
<img width="461" height="162" alt="Screenshot 2026-05-19 224846" src="https://github.com/user-attachments/assets/cfcc8cf8-e3d5-48af-89f9-d19a5d2a67d1" />
<img width="222" height="192" alt="Screenshot 2026-05-19 224904" src="https://github.com/user-attachments/assets/20f4e0d1-18df-4385-847f-7f0e84d709af" />
<img width="295" height="141" alt="Screenshot 2026-05-19 224918" src="https://github.com/user-attachments/assets/cbeac8ae-3519-43e6-be01-b571c6b98cea" />
<img width="293" height="147" alt="Screenshot 2026-05-19 224927" src="https://github.com/user-attachments/assets/135dac07-e328-4f8c-8738-697cc7c64c77" />


# Penjelasan Output
Saat program dijalankan, pengguna akan melihat menu utama sistem antrean BPJS yang terdiri dari beberapa pilihan, seperti menambahkan pasien, memanggil pasien, menampilkan antrean, dan mengecek kondisi antrean.

Ketika pengguna memilih menu tambah antrean pasien, program akan meminta nama pasien yang ingin mengambil nomor antrean BPJS. Nama pasien tersebut kemudian disimpan ke dalam Queue sesuai urutan kedatangan.

Jika kapasitas antrean masih tersedia, program akan menampilkan pesan bahwa pasien berhasil mengambil antrean. Namun jika jumlah antrean sudah mencapai batas maksimal, program akan memberikan informasi bahwa antrean BPJS sudah penuh sehingga pasien baru tidak dapat ditambahkan lagi.

Saat menu tampilkan antrean dipilih, program akan menampilkan seluruh daftar pasien yang sedang menunggu pelayanan. Pasien yang berada di posisi paling depan merupakan pasien yang akan dipanggil terlebih dahulu.

Ketika menu panggil pasien dijalankan, program akan mengambil data pasien paling depan dari Queue. Proses ini menunjukkan bahwa Queue bekerja menggunakan prinsip FIFO (First In First Out), yaitu pasien yang datang lebih awal akan mendapatkan pelayanan lebih dahulu dibanding pasien yang datang setelahnya.

Apabila seluruh antrean sudah selesai dilayani, maka program akan menampilkan pesan bahwa antrean BPJS kosong. Dengan demikian, program berhasil menerapkan konsep Queue dalam simulasi sistem antrean pelayanan BPJS secara sederhana dan teratur.

# E. Link Youtube
https://youtu.be/lpSRmdC1uSU
