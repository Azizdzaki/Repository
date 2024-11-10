from src.utility import isDigit

def laboratory(user_id_now,user_oc_now,monster_read, monster_inventory_read, user_read):
    all_user_id = [i[0] for i in monster_inventory_read]
    all_monster_id = [i[1] for i in monster_inventory_read]
    all_level_monster = [i[2] for i in monster_inventory_read]
    all_monster_name = [i[1] for i in monster_read]

    print("\n>>> LABORATORY")
    print("\n============ MONSTER LIST ============")
    count_monster = 0
    monster_list = []
    for i in range(len(all_user_id)):
        if all_user_id[i] == user_id_now:
            count_monster += 1
            monster_list.append([count_monster,all_monster_name[i],all_level_monster[i],all_monster_id[i]])
    
    for i in monster_list:
        print(f"{i[0]}. {i[1]} (Level: {i[2]})")

    print("\n============ UPGRADE PRICE ============")
    print("1. Level 1 -> Level 2: 300 OC")
    print("2. Level 2 -> Level 3: 500 OC")
    print("3. Level 3 -> Level 4: 800 OC")
    print("4. Level 4 -> Level 5: 1000 OC")
    upgrade_price = [300,500,800,1000]
    print()
    upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
    while not isDigit(upgrade_monster):
        print("Masukan tidak valid, pilih nomor yang tersedia!")
        upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
    while int(upgrade_monster)>count_monster:
        print("Masukkan input sesuai nomor monster yang tersedia, coba lagi!")
        upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
        while not isDigit(upgrade_monster):
            print("Masukan tidak valid, pilih nomor yang tersedia!")
            upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
    while upgrade_monster != '0':
        for i in monster_list:
            if (i[0])==int(upgrade_monster):
                if int(i[2])<5:
                    print(f"{i[1]} akan di-upgrade ke level {int(i[2])+1}.")
                    print(f"Harga untuk melanjutkan upgrade {i[1]} adalah {upgrade_price[int(i[2])-1]}")
                    validasi = input("\n>>> Lanjutkan upgrade (y/n): ").lower()
                    while validasi!='y' and validasi!='n':
                        print("Masukan tidak valid, coba lagi!")
                        validasi = input("\n>>> Lanjutkan upgrade (y/n): ").lower()
                    if validasi=='y':
                        if user_oc_now >= upgrade_price[int(i[2])-1]:
                            for j in range(len(user_read)):
                                if user_read[j][0]==user_id_now:
                                    user_read[j][4] = str(int(user_oc_now)-upgrade_price[int(i[2])-1])
                            for j in monster_inventory_read:
                                if j[0]==user_id_now and j[1]==i[3]:
                                    j[2]=str(int(i[2])+1)
                            print(f"Selamat, {i[1]} berhasil di-upgrade ke level {int(i[2])+1}!")
                            upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                            while not isDigit(upgrade_monster):
                                print("Masukan tidak valid, pilih nomor yang tersedia!")
                                upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                            while int(upgrade_monster)>count_monster:
                                print("Masukkan input sesuai nomor monster yang tersedia, coba lagi!")
                                upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                                while not isDigit(upgrade_monster):
                                    print("Masukan tidak valid, pilih nomor yang tersedia!")
                                    upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                        else:
                            print("OC anda tidak cukup untuk melakukan upgrade")
                            upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                            while not isDigit(upgrade_monster):
                                print("Masukan tidak valid, pilih nomor yang tersedia!")
                                upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                            while int(upgrade_monster)>count_monster:
                                print("Masukkan input sesuai nomor monster yang tersedia, coba lagi!")
                                upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                                while not isDigit(upgrade_monster):
                                    print("Masukan tidak valid, pilih nomor yang tersedia!")
                                    upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                    elif validasi=='n':
                        print(f"{i[1]} gagal di-upgrade")
                        upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                        while not isDigit(upgrade_monster):
                            print("Masukan tidak valid, pilih nomor yang tersedia!")
                            upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                        while int(upgrade_monster)>count_monster:
                            print("Masukkan input sesuai nomor monster yang tersedia, coba lagi!")
                            upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                            while not isDigit(upgrade_monster):
                                print("Masukan tidak valid, pilih nomor yang tersedia!")
                                upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                else:
                    print("Maaf, monster yang Anda pilih sudah memiliki level maksimum")
                    upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                    while not isDigit(upgrade_monster):
                        print("Masukan tidak valid, pilih nomor yang tersedia!")
                        upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                    while int(upgrade_monster)>count_monster:
                        print("Masukkan input sesuai nomor monster yang tersedia, coba lagi!")
                        upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
                        while not isDigit(upgrade_monster):
                            print("Masukan tidak valid, pilih nomor yang tersedia!")
                            upgrade_monster = input(">>> Pilih monster (0 untuk keluar): ")
    print("\nKeluar ke menu utama...")
    return (monster_inventory_read, user_read)