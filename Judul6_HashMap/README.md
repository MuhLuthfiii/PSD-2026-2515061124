# A. Judul Program

Program Akun E-Wallet Menggunakan Hash Map (Separate Chaining)

# B. Deskripsi Singkat

Program ini dibuat untuk mensimulasikan pengelolaan akun pada sebuah aplikasi e-wallet. Setiap akun memiliki ID akun, nama pengguna, dan saldo. Pengguna dapat menambahkan akun baru, mencari akun berdasarkan ID, melakukan top up saldo, menghapus akun, serta menampilkan seluruh data akun yang tersimpan.

Program ini menerapkan struktur data Hash Map dengan metode Separate Chaining. Hash Map digunakan untuk mempercepat proses pencarian data berdasarkan ID akun. Jika terjadi collision atau dua data memiliki indeks hash yang sama, data tersebut tetap dapat disimpan menggunakan Linked List pada indeks yang sama sehingga tidak ada data yang hilang.

# C. Source Code
<img width="1248" height="8120" alt="code" src="https://github.com/user-attachments/assets/178a898c-701b-4a03-8b62-f487399a2ef4" />

# Penjelasan Source Code
# 1. Class Node
- class Node:

  Class Node digunakan untuk menyimpan data setiap akun e-wallet.

- def __init__(self, key, nama, saldo):

  Constructor yang dijalankan ketika objek node dibuat.

- self.key = key

  Menyimpan ID akun sebagai key.

- self.nama = nama

  Menyimpan nama pemilik akun.

- self.saldo = saldo

  Menyimpan saldo akun.

- self.next = None

  Digunakan untuk menghubungkan node lain apabila terjadi collision.
  
# 2. Class HashMapSeparateChaining
- class HashMapSeparateChaining:

  Class ini digunakan untuk mengelola seluruh proses penyimpanan dan pengolahan data pada Hash Map.

# 3. Constructor Hash Map
- def __init__(self, size=10):

  Digunakan untuk membuat Hash Map dengan ukuran default 10 indeks.

- self.SIZE = size

  Menyimpan ukuran Hash Map.

- self.table = [None] * self.SIZE

  Membuat tabel hash yang seluruh elemennya masih kosong.

# 4. Fungsi Hash
- def hash_function(self, key):

  Digunakan untuk menentukan posisi penyimpanan data.

- return (key % self.SIZE + self.SIZE) % self.SIZE

  Menghasilkan indeks berdasarkan ID akun.

# 5. Fungsi Insert
- def insert(self, key, nama, saldo):

  Digunakan untuk menambahkan akun baru ke dalam Hash Map.

- index = self.hash_function(key)

  Menentukan lokasi penyimpanan data.

- current = self.table[index]

  Mengambil node pertama pada indeks tersebut.

- while current is not None:

  Menelusuri Linked List apabila terdapat data pada indeks yang sama.

- if current.key == key:

  Mengecek apakah ID akun sudah ada.

- current.nama = nama
  current.saldo = saldo

  Jika ditemukan, data diperbarui.

- new_node = Node(key, nama, saldo)

  Membuat node baru.

- new_node.next = self.table[index]

  Menghubungkan node baru dengan node sebelumnya.

- self.table[index] = new_node

  Menyimpan node pada tabel hash.

# 6. Fungsi Search
- def search(self, key):

  Digunakan untuk mencari akun berdasarkan ID akun.

- index = self.hash_function(key)

  Menentukan lokasi pencarian.

- current = self.table[index]

  Mengambil node pertama pada indeks tersebut.

- while current is not None:

  Menelusuri Linked List.

- if current.key == key:

  Memeriksa apakah akun ditemukan.

- return current

  Mengembalikan data akun jika ditemukan.

- return None

  Dijalankan apabila akun tidak ditemukan.

# 7. Fungsi Top Up
- def topup(self, key, nominal):

  Digunakan untuk menambahkan saldo akun.

- akun = self.search(key)

  Mencari akun berdasarkan ID.

- akun.saldo += nominal

  Menambahkan nominal top up ke saldo akun.

# 8. Fungsi Withdraw
- def withdraw(self, key, nominal):

  Digunakan untuk mengurangi saldo akun.

- akun = self.search(key)

  Mencari akun berdasarkan ID.

- akun.saldo -= nominal

  Mengurangi saldo sesuai nominal yang dimasukkan.

# 9. Fungsi Remove
- def remove_key(self, key):

  Digunakan untuk menghapus akun dari Hash Map.

