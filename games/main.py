from src import register,login,logout,help,inventory,battle,arena,shop,laboratory,shop_management,monster_management,load,save,user_exit,utility

folder_path = str(load.load())
user_read = utility.read_csv(folder_path + "/user.csv")
monster_read = utility.read_csv(folder_path + "/monster.csv")
item_inventory_read = utility.read_csv(folder_path + "/item_inventory.csv")
monster_inventory_read = utility.read_csv(folder_path + "/monster_inventory.csv")
item_shop_read = utility.read_csv(folder_path + "/item_shop.csv")
monster_shop_read = utility.read_csv(folder_path + "/monster_shop.csv")

(user_id_now,username,user_role_now,user_oc_now,sudah_login) = ('','','','',False)

while True:
    print("\n-------------------------------------------------------------------------------------")
    menu = input(">>> Masukkan command ('help' untuk daftar command yang dapat kamu panggil): ").lower()
    print("-------------------------------------------------------------------------------------")
    if menu=='register':
        register.register(user_read, monster_read, monster_inventory_read,sudah_login,username)
    elif menu=='login':
        (user_id_now,username,user_role_now,user_oc_now,sudah_login) = login.login(user_read,user_id_now,username,user_oc_now,user_role_now,sudah_login)
    elif menu=='logout':
        sudah_login = logout.logout(sudah_login)
    elif menu=='help':
        help.help(user_role_now)
    elif menu=='inventory':
        if sudah_login == False:
            print("Maaf anda harus login terlebih dahulu untuk mengakses inventory")
        else:
            if user_role_now == 'agent':
                inventory.inventory(user_id_now,user_oc_now,monster_inventory_read,item_inventory_read,monster_read)
            elif user_role_now == 'admin':
                print("Maaf, perintah yang hanya dapat dijalankan oleh agent")
    elif menu=='battle':
        if sudah_login == False:
            print("Maaf anda harus login terlebih dahulu untuk mengakses battle")
        else:
            if user_role_now == 'agent':
                battle.battle(user_id_now,user_oc_now,user_read, monster_read, monster_inventory_read, item_inventory_read)
            elif user_role_now == 'admin':
                print("Maaf, perintah yang hanya dapat dijalankan oleh agent") 
    elif menu=='arena':
        if sudah_login == False:
            print("Maaf anda harus login terlebih dahulu untuk mengakses arena")
        else:
            if user_role_now == 'agent':
                arena.arena(user_id_now,user_oc_now,user_read, monster_read, monster_inventory_read, item_inventory_read)
            elif user_role_now == 'admin':
                print("Maaf, perintah yang hanya dapat dijalankan oleh agent") 
    elif menu=='shop':
        if sudah_login == False:
            print("Maaf anda harus login terlebih dahulu untuk mengakses shop")
        else:
            if user_role_now == 'agent':
                shop.shop(user_id_now,user_oc_now,user_read, monster_read, monster_shop_read, item_shop_read, monster_inventory_read, item_inventory_read)
            elif user_role_now == 'admin':
                print("Maaf, perintah yang hanya dapat dijalankan oleh agent")
    elif menu=='laboratory':
        if sudah_login == False:
            print("Maaf anda harus login terlebih dahulu untuk mengakses laboratory")
        else:
            if user_role_now == 'agent':
                laboratory.laboratory(user_id_now,user_oc_now,monster_read, monster_inventory_read, user_read)
            elif user_role_now == 'admin':
                print("Maaf, perintah yang hanya dapat dijalankan oleh agent")
    elif menu =='shop management':
        if sudah_login == False:
            print("Maaf anda harus login terlebih dahulu untuk mengakses shop management")
        else:
            if user_role_now == 'admin':
                shop_management.shop_management(item_shop_read, monster_shop_read, monster_read)
            elif user_role_now == 'agent':
                print("Maaf, perintah yang hanya dapat dijalankan oleh admin")
    elif menu =='monster management':
        if sudah_login == False:
            print("Maaf anda harus login terlebih dahulu untuk mengakses monster management")
        else:
            if user_role_now == 'admin':
                monster_management.monster_management(monster_read)
            elif user_role_now == 'agent':
                print("Maaf, perintah yang hanya dapat dijalankan oleh admin")
    elif menu=='exit':
        user_exit.user_exit(user_read,monster_read,item_inventory_read,monster_inventory_read,item_shop_read,monster_shop_read) 
        break
    else:
        print("Input tidak valid! Masukkan nama command yang tersedia!")