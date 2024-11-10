import os
import time
from src.utility import write_csv

def save(user_read, monster_read, item_inventory_read, monster_inventory_read, item_shop_read, monster_shop_read):
    folder_path_save = input("Masukkan nama folder: ")
    print("\nSaving...\n")

    if not os.path.exists("./data"):                # handle kasus jika belum ada folder ./data
        os.mkdir("./data")
        print("membuat folder data...")
        time.sleep(0.3)

    if not os.path.exists("./data/"+folder_path_save):              # handle kasus jika belum ada folder tersebut di dalam ./data
        os.makedirs("./data/"+folder_path_save)
        print(f"\nMembuat folder data/{folder_path_save} ...")

    write_csv(user_read, os.path.join("./data/"+folder_path_save, "user.csv"))
    write_csv(monster_read, os.path.join("./data/"+folder_path_save, "monster.csv"))
    write_csv(item_inventory_read, os.path.join("./data/"+folder_path_save, "item_inventory.csv"))
    write_csv(monster_inventory_read, os.path.join("./data/"+folder_path_save, "monster_inventory.csv"))
    write_csv(item_shop_read, os.path.join("./data/"+folder_path_save, "item_shop.csv"))
    write_csv(monster_shop_read, os.path.join("./data/"+folder_path_save, "monster_shop.csv"))

    print(f"Berhasil menyimpan data di folder data/{folder_path_save}!")