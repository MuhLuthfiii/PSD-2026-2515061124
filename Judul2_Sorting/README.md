# A. JUDUL PROGRAM
Pengurutan Buku Sesuai Tahun Terbit (Insertion Sort)

# B. DESKRIPSI SINGKAT
Program ini dibuat untuk mengelola data buku sederhana yang terdiri dari judul dan tahun terbit. Pengguna atau user dapat memasukkan beberapa data buku, lalu program akan mengurutkan data tersebut berdasarkan tahun terbit, mulai dari yang paling lama sampai yang paling baru. Contoh penerapannya bisa ditemukan pada sistem katalog perpustakaan atau pengelolaan arsip buku.

Metode yang digunakan dalam program ini adalah insertion sort. Cara kerjanya sederhana, yaitu dengan mengambil satu data, lalu membandingkannya dengan data sebelumnya dan menempatkannya di posisi yang sesuai. Proses ini dilakukan berulang sampai semua data tersusun rapi. Pada program ini, data tidak hanya berupa angka, tetapi berbentuk sebuah dictionary, sehingga proses pengurutan dilakukan berdasarkan nilai tahun terbit.

# C. SOURCE CODE
<img width="1372" height="1888" alt="code2" src="https://github.com/user-attachments/assets/76bacb9e-ee12-4193-bc7a-ba69d2ee29e8" />

# Penjelasan Kode

# 1. Fungsi Insertion Sort
- def insertion_sort(data):

  Fungsi ini dibuat untuk mengurutkan data buku berdasarkan tahun terbit.

- for i in range(1, len(data)):

  Berfungsi sebagai perulangan dimulai dari indeks ke-1 karena elemen pertama dianggap sudah terurut.

- key = data[i]

  Befungsi untuk menyimpan data yang sedang diproses (buku saat ini).

- j = i - 1

  Berfungsi untuk menentukan posisi sebelumnya untuk dibandingkan.

- while j >= 0 and data[j]["tahun"] > key["tahun"]:

  Berfungsi untuk membandingkan tahun buku sebelumnya dengan buku saat ini. Jika lebih besar, berarti harus digeser.

- data[j + 1] = data[j]

  Berfungsi untuk menggeser data ke kanan.

- j -= 1
  
  Berfungsi untuk memindahkan ke data sebelumnya lagi.

- data[j + 1] = key
  
  Berfungsi untuk menempatkan data (key) pada posisi yang tepat.

# 2. Fungsi Utama Program
- def main():

  Sebagai fungsi utama yang mengatur jalannya program.

- data_buku = []

  Berfungsi untuk membuat list kosong untuk menyimpan data buku.

- try:
    n = int(input("Masukkan jumlah buku: "))

  Berfungsi untuk meminta jumlah buku dari pengguna.

- except ValueError:
    print("Input hanya berupa angka")
    return

  Berfungsi untuk menangani kesalahan jika input bukan angka, lalu program dihentikan.

# 3. Input Data Buku
- for i in range(n):

  Berfungsi sebagai perulangan untuk memasukkan data sebanyak jumlah yang diminta.

- while True:

  Digunakan agar input diulang jika terjadi kesalahan.

- judul = input(f"Judul buku ke-{i+1}: ")

  Untuk mengambil input judul buku.

- tahun = int(input("Tahun terbit: "))

  Untuk mengambil input tahun terbit (harus angka).

- data_buku.append({
    "judul": judul,
    "tahun": tahun})

  Untuk menyimpan data dalam bentuk dictionary ke dalam list.

- break

  Untuk keluar dari perulangan jika input valid.

- except ValueError:
    print("Input tidak valid, silahkan masukkan kembali")

  Berfungsi jika input salah, user diminta mengulang.

# 4. Menampilkan Data Sebelum Sorting
- print("\nData sebelum diurutkan:")

  Berfungsi untuk menampilkan judul bagian.

- for b in data_buku:

  Berfungsi sebagai perulangan untuk membaca seluruh data.

- print(f"- Judul: {b['judul']} Tahun: {b['tahun']}")

  Berfungsi untuk menampilkan data buku satu per satu.

# 5. Proses Sorting
- insertion_sort(data_buku)

  Untuk memanggil fungsi insertion sort untuk mengurutkan data.

# 6. Menampilkan Data Setelah Sorting
- print("\nData setelah diurutkan (berdasarkan tahun terbit):")

  Berfungsi untuk menampilkan judul setelah sorting.

- for b in data_buku:

  Berfungsi untuk membaca ulang data yang sudah terurut.

- print(f"- Judul: {b['judul']} Tahun: {b['tahun']}")

  Berfungsi untuk menampilkan hasil akhir.

# 7. Menjalankan Program
- if __name__ == "__main__":
    main()

  Kode ini memastikan bahwa fungsi main() dijalankan saat program dieksekusi.

  


# D. OUTPUT PROGRAM
<img width="496" height="252" alt="Screenshot 2026-05-04 183715" src="https://github.com/user-attachments/assets/617e1fc7-5de0-4614-b101-28d3042d0c8c" />



# Penjelasan Output
Output dari program ini menunjukkan alur proses mulai dari input data sampai hasil pengurutan. Di awal, pengguna diminta memasukkan jumlah buku yang ingin didata. Kalau yang dimasukkan bukan angka, program akan langsung memberi pesan kesalahan dan berhenti, jadi tidak terjadi error di bagian selanjutnya.

Setelah itu, pengguna diminta memasukkan data buku satu per satu, yaitu judul dan tahun terbit. Kalau saat memasukkan tahun terjadi kesalahan, misalnya mengetik huruf, program akan memberi peringatan dan meminta input ulang sampai benar. Dengan cara ini, data yang masuk tetap sesuai dan program bisa berjalan dengan lancar.
Setelah semua data dimasukkan, program akan menampilkan daftar buku sesuai urutan input. Di tahap ini, data masih belum diurutkan, jadi tampilannya mengikuti urutan saat dimasukkan oleh pengguna.

Selanjutnya, program menjalankan proses pengurutan menggunakan insertion sort. Setelah proses selesai, data ditampilkan kembali, tetapi kali ini sudah dalam kondisi terurut berdasarkan tahun terbit, dari yang paling lama sampai yang paling baru.

Kesimpulannya Program ini mengubah data yang awalnya acak jadi lebih rapi dan mudah dibaca. 