- current = self.table[index]

  Mengambil node pertama.

- prev = None

  Digunakan untuk menyimpan node sebelumnya.

- if current.key == key:

  Memeriksa apakah akun yang dicari ditemukan.

- self.table[index] = current.next

  Menghapus node pertama pada Linked List.

- prev.next = current.next

  Menghapus node yang berada di tengah atau akhir Linked List.

# 10. Fungsi Display
- def display(self):

  Digunakan untuk menampilkan seluruh data akun yang tersimpan.

- for i in range(self.SIZE):

  Menampilkan setiap indeks pada tabel hash.

- while current is not None:

  Menelusuri seluruh node pada Linked List.

# 11. Fungsi Main
- def main():

  Merupakan fungsi utama yang mengatur seluruh jalannya program.

- Program menyediakan menu:

1. Tambah Akun
2. Cari Akun
3. Top Up Saldo
4. Withdraw Saldo
5. Hapus Akun
6. Tampilkan Data
7. Keluar

  Setiap menu akan memanggil fungsi yang sesuai pada Hash Map sehingga pengguna dapat mengelola akun e-wallet dengan mudah.

# D. Ouput Program
<img width="250" height="485" alt="Screenshot 2026-06-09 215459" src="https://github.com/user-attachments/assets/cf643a7b-486d-4690-bbd1-da465556fed0" />
<img width="182" height="481" alt="Screenshot 2026-06-09 215516" src="https://github.com/user-attachments/assets/efabede9-586f-411f-8191-e5c7ef4899da" />
<img width="330" height="608" alt="Screenshot 2026-06-09 215532" src="https://github.com/user-attachments/assets/d0a76c8d-3272-4a89-9d3d-77040a5099a9" />
<img width="321" height="603" alt="Screenshot 2026-06-09 215545" src="https://github.com/user-attachments/assets/df5f59ef-bfc7-4aae-8227-55d55744c129" />
<img width="328" height="590" alt="Screenshot 2026-06-09 215559" src="https://github.com/user-attachments/assets/68eab0db-51f4-46d0-b752-c8d5db59b167" />
<img width="187" height="177" alt="Screenshot 2026-06-09 215607" src="https://github.com/user-attachments/assets/03b7da21-4505-4f0a-834a-0858b1076995" />


# Penjelasan Output

Saat program dijalankan, pengguna akan melihat menu utama yang berisi beberapa pilihan pengelolaan akun e-wallet. Pengguna dapat menambahkan akun baru dengan memasukkan ID akun, nama pemilik akun, dan saldo awal. Setelah data berhasil dimasukkan, sistem akan menyimpan akun tersebut ke dalam Hash Map dan menampilkan pesan bahwa akun berhasil ditambahkan.

Ketika menu pencarian digunakan, program akan meminta ID akun yang ingin dicari. Jika akun ditemukan, sistem akan menampilkan informasi lengkap berupa ID akun, nama pemilik akun, dan saldo yang dimiliki. Sebaliknya, jika ID yang dimasukkan tidak terdaftar, program akan menampilkan pesan bahwa data tidak ditemukan.

Pada menu top up, pengguna dapat menambahkan saldo ke akun yang sudah ada. Setelah nominal dimasukkan, saldo akun akan bertambah sesuai jumlah top up yang dilakukan. kebalikan dari top up, pada menu withdraw pengguna dapat mengambil saldo mereka yang ada dalam akun. Pengguna akan menginputkan nomilan, kemudai saldo akun akan berkurang sesuai jumlah withdraw yang dilakukan

Menu hapus akun digunakan pengguna untuk menghapus data akun dari sistem. Jika akun berhasil ditemukan, data akun akan dihapus dari program Hash Map dan program akan menampilkan pesan bahwa akun berhasil dihapus. Sebaliknya, jika data akun tidak ditemukan, maka program otomatis akan memberi tahu pengguna bahwa data akun tidak ditemukan, sehingga proses menghapus akun tidak dapat dilakukan

Menu tampilkan data digunakan untuk melihat seluruh akun yang tersimpan. Output yang ditampilkan memperlihatkan bagaimana data disimpan pada masing-masing indeks Hash Map. Jika terjadi collision, beberapa akun akan muncul dalam satu indeks yang sama dan dihubungkan menggunakan metode Separate Chaining. Hal ini menunjukkan bahwa Hash Map tetap dapat menyimpan seluruh data dengan baik meskipun terdapat indeks yang sama.

Dan terakhir menu keluar digunakan oleh pengguna jika mereka ingin mengakhiri program
