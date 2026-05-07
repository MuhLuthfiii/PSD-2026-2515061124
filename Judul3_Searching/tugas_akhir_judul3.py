def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j]["tahun"] > key["tahun"]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key


def sequential_search_sentinel(data, n, target):
    data.append({
        "judul": target,
        "tahun": 0
    })

    i = 0

    while data[i]["judul"].lower() != target.lower():
        i += 1

    data.pop()

    if i < n:
        return True, i
    else:
        return False, -1


def main():
    data_buku = []

    try:
        n = int(input("Masukkan jumlah buku: "))
    except ValueError:
        print("Input tidak valid!")
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
                print("Input tidak valid!")

    print("\nData sebelum diurutkan:")
    for b in data_buku:
        print(f"- {b['judul']} ({b['tahun']})")

    insertion_sort(data_buku)

    print("\nData setelah diurutkan:")
    for b in data_buku:
        print(f"- {b['judul']} ({b['tahun']})")

    while True :
        cari = input("\nMasukkan judul buku yang dicari: ")
        found, index = sequential_search_sentinel(data_buku, n, cari)
        if found:
            print(f"\nbuku ditemukan pada indeks ke-{index}")
            print(f"Judul : {data_buku[index]['judul']}")
            print(f"Tahun : {data_buku[index]['tahun']}")
            break
        
        else:
            print("\nBuku tidak terdaftar, silahkan cari kembali")


if __name__ == "__main__":
    main()