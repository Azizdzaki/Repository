from src.utility import monster_stats, isDigit

def shop(user_id_now,user_oc_now,user_read,monster_read,monster_shop_read,item_shop_read,monster_inventory_read,item_inventory_read):
    print("\n>>> SHOP")
    print("\n======== Selamat datang di SHOP!! ========")
    aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
    while aksi != '3':
        while aksi!='1' and aksi!='2':
            print('Input tidak valid. Masukkan input sesuai nomor yang tersedia!')
            aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
        print()
        if aksi=='1':
            lihat = input(">>> Mau lihat apa?\n1. Lihat monster\n2. Lihat potion\n>>> ")
            while lihat!='1'and lihat!='2':
                print('Input tidak valid. Masukkan input sesuai nomor yang tersedia!\n')
                lihat = input(">>> Mau lihat apa?\n1. Lihat monster\n2. Lihat potion\n>>> ")
            print()
            if lihat=='1':
                print("ID | Type           | ATK Power | DEF Power | HP  | Stok | Harga")
                width = [3,15,10,10,4,5,6]
                for i in range(1,len(monster_read)):
                    for j in range(1,len(monster_shop_read)):
                        if monster_read[i][0]==monster_shop_read[j][0]:
                            print("| ".join([f'{monster_read[i][k]: <{width[k]}}' for k in range(5)]+[f'{monster_shop_read[j][1]: <{width[5]}}',f'{monster_shop_read[j][2]: <{width[6]}}']))
                aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
            elif lihat=='2':
                print("Type       | Stok  | Harga")
                width = [11,6,6]
                for i in range(1,len(item_shop_read)):
                    print("| ".join([f'{item_shop_read[i][j]: <{width[j]}}' for j in range(3)]))
                aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
        elif aksi=='2':
            print(f"Jumlah O.W.C.A Coin-mu sekarang {user_oc_now}\n")
            beli = input(">>> Mau beli apa?\n1. Beli monster\n2. Beli potion\n>>> ")
            while beli!='1'and beli!='2':
                print('Input tidak valid. Masukkan input sesuai nomor yang tersedia!\n')
                beli = input(">>> Mau beli apa?\n1. Beli monster\n2. Beli potion\n>>> ")
            print()
            if beli=='1':
                monster_id_buy = input(">>> Masukkan ID monster: ")
                all_monster_id_shop = [i[0] for i in monster_shop_read]
                all_monster_id_inventory = []
                for i in range(len(monster_inventory_read)):
                    if monster_inventory_read[i][0]==user_id_now:
                        all_monster_id_inventory += [monster_inventory_read[i][1]]
                if monster_id_buy not in all_monster_id_shop:
                    print("\nMonster tidak tersedia di Shop!")
                    aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
                else:
                    for i in range(len(monster_shop_read)):
                        if monster_id_buy==monster_shop_read[i][0]:
                            if int(user_oc_now)<int(monster_shop_read[i][2]):
                                print(f"OC-mu tidak cukup untuk membeli monster {monster_stats(monster_id_buy,monster_read)[1]}.")
                                aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
                            elif monster_id_buy in all_monster_id_inventory:
                                print(f"Monster {monster_stats(monster_id_buy,monster_read)[1]} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
                                aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
                            else:
                                monster_inventory_read += [[user_id_now,monster_id_buy,'1']]
                                monster_shop_read[i][1] = str(int(monster_shop_read[i][1])-1)
                                for j in range(len(user_read)):
                                    if user_read[j][0]==user_id_now:
                                        user_read[j][4] = str(int(user_oc_now)-int(monster_shop_read[i][2]))
                                print(f"Berhasil membeli monster {monster_stats(monster_id_buy,monster_read)[1]}. Monster sudah masuk ke inventory-mu!.")
                                aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
            elif beli=='2':
                all_item_type_inventory = []
                for j in item_inventory_read:
                    if j[0]==user_id_now:
                        all_item_type_inventory += [j[1]]
                potion_type_buy = input("1. Strength     2. Resillence     3. Healing\n>>> Masukkan nomor tipe potion: ")
                while potion_type_buy!='1' and potion_type_buy!='2' and potion_type_buy!='3':
                    print("Masukkan tidak valid, masukkan nomor tipe potion yang tersedia!")
                    potion_type_buy = input("\n1. Strength     2. Resillence     3. Healing\n>>> Masukkan nomor tipe potion: ")
                if potion_type_buy == '1' :
                    potion_type_buy = 'strength'
                elif potion_type_buy == '2' :
                    potion_type_buy = 'resilience'
                elif potion_type_buy == '3' :
                    potion_type_buy = 'healing'
                quantity = input('>>> Masukkan jumlah pembelian : ')
                while not isDigit(quantity):
                    print("Masukan tidak valid, coba lagi!")
                    quantity = input('>>> Masukkan jumlah pembelian : ')
                for i in range(1, len(item_shop_read)):           
                    if potion_type_buy == item_shop_read[i][0] :
                        if item_shop_read[i][1] != '0' :
                            while int(quantity) > int(item_shop_read[i][1]) :
                                print('Jumlah pembelian melebihi batas stock yang tersedia!')
                                quantity = input('>>> Masukkan jumlah pembelian : ')
                                while not isDigit(quantity):
                                    print("Masukan tidak valid, coba lagi!")
                                    quantity = input('>>> Masukkan jumlah pembelian : ')
                            invoice = int(quantity)*(int(item_shop_read[i][2]))
                            if invoice > user_oc_now :
                                print('OC-mu tidak cukup')
                                aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
                            else :
                                print(f"Berhasil membeli item: {quantity} {potion_type_buy} potion. Item sudah masuk inventory-mu!")
                                item_shop_read[i][1] = str(int(item_shop_read[i][1]) - int(quantity))
                                for j in range(len(user_read)):
                                    if user_read[j][0]==user_id_now:
                                        user_read[j][4] = str(int(user_oc_now)-invoice)
                                if potion_type_buy not in all_item_type_inventory:
                                    item_inventory_read += [[user_id_now,potion_type_buy,quantity]]
                                else:
                                    for i in range(len(item_inventory_read)):
                                        if item_inventory_read[i][0]==user_id_now and item_inventory_read[i][1]==potion_type_buy:
                                            item_inventory_read[i][2]=str(int(item_inventory_read[i][2])+int(quantity))
                                aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
                        else :
                            print('Sayang sekali, potion sedang tidak tersedia di Shop!')
                            aksi = input('\n>>> Pilih perintah: \n1. Lihat\n2. Beli\n3. Keluar\n>>> ')
    print("\nKeluar ke menu utama...")
    return (monster_inventory_read,item_inventory_read,monster_shop_read,item_shop_read,user_read)