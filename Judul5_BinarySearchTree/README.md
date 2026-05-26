# A. Judul Program
Sistem Pendataan Kendaraan Parkir Menggunakan Binary Search Tree (BST)

# B. Deskripsi Singkat

Program ini dibuat untuk membantu pengelolaan data kendaraan pada area parkir menggunakan struktur data Binary Search Tree (BST). Sistem dapat digunakan untuk menambahkan nomor kendaraan yang masuk, mencari data kendaraan tertentu, menampilkan seluruh data kendaraan secara urut, dan menghapus data kendaraan yang sudah keluar dari area parkir.

Penggunaan BST membuat proses pencarian kendaraan menjadi lebih cepat dibanding pencarian biasa. Data kendaraan akan disusun secara otomatis berdasarkan nilainya. Nomor kendaraan yang lebih kecil ditempatkan di sebelah kiri node, sedangkan nomor yang lebih besar ditempatkan di sebelah kanan node. Dengan susunan seperti ini, data menjadi lebih rapi dan mudah dikelola.

# C. Source Code
<img width="1432" height="5194" alt="code" src="https://github.com/user-attachments/assets/07396e79-7d18-4d3f-92f6-d2e9c004d324" />


# Penjelasan Kode
# 1. Class Node
- class Node:

  Baris ini digunakan untuk membuat class Node. Node merupakan bagian utama pada Binary Search Tree yang digunakan untuk menyimpan data kendaraan.

- def __init__(self, data):

  Constructor digunakan untuk menerima data saat node dibuat.

- self.data = data

  Digunakan untuk menyimpan nomor kendaraan ke dalam node.

- self.left = None
  self.right = None

  Variabel left digunakan untuk menyimpan child kiri, sedangkan right digunakan untuk menyimpan child kanan. Nilai awal None berarti node belum memiliki child.

# 2. Class BinarySearchTree
- class BinarySearchTree:

  Class utama yang digunakan untuk menjalankan seluruh operasi Binary Search Tree.

- def __init__(self):

  Constructor pada class BST.

- self.root = None

  Variabel root digunakan sebagai node utama pada tree. Nilai awal None berarti tree masih kosong.

# 3. Fungsi Insert
- def insert(self, root, data):

  Fungsi insert() digunakan untuk menambahkan data kendaraan ke dalam BST.

- if root is None:
    return Node(data)

  Jika tree masih kosong, maka program akan membuat node baru.

- if data < root.data:

  Jika data lebih kecil dari root, data akan ditempatkan di subtree kiri.

- root.left = self.insert(root.left, data)

  Melakukan proses insert secara rekursif ke bagian kiri tree.

- elif data > root.data:

  Jika data lebih besar dari root, data akan ditempatkan di subtree kanan.

- root.right = self.insert(root.right, data)

  Melakukan proses insert secara rekursif ke bagian kanan tree.

- return root

  Mengembalikan root setelah proses penambahan data selesai.

# 4. Fungsi Search
- def search(self, root, key):

  Fungsi search() digunakan untuk mencari nomor kendaraan tertentu.

- if root is None:
    return False

  Jika node kosong, berarti data tidak ditemukan.

- if root.data == key:
    return True

  Jika data pada node sama dengan data yang dicari, maka program mengembalikan nilai True.

- if key < root.data:

  Jika data yang dicari lebih kecil dari root, pencarian dilanjutkan ke subtree kiri.

- return self.search(root.left, key)

  Melakukan pencarian secara rekursif pada bagian kiri tree.

- return self.search(root.right, key)

  Jika data lebih besar, pencarian dilakukan ke subtree kanan.

# 5. Fungsi Inorder
- def inorder(self, root):

  Fungsi inorder() digunakan untuk menampilkan data kendaraan secara urut.

- if root:

  Mengecek apakah node masih ada.

- self.inorder(root.left)

  Traversal dilakukan terlebih dahulu ke subtree kiri.

- print(root.data, end=" ")

  Menampilkan data kendaraan pada node.

- self.inorder(root.right)

  Traversal dilanjutkan ke subtree kanan.

# 6. Fungsi Find Minimum
- def find_min(self, root):

  Fungsi ini digunakan untuk mencari nilai terkecil pada subtree kanan saat proses delete.

- current = root

  Variabel current digunakan untuk menelusuri node.

- while current.left is not None:

  Perulangan dilakukan selama masih ada child kiri.

- current = current.left

  Berpindah ke node paling kiri karena node paling kiri memiliki nilai terkecil.

- return current

  Mengembalikan node dengan nilai terkecil.

