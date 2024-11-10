from src.utility import isDigit

def monster_management(monster_read):
    print("\n>>> MONSTER\n")
    print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!")
    print("1. Tampilkan semua Monster")
    print("2. Tambah Monster baru")
    print("3. Keluar")

    aksi = input("\n>>> Pilih Aksi : ")
    while aksi != '3':
        while aksi!='1' and aksi!='2':
            print("Input tidak valid, Masukkan input sesuai nomor yang tersedia!")
            aksi = input("\n>>> Pilih Aksi : ")
        if aksi=='1':
            width = [3,15,10,10,3]
            for i in range(len(monster_read)):
                print("| ".join([f'{monster_read[i][j]: <{width[j]}}' for j in range(5)]))  
            aksi = input("\n>>> Pilih Aksi : ")
        elif aksi=='2':
            print("Memulai pembuatan monster baru")
            type_monster = [i[1] for i in monster_read]
            type_monster_new = input(">>> Masukkan Type / Nama : ")
            if type_monster_new in type_monster:
                print("Nama sudah terdaftar, coba lagi!")
            else:
                atk_power_new = input(">>> Masukkan ATK Power : ")
                while not isDigit(atk_power_new):
                    print("Masukkan input bertipe Integer, coba lagi!")
                    atk_power_new = input(">>> Masukkan ATK Power : ")
                def_power_new = input(">>> Masukkan DEF Power (0-50) : ")
                while not isDigit(def_power_new):
                    print("Masukkan input bertipe Integer, coba lagi!\n")
                    def_power_new = input(">>> Masukkan DEF Power (0-50) : ")
                while int(def_power_new)<0 or int(def_power_new)>50:
                    print("DEF Power harus bernilai 0-50, coba lagi!")
                    def_power_new = input(">>> Masukkan DEF Power (0-50) : ")
                    while not isDigit(def_power_new):
                        print("Masukkan input bertipe Integer, coba lagi!")
                        def_power_new = input(">>> Masukkan DEF Power (0-50) : ")
                hp_new = input(">>> Masukkan HP : ")
                while not isDigit(hp_new):
                    print("Masukkan input bertipe Integer, coba lagi!")
                    hp_new = input(">>> Masukkan HP : ")

                print("\nMonster baru berhasil dibuat!")
                print(f"Type : {type_monster_new}")
                print(f"ATK Power : {atk_power_new}")
                print(f"DEF Power : {def_power_new}")
                print(f"HP : {hp_new}")
                validasi = input("\n>>> Tambahkan Monster ke database (y/n) : ").lower()
                while validasi!='y' and validasi!='n':
                    print("Masukan tidak valid, coba lagi!")
                    validasi = input("\n>>> Tambahkan Monster ke database (y/n) : ")
                if validasi=='y':
                    monster_id = str(len(monster_read))
                    monster_read += [[monster_id,type_monster_new,str(atk_power_new),str(def_power_new),str(hp_new)]]
                    print("Monster baru telah ditambahkan!")
                elif validasi=='n':
                    print("Monster gagal ditambahkan!")
            aksi = input("\n>>> Pilih Aksi : ")
    print("\nKeluar ke menu utama...")
    return(monster_read)