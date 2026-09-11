# SISTEM PENGELOLAAN DATA GAJI KARYAWAN
data_gaji_karyawan = []

while True:
    print("SISTEM PENGELOLAAN DATA GAJI KARYAWAN")
    print("1. tambah data")
    print("2. tampilkan data")
    print("3. ubah data")
    print("4. hapus data")
    print("5. keluar")

    pilihan = input("pilih menu: ")

    if pilihan == "1":
        nama = input("nama karyawan: ")
        golongan = input("golongan (A/B/C/D/E): ")

        if golongan in ["A", "B", "C", "D", "E"]:
            gaji = int(input("gaji: "))
            data_gaji_karyawan.append([nama, golongan, gaji])
            print("data berhasil ditambahkan.")
        else:
            print("golongan tidak valid.")

    elif pilihan == "2":
        if len(data_gaji_karyawan) == 0:
            print("belum ada data karyawan.")
        else:
            print("DATA GAJI KARYAWAN")
            for data in data_gaji_karyawan:
                print("Nama     :", data[0])
                print("Golongan :", data[1])
                print("Gaji     : Rp", data[2])

    elif pilihan == "3":
        nama = input("masukkan nama yang ingin diubah: ")
        ditemukan = False

        for data in data_gaji_karyawan:
            if data[0] == nama:
                data[0] = input("nama baru: ")
                data[1] = input("golongan baru (A/B/C/D/E): ")
                data[2] = int(input("gaji baru: "))

                print("data berhasil diubah.")
                ditemukan = True
                break

        if not ditemukan:
            print("data tidak ditemukan.")

    elif pilihan == "4":
        nama = input("masukkan nama yang ingin dihapus: ")
        ditemukan = False

        for data in data_gaji_karyawan:
            if data[0] == nama:
                data_gaji_karyawan.remove(data)
                print("data berhasil dihapus.")
                ditemukan = True
                break

        if not ditemukan:
            print("data tidak ditemukan.")

    elif pilihan == "5":
        print("program selesai.")
        break

    else:
        print("pilihan menu tidak tersedia.")