# 7. Fungsi Delete
- def delete(self, root, key):

  Fungsi delete() digunakan untuk menghapus data kendaraan dari BST.

- if root is None:
    return root

  Jika tree kosong, tidak ada data yang dapat dihapus.

- if key < root.data:

  Jika data yang ingin dihapus lebih kecil dari root, proses dilanjutkan ke subtree kiri.

- root.left = self.delete(root.left, key)

  Menghapus data secara rekursif pada subtree kiri.

- elif key > root.data:

  Jika data lebih besar dari root, proses dilanjutkan ke subtree kanan.

- root.right = self.delete(root.right, key)

  Menghapus data secara rekursif pada subtree kanan.

- if root.left is None:
    return root.right

  Jika node tidak memiliki child kiri, maka node kanan akan menggantikan posisi node yang dihapus.

- elif root.right is None:
    return root.left

  Jika node tidak memiliki child kanan, maka node kiri akan menggantikan posisi node yang dihapus.

- temp = self.find_min(root.right)

  Mencari nilai terkecil pada subtree kanan untuk menggantikan node yang dihapus.

- root.data = temp.data

  Mengganti data node yang dihapus dengan data pengganti.

- root.right = self.delete(root.right, temp.data)

  Menghapus node pengganti yang sebelumnya dipindahkan.

- return root

  Mengembalikan root setelah proses penghapusan selesai.

# 8. Program Utama
- def main():

  Fungsi utama program.

- bst = BinarySearchTree()

  Membuat objek BST.

- pilih = 0

  Variabel untuk menyimpan pilihan menu.

- while pilih != 5:

  Perulangan program akan terus berjalan sampai pengguna memilih menu keluar.

- print("\n=== SISTEM PARKIR KENDARAAN ===")

  Menampilkan judul program.

- pilih = int(input("Pilih menu: "))

  Digunakan untuk menerima input pilihan menu dari pengguna.

- nomor = int(input("Masukkan nomor kendaraan: "))

  Digunakan untuk menerima input nomor kendaraan.

- bst.root = bst.insert(bst.root, nomor)

  Menambahkan nomor kendaraan ke dalam BST.

- if bst.search(bst.root, cari):

  Mengecek apakah data kendaraan ditemukan.

- bst.inorder(bst.root)

  Menampilkan seluruh data kendaraan secara urut.

- bst.root = bst.delete(bst.root, hapus)

  Menghapus data kendaraan dari BST.

- if __name__ == "__main__":
    main()

  Digunakan agar fungsi main() dijalankan saat program dieksekusi.


# D. Output Program
<img width="252" height="690" alt="Screenshot 2026-05-26 212056" src="https://github.com/user-attachments/assets/48697014-02ee-48f0-a99a-b5bfca9585e4" />
<img width="315" height="661" alt="Screenshot 2026-05-26 212122" src="https://github.com/user-attachments/assets/23509ac0-994a-43a4-b507-1bae10b01a20" />
<img width="238" height="146" alt="Screenshot 2026-05-26 212131" src="https://github.com/user-attachments/assets/7586f513-f8f9-4736-ad70-1ea8c2728fd5" />

# Penjelasan Output
Pada output program, petugas parkir memasukkan beberapa nomor kendaraan yang masuk ke area parkir, yaitu 2789, 2456, 4016, dan 6972. Setelah data dimasukkan, sistem langsung menyusun data sesuai aturan Binary Search Tree. Nomor yang lebih kecil ditempatkan di sebelah kiri node, sedangkan nomor yang lebih besar ditempatkan di sebelah kanan.

Saat menu “Tampilkan Kendaraan” dipilih, sistem menampilkan seluruh nomor kendaraan secara urut dari kecil ke besar, yaitu 2456, 2789, 4016, 6972. Hal ini dilakukan menggunakan traversal inorder pada BST.

Kemudian petugas mencoba mencari kendaraan dengan nomor 4016 dan sistem berhasil menemukannya. Karena BST menyusun data secara terstruktur, proses pencarian menjadi lebih cepat dibanding harus memeriksa data satu per satu.

Selanjutnya kendaraan dengan nomor 2456 keluar dari area parkir sehingga datanya dihapus dari sistem. Setelah data ditampilkan kembali, daftar kendaraan berubah menjadi 2789, 4016, dan 6972. Sistem tetap mempertahankan susunan data agar tetap rapi dan terurut.

Dan yang terakhir, ketika petugas memilih menu selesai, maka program secara otomatis akan berhenti.

# E. Link Youtube


