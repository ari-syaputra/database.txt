
def simpan_biodata():
    nama = input("Masukan Nama           : ")
    tgl = input("Masukan Tanggal Lahir   : ")
    asal = input("Masukan Asal Daerah    : ")

    with open("database.txt", "a") as f:
        f.write(f"Nama           : {nama}\n")
        f.write(f"Tanggal Lahir  : {tgl}\n")
        f.write(f"Asal Daerah    : {asal}\n")
        f.write("-" * 30 + "\n")  

    print("\n--- Biodata berhasil disimpan! ---\n")

def tampilkan_data():
    with open("database.txt", "r") as f:
        isi = f.read()   
    print("\n===== SEMUA BIODATA =====")
    print(isi)
    print("==========================\n")

def menu():
    print("===== MENU UTAMA =====")
    print("1. Menyimpan Biodata")
    print("2. Tampilkan Semua Biodata")
    print("3. Mengahapus Biodata")
    print("4. Mengganti Biodata")
    print("5. Keluar Program")
    try:
        return int(input("Masukkan pilihan: "))
    except:
        return 0   

def hapus_data():
    nama_target = input("Masukkan nama yang ingin dihapus: ")

    with open("database.txt", "r") as f:
        lines = f.readlines()

    new_lines = []
    skip = False 
    for i in range(len(lines)):
        line = lines[i]

        if line.startswith("Nama") and nama_target.lower() in line.lower():
            skip = True
            continue

        if skip:
            if line.startswith("------------------------------"):
                skip = False
            continue

        new_lines.append(line)

    with open("database.txt", "w") as f:
        f.writelines(new_lines)

    print(f"\n--- Data '{nama_target}' berhasil dihapus! ---\n")

def ganti_data():
    target = input("Masukkan nama yang datanya ingin diganti: ")

    with open("database.txt", "r") as f:
        lines = f.readlines()

    new_lines = []
    found = False
    skip = False

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("Nama") and target.lower() in line.lower():
            found = True
            skip = True
            i += 4   
            continue

        if not skip:
            new_lines.append(line)
        else:
            skip = False

        i += 1

    if not found:
        print(f"\n--- Data '{target}' tidak ditemukan! ---\n")
        return

    print("\nMasukkan data baru:")
    nama_baru = input("Nama Baru           : ")
    tgl_baru = input("Tanggal Lahir Baru  : ")
    asal_baru = input("Asal Daerah Baru    : ")

    new_lines.append(f"Nama            : {nama_baru}\n")
    new_lines.append(f"Tanggal Lahir   : {tgl_baru}\n")
    new_lines.append(f"Asal Daerah     : {asal_baru}\n")
    new_lines.append("-" * 30 + "\n")

    with open("database.txt", "w") as f:
        f.writelines(new_lines)

    print(f"\n--- Data '{target}' berhasil diganti! ---\n")


pilihan = menu()

while pilihan < 5:  
    if pilihan == 1:
        simpan_biodata()
    elif pilihan == 2:
        tampilkan_data()
    elif pilihan == 3:
        hapus_data()
    elif pilihan == 4:
        ganti_data()
    else:
        print("\n--- Pilihan tidak valid! ---\n")

    pilihan = menu()  

print("\nProgram selesai, terima kasih!\n")
