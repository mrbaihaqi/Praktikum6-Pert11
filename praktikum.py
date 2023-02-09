x = {}

def tambah():
    print("\nTambah data")
    nama = input("Nama           : ")
    nim = int(input("NIM            : "))
    uts = int(input("Nilai UTS      : "))
    uas = int(input("Nilai UAS      : "))
    tugas = int(input("Nilai Tugas    : "))
    akhir = tugas*30/100 + uts*35/100 + uas*35/100
    x[nama] = nim, tugas, uts, uas, akhir

def tampilkan():
    if x.items():
        print("\nDaftar Nilai")
        print("="*78)
        print("|No. |      NAMA       |       NIM       |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
        print("="*78)
        i = 0
        for z in x.items():
            i += 1
            print("| {no:2d} | {0:15s}| {1:15d}  | {2:5d}   | {3:5d} |{4:6d} | {5:7.2f} |"
                    .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
        print("=" * 78)
    else:
        print("\nDaftar Nilai")
        print("="*78)
        print("|No. |      NAMA       |       NIM       |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
        print("="*78)
        print("|                                TIDAK ADA DATA                              |")
        print("="*78)
    
def hapus():
    print("\nHapus Data")
    nama = input("Masukan Nama    : ")
    if nama in x.keys():
        del x[nama]
        print()
        print("|====================================|")
        print("|       BERHASIL MENGHAPUS DATA      |")
        print("|====================================|")
    else:
        print("Nama {0} Tidak Ditemukan".format(nama))

def ubah():
    print("\nUbah Data")
    nama = input("Nama           : ")
    if nama in x.keys():
        del x[nama]
        nama = input("Nama           : ")
        nim = int(input("NIM            : "))
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        tugas = int(input("Nilai Tugas    : "))
        akhir = tugas*30/100 + uts*35/100 + uas*35/100
        x[nama] = nim, tugas, uts, uas, akhir
        print()
        print("|====================================|")
        print("|        BERHASIL MENGUBAH DATA      |")
        print("|====================================|")
    else:
        print("Nama {0} tidak ditemukan".format(nama))


print("Program Input Nilai")
print("="*19)
while True:
    c = input("\n(T)ambah, tampi(L)kan, (U)bah, (H)apus, (K)eluar: ")
    if c.lower() == 't':
        tambah()
    elif c.lower() == 'l':
        tampilkan()
    elif c.lower() == 'u':
        ubah()
    elif c.lower() == 'h':
        hapus()
    elif c. lower() == 'k':
        break
    else:
        print("Pilih menu yang tersedia")
