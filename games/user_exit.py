from src import save

def user_exit(user_read,monster_read,item_inventory_read,monster_inventory_read,item_shop_read,monster_shop_read):
    validation = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ").lower()
    while validation != "y" and validation != "n":
        validation = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ").lower()
    if validation == 'y':
        save.save(
            user_read,
            monster_read,
            item_inventory_read,
            monster_inventory_read,
            item_shop_read,
            monster_shop_read
        )
        print("\nKeluar program...")
    elif validation == 'n':
        print("\nKeluar program...")
        exit()