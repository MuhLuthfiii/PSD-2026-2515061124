def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j]["tahun"] > key["tahun"]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key


def main():
    data_buku = []
    try:
        n = int(input("Masukkan jumlah buku: "))
    except ValueError:
        print("Input hanya berupa angka")
        return
    for i in range(n):
        while True:
            try:
                judul = input(f"Judul buku ke-{i+1}: ")
                tahun = int(input("Tahun terbit: "))
                data_buku.append({
                    "judul": judul,
                    "tahun": tahun
                })
                break
            except ValueError:
                print("Input tidak valid, silahkan masukkan kembali")

    print("\nData sebelum diurutkan:")
    for b in data_buku:
        print(f"- Judul: {b['judul']}, Tahun: {b['tahun']}")
    insertion_sort(data_buku)
    print("\nData setelah diurutkan (berdasarkan tahun terbit):")
    for b in data_buku:
        print(f"- Judul: {b['judul']}, Tahun: {b['tahun']}")

if __name__ == "__main__":
    main()