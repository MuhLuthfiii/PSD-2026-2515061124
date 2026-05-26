class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def find_min(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)

            root.data = temp.data

            root.right = self.delete(root.right, temp.data)

        return root


def main():
    bst = BinarySearchTree()

    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM PARKIR KENDARAAN ===")
        print("1. Tambah Kendaraan")
        print("2. Cari Kendaraan")
        print("3. Tampilkan Kendaraan")
        print("4. Hapus Kendaraan")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nomor = int(input("Masukkan nomor kendaraan: "))
            bst.root = bst.insert(bst.root, nomor)
            print("Kendaraan berhasil ditambahkan")

        elif pilih == 2:
            cari = int(input("Masukkan nomor kendaraan yang dicari: "))

            if bst.search(bst.root, cari):
                print("Kendaraan ditemukan")
            else:
                print("Kendaraan tidak ditemukan")

        elif pilih == 3:
            print("Daftar kendaraan:", end=" ")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            hapus = int(input("Masukkan nomor kendaraan yang keluar: "))
            if bst.search(bst.root, hapus):
                bst.root = bst.delete(bst.root, hapus)
                print("Kendaraan berhasil dihapus")
            else:
                print("Nomor kendaraan tidak ditemukan")

        elif pilih == 5:
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()