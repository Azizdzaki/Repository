from src.utility import monster_stats

def shop_management(item_shop_read, monster_shop_read, monster_read):
    print("\n>>> SHOP")
    print("\nSelamat datang kembali, Admin!\n")
    aksi = input(">>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
    while aksi!="5":
        while aksi!="1" and aksi!="2" and aksi!="3" and aksi!="4":
            print('Input tidak valid. Masukkan input sesuai nomor yang tersedia!')
            aksi = input(">>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
        if aksi=="1":
            lihat = input("\n>>> Mau lihat apa?\n1. Monster\n2. Potion\n>>> ")
            while lihat!='1' and lihat!='2':
                print('Input tidak valid. Masukkan input sesuai nomor yang tersedia!')
                lihat = input("\n>>> Mau lihat apa?\n1. Monster\n2. Potion\n>>> ")
            print()
            if lihat=="1":
                print("ID | Type           | ATK Power | DEF Power | HP  | Stok | Harga")
                width = [3,15,10,10,4,5,6]
                for i in range(len(monster_read)):
                    for j in range(1,len(monster_shop_read)):
                        if monster_read[i][0]==monster_shop_read[j][0]:
                            print("| ".join([f'{monster_read[i][k]: <{width[k]}}' for k in range(5)]+[f'{monster_shop_read[j][1]: <{width[5]}}',f'{monster_shop_read[j][2]: <{width[6]}}']))
                aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
            elif lihat=="2":
                print("Type       | Stok  | Harga")
                width = [11,6,6]
                for i in range(1,len(item_shop_read)):
                    print("| ".join([f'{item_shop_read[i][j]: <{width[j]}}' for j in range(3)]))
                aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
        elif aksi=='2':
            tambah = input("\n>>> Mau nambahin apa?\n1. Monster\n2. Potion\n>>> ")
            while tambah!='1' and tambah!='2':
                print('Input tidak valid. Masukkan input sesuai nomor yang tersedia!')
                tambah = input("\n>>> Mau nambahin apa?\n1. Monster\n2. Potion\n>>> ")
            print()
            if tambah=='1':
                all_monster_id_shop = [i[0] for i in monster_shop_read]
                width = [3,15,10,10,4]
                print("ID | Type           | ATK Power | DEF Power | HP")
                for i in range(1, len(monster_read)):
                    if monster_read[i][0] not in all_monster_id_shop:
                        print("| ".join([f'{monster_read[i][j]: <{width[j]}}' for j in range(5)]))
                monster_id_tambah = input("\n>>> Masukkan id monster: ")
                stock_monster_tambah = input(">>> Masukkan stok awal: ")
                price_monster_tambah = input(">>> Masukkan harga: ")
                monster_shop_read += [[monster_id_tambah,stock_monster_tambah,price_monster_tambah]]
                print(f"{monster_stats(monster_id_tambah,monster_read)[1]} telah berhasil ditambahkan ke dalam Shop!")
                aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
            elif tambah=='2':
                all_potion_type_shop = [i[0] for i in item_shop_read]
                print("Type")
                potion_type = ["strength", "resilience", "healing"]
                for i in range(3):
                    if potion_type[i] not in all_potion_type_shop:
                        print(f"{potion_type[i]}")
                potion_type_tambah = input("\n>>> Masukkan no tipe potion: ")
                if potion_type_tambah=='1':
                    potion_type_tambah = "strength"
                elif potion_type_tambah=='2':
                    potion_type_tambah = "resilience"
                elif potion_type_tambah=='3':
                    potion_type_tambah = "healing"
                stock_potion_tambah = input(">>> Masukkan stok awal: ")
                price_potion_tambah = input(">>> Masukkan harga: ")
                item_shop_read += [[potion_type_tambah,stock_potion_tambah,price_potion_tambah]]
                print(f"{potion_type_tambah} potion telah berhasil ditambahkan ke dalam Shop!")
                aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
        elif aksi=='3':
            ubah = input("\n>>> Mau ubah apa?\n1. Monster\n2. Potion\n>>> ")
            while ubah!='1' and ubah!='2':
                print('Input tidak valid. Masukkan input sesuai nomor yang tersedia!')
                ubah = input("\n>>> Mau ubah apa?\n1. Monster\n2. Potion\n>>> ")
            print()
            if ubah=="1":
                print("ID | Type           | ATK Power | DEF Power | HP  | Stok | Harga")
                width = [3,15,10,10,4,5,6]
                for i in range(len(monster_read)):
                    for j in range(1,len(monster_shop_read)):
                        if monster_read[i][0]==monster_shop_read[j][0]:
                            print("| ".join([f'{monster_read[i][k]: <{width[k]}}' for k in range(5)]+[f'{monster_shop_read[j][1]: <{width[5]}}',f'{monster_shop_read[j][2]: <{width[6]}}']))
                monster_id_ubah = input("\n>>> Masukkan id monster: ")
                stock_monster_ubah = input(">>> Masukkan stok baru: ")
                price_monster_ubah = input(">>> Masukkan harga baru: ")
                for i in range(len(monster_shop_read)):
                    if monster_shop_read[i][0]==monster_id_ubah:
                        if stock_monster_ubah != '':
                            monster_shop_read[i][1] = stock_monster_ubah
                        if price_monster_ubah != '':
                            monster_shop_read[i][2] = price_monster_ubah
                if stock_monster_ubah!='' and price_monster_ubah!='':
                    print(f"{monster_stats(monster_id_ubah,monster_read)[1]} telah berhasil diubah dengan stok baru sejumlah {stock_monster_ubah} dan dengan harga baru {price_monster_ubah} OC!")
                elif stock_monster_ubah!='' and price_monster_ubah=='':
                    print(f"{monster_stats(monster_id_ubah,monster_read)[1]} telah berhasil diubah dengan stok baru sejumlah {stock_monster_ubah}!")
                elif stock_monster_ubah=='' and price_monster_ubah!='':
                    print(f"{monster_stats(monster_id_ubah,monster_read)[1]} telah berhasil diubah dengan harga baru {price_monster_ubah} OC!")
                aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
            elif ubah=="2":
                print("Type       | Stok  | Harga")
                width = [11,6,6]
                for i in range(1,len(item_shop_read)):
                    print("| ".join([f'{item_shop_read[i][j]: <{width[j]}}' for j in range(3)]))
                potion_type_ubah = input("\n>>> Masukkan nomor tipe potion: ")
                if potion_type_ubah=='1':
                    potion_type_ubah = "strength"
                elif potion_type_ubah=='2':
                    potion_type_ubah = "resilience"
                elif potion_type_ubah=='3':
                    potion_type_ubah = "healing"
                stock_potion_ubah = input(">>> Masukkan stok baru: ")
                price_potion_ubah = input(">>> Masukkan harga baru: ")
                for i in range(len(item_shop_read)):
                    if item_shop_read[i][0]==potion_type_ubah:
                        if stock_potion_ubah != '':
                            item_shop_read[i][1] = stock_potion_ubah
                        if price_potion_ubah != '':
                            item_shop_read[i][2] = price_potion_ubah
                if stock_potion_ubah!='' and price_potion_ubah!='':
                    print(f"{potion_type_ubah} potion telah berhasil diubah dengan stok baru sejumlah {stock_potion_ubah} dan dengan harga baru {price_potion_ubah} OC!")
                elif stock_potion_ubah!='' and price_potion_ubah=='':
                    print(f"{potion_type_ubah} potion telah berhasil diubah dengan stok baru sejumlah {stock_potion_ubah}!")
                elif stock_potion_ubah=='' and price_potion_ubah!='':
                    print(f"{potion_type_ubah} potion telah berhasil diubah dengan harga baru {price_potion_ubah} OC!")
                aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
        elif aksi=='4':
            hapus = input("\n>>> Mau hapus apa?\n1. Monster\n2. Potion\n>>> ")
            while hapus!='1' and hapus!='2':
                print('Input tidak valid. Masukkan input sesuai nomor yang tersedia!')
                hapus = input("\n>>> Mau hapus apa?\n1. Monster\n2. Potion\n>>> ")
            print()
            if hapus=='1':
                print("ID | Type           | ATK Power | DEF Power | HP  | Stok | Harga")
                width = [3,15,10,10,4,5,6]
                for i in range(len(monster_read)):
                    for j in range(1,len(monster_shop_read)):
                        if monster_read[i][0]==monster_shop_read[j][0]:
                            print("| ".join([f'{monster_read[i][k]: <{width[k]}}' for k in range(5)]+[f'{monster_shop_read[j][1]: <{width[5]}}',f'{monster_shop_read[j][2]: <{width[6]}}']))
                monster_id_hapus = input("\n>>> Masukkan id monster: ")
                validasi = input(f">>> Apakah anda yakin ingin menghapus {monster_stats(monster_id_hapus,monster_read)[1]} dari Shop (y/n): ").lower()
                while validasi!='y' and validasi!='n':
                    print("Masukan tidak valid, coba lagi!")
                    validasi = input(f">>> Apakah anda yakin ingin menghapus {monster_stats(monster_id_hapus,monster_read)[1]} dari Shop (y/n): ").lower()
                if validasi=='y':
                    for i in range(len(monster_shop_read)):
                        if monster_shop_read[i][0]==monster_id_hapus:
                            del monster_shop_read[i]
                            break
                    print(f"Monster {monster_stats(monster_id_hapus,monster_read)[1]} telah berhasil dihapus dari Shop!")
                    aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
                elif validasi=='n':
                    print(f"Monster {monster_stats(monster_id_hapus,monster_read)[1]} gagal dihapus dari Shop!")
                    aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
            elif hapus=="2":
                print("Type       | Stok  | Harga")
                width = [11,6,6]
                for i in range(1,len(item_shop_read)):
                    print("| ".join([f'{item_shop_read[i][j]: <{width[j]}}' for j in range(3)]))
                potion_type_hapus = input("\nMasukkan nomor tipe potion: ")
                if potion_type_hapus=='1':
                    potion_type_hapus = "strength"
                elif potion_type_hapus=='2':
                    potion_type_hapus = "resilience"
                elif potion_type_hapus=='3':
                    potion_type_hapus = "healing"
                validasi = input(f">>> Apakah anda yakin ingin menghapus {potion_type_hapus} potion dari Shop (y/n): ").lower()
                while validasi!='y' and validasi!='n':
                    print("Masukan tidak valid, coba lagi!")
                    validasi = input(f">>> Apakah anda yakin ingin menghapus {monster_stats(monster_id_hapus,monster_read)[1]} dari Shop (y/n): ").lower()
                if validasi=='y':
                    for i in range(len(item_shop_read)):
                        if item_shop_read[i][0]==potion_type_hapus:
                            del item_shop_read[i]
                            break
                    print(f"{potion_type_hapus} potion telah berhasil dihapus dari Shop!")
                    aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
                elif validasi=='n':
                    print(f"{potion_type_hapus} gagal dihapus dari Shop!")
                    aksi = input("\n>>> Pilih aksi:\n1. Lihat\n2. Tambah\n3. Ubah\n4. Hapus\n5. Keluar\n>>> ")
    print("Sampai jumpa lagi Admin")
    print("\nKeluar ke menu utama...")
    return (item_shop_read,monster_shop_read)