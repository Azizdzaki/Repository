from src.utility import monster_inventory_stats, isDigit

def inventory(user_id_now,user_oc_now,monster_inventory_read, item_inventory_read, monster_read):
    inventory_list = []

    print("\n>>> INVENTORY\n")
    print(f"============ INVENTORY LIST (User ID: {user_id_now}) ============")
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc_now}.")
    idx = 0
    for i in range(len(monster_inventory_read)):
        if monster_inventory_read[i][0]==user_id_now:
            idx += 1
            inventory_list += [monster_inventory_stats(int(user_id_now),int(monster_inventory_read[i][1]),monster_read,monster_inventory_read)]
            print(f"{idx}. Monster       (Name: {monster_inventory_stats(int(user_id_now),int(monster_inventory_read[i][1]),monster_read,monster_inventory_read)[1]}, Lvl: {monster_inventory_read[i][2]}, HP: {monster_inventory_stats(int(user_id_now),int(monster_inventory_read[i][1]),monster_read,monster_inventory_read)[4]})")
    for i in range(len(item_inventory_read)):
        if item_inventory_read[i][0]==user_id_now:
            idx += 1
            if item_inventory_read[i][1]=="strength":
                potion_type = "ATK"
            elif item_inventory_read[i][1]=="resilience":
                potion_type = "DEF"
            elif item_inventory_read[i][1]=="healing":
                potion_type = "Heal"
            inventory_list += [[potion_type,item_inventory_read[i][2]]]
            print(f"{idx}. Potion        (Type: {potion_type}, Qty: {item_inventory_read[i][2]})")

    print("\nKetikkan id untuk menampilkan detail item (0 untuk keluar):")
    id_detail = input(">>> ")
    while not isDigit(id_detail):
        print("Masukan tidak valid, pilih nomor yang tersedia!")
        id_detail = input(">>> ")
    while int(id_detail)>idx:
        print("Masukan tidak valid, pilih nomor yang tersedia!")
        id_detail = input(">>> ")
        while not isDigit(id_detail):
            print("Masukan tidak valid, pilih nomor yang tersedia!")
            id_detail = input(">>> ")
    while id_detail != '0':
        if len(inventory_list[int(id_detail)-1])==6:
            print("\nMonster")
            print(f"Name       : {inventory_list[int(id_detail)-1][1]}")
            print(f"ATK Power  : {inventory_list[int(id_detail)-1][2]}")
            print(f"DEF Power  : {inventory_list[int(id_detail)-1][3]}")
            print(f"HP         : {inventory_list[int(id_detail)-1][4]}")
            print(f"Level      : {inventory_list[int(id_detail)-1][5]}")
            print("\nKetikkan id untuk menampilkan detail item (0 untuk keluar):")
            id_detail = input(">>> ")
            while not isDigit(id_detail):
                print("Masukan tidak valid, pilih nomor yang tersedia!")
                id_detail = input(">>> ")
            while int(id_detail)>idx:
                print("Masukan tidak valid, pilih nomor yang tersedia!")
                id_detail = input(">>> ")
                while not isDigit(id_detail):
                    print("Masukan tidak valid, pilih nomor yang tersedia!")
                    id_detail = input(">>> ")
        elif len(inventory_list[int(id_detail)-1])==2:
            print("\nPotion")
            print(f"Type       : {inventory_list[int(id_detail)-1][0]}")
            print(f"Quantity   : {inventory_list[int(id_detail)-1][1]}")
            print("\nKetikkan id untuk menampilkan detail item (0 untuk keluar):")
            id_detail = input(">>> ")
            while not isDigit(id_detail):
                print("Masukan tidak valid, pilih nomor yang tersedia!")
                id_detail = input(">>> ")
            while int(id_detail)>idx:
                print("Masukan tidak valid, pilih nomor yang tersedia!")
                id_detail = input(">>> ")
                while not isDigit(id_detail):
                    print("Masukan tidak valid, pilih nomor yang tersedia!")
                    id_detail = input(">>> ")
    print("\nKeluar ke menu utama...")