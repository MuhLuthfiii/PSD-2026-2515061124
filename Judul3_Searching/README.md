# A. Judul Program

Mencari Data Buku Berdasarkan Judulnya (Sequential Search Sentinel)

# B. Deskripsi Singkat

Program ini menggunakan algoritma Insertion Sort untuk mengurutkan data buku dari tahun terbit paling lama ke yang paling baru. Setelah data berhasil diurutkan, program menggunakan metode Sequential Search Sentinel untuk mencari judul buku tertentu. Metode pencarian ini bekerja dengan menambahkan data sementara di akhir list agar proses pencarian dapat berjalan lebih sederhana tanpa harus terus memeriksa batas data.

Program juga dilengkapi validasi input sehingga pengguna dapat mengulang pencarian apabila buku yang dicari belum tersedia di dalam data. Dengan adanya fitur sorting dan searching, data buku menjadi lebih rapi dan lebih mudah ditemukan.

# C. Source Code

<img width="1372" height="3370" alt="code3" src="https://github.com/user-attachments/assets/c932a638-200b-4c9e-a768-b478f39402f6" />

# Penjelasan Kode

# 1. Fungsi sequential_search_sentinel()
- def sequential_search_sentinel(data, n, target):

  Fungsi ini digunakan untuk mencari data buku berdasarkan judul menggunakan metode sequential search sentinel.

- data.append({
    "judul": target,
    "tahun": 0
  })

  Fungsi ini digunakan agar program menambahkan data sementara di akhir list untuk mempermudah proses pencarian.

- i = 0

  Variabel i digunakan sebagai indeks awal pencarian.

- while data[i]["judul"].lower() != target.lower():

  Digunakan agar program memeriksa data satu per satu sampai menemukan judul yang sesuai dengan input pengguna.

- i += 1

  Digunakan jika data belum ditemukan, indeks berpindah ke data berikutnya.

- data.pop()

  Digunakan agar data yang tadi ditambahkan akan dihapus kembali agar data asli tetap seperti semula.

- if i < n:

  Fungsi decision agar program memeriksa apakah data ditemukan sebelum mencapai sentinel.

- return True, i

  Jika data ditemukan, fungsi mengembalikan nilai True dan indeks data.

- return False, -1

  Jika data tidak ditemukan, fungsi mengembalikan False dan indeks -1.

# 2. Fungsi main
- def main():

  Fungsi ini sebagai bagian utama yang mengatur seluruh jalannya program.

# 3. Proses Searching
- while True:

  Program akan terus meminta input pencarian sampai buku ditemukan.

- cari = input("\nMasukkan judul buku yang dicari: ")

  Digunakan untuk user memasukkan judul buku yang ingin dicari.

- found, index = sequential_search_sentinel(data_buku, n, cari)

  Membuat sebuah variabel untuk memanggil fungsi sequential search sentinel untuk mencari data buku.

- if found:

  Memeriksa apakah buku berhasil ditemukan.

- print(f"\nBuku ditemukan pada indeks ke-{index}")

  Menampilkan posisi indeks data buku.

- print(f"Judul : {data_buku[index]['judul']}")

  Menampilkan judul buku yang ditemukan.

- print(f"Tahun : {data_buku[index]['tahun']}")

  Menampilkan tahun terbit buku.

- break

  Menghentikan perulangan pencarian jika data sudah ditemukan.

- else:

  Dijalankan jika buku tidak ditemukan.

- print("\nBuku tidak terdaftar, silahkan cari kembali")

  Menampilkan pesan agar pengguna melakukan pencarian ulang.

# D. Output Program

<img width="313" height="295" alt="Screenshot 2026-05-07 170233" src="https://github.com/user-attachments/assets/464c6497-b849-4153-ac5e-e7e3973dd1ab" />

<img width="459" height="118" alt="Screenshot 2026-05-07 170127" src="https://github.com/user-attachments/assets/3853d075-bcad-4f17-8e87-7175a60aec50" />

<img width="520" height="277" alt="Screenshot 2026-05-07 170054" src="https://github.com/user-attachments/assets/e0013833-ca1b-433e-851c-e8d2398c63d2" />

# Penjelasan Output

Output program menunjukkan bahwa data buku berhasil dimasukkan dan diproses dengan baik. Pada awal program, pengguna diminta memasukkan jumlah buku beserta data berupa judul dan tahun terbit. Setelah semua data dimasukkan, program menampilkan data sesuai urutan input pengguna.

Selanjutnya program menjalankan proses insertion sort untuk mengurutkan data berdasarkan tahun terbit. Setelah proses selesai, urutan data berubah menjadi lebih rapi, dimulai dari tahun paling lama ke yang paling baru.

Program kemudian meminta pengguna memasukkan judul buku yang ingin dicari. Proses pencarian dilakukan menggunakan sequential search sentinel dengan memeriksa data satu per satu sampai buku ditemukan. Pada contoh di atas, buku berjudul “Python” berhasil ditemukan pada indeks ke-2 sehingga program menampilkan informasi judul dan tahun terbit buku tersebut.

Jika buku yang dicari tidak tersedia, program akan menampilkan pesan bahwa buku tidak terdaftar dan pengguna diminta melakukan pencarian ulang. Hal ini menunjukkan bahwa program sudah mampu menjalankan proses sorting dan searching dengan baik tanpa mengalami error.

# E. Link Youtube
https://youtu.be/3IVDuCYOamY
