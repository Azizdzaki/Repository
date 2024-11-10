from src.utility import random_number,mekanisme_battle,monster_inventory_stats,isDigit

def battle(user_id_now,user_oc_now,user_read, monster_read, monster_inventory_read, item_inventory_read):
    all_monster_id_database = [i[0] for i in monster_read]
    all_monster_id_user = []

    print("\n>>> BATTLE")
    monster_id_musuh = random_number(1,len(all_monster_id_database)-1)
    monster_musuh = monster_read[monster_id_musuh][1]
    atk_musuh = int(monster_read[monster_id_musuh][2])
    def_musuh = int(monster_read[monster_id_musuh][3])
    hp_musuh = int(monster_read[monster_id_musuh][4])
    level_monster_musuh = 1
    print(f"\nRAWRRR, Monster {monster_musuh} telah muncul !!!\n")
    print(f"Name      : {monster_musuh}")
    print(f"ATK Power : {atk_musuh}")
    print(f"DEF Power : {def_musuh}")
    print(f"HP        : {hp_musuh}")
    print(f"Level     : {level_monster_musuh}")

    print("\n============ MONSTER LIST ============")
    idx = 0
    for i in range(len(monster_inventory_read)):
        if monster_inventory_read[i][0]==user_id_now:
            idx += 1
            all_monster_id_user += monster_inventory_read[i][1]
            print(f"{idx}. {monster_inventory_stats(int(user_id_now),int(monster_inventory_read[i][1]),monster_read,monster_inventory_read)[1]}")
    print()
    monster_use = input("Pilih monster untuk bertarung: ")
    while not isDigit(monster_use):
        print("Masukan tidak valid, pilih nomor yang tersedia!")
        monster_use = input("Pilih monster untuk bertarung: ")
    while int(monster_use)>idx:
        print("Pilihan nomor tidak tersedia!")
        monster_use = input("Pilih monster untuk bertarung: ")
        while not isDigit(monster_use):
            print("Masukan tidak valid, pilih nomor yang tersedia!")
            monster_use = input("Pilih monster untuk bertarung: ")
    monster_user = monster_inventory_stats(user_id_now,all_monster_id_user[int(monster_use)-1],monster_read,monster_inventory_read)[1]
    level_monster_user = int(monster_inventory_stats(user_id_now,all_monster_id_user[int(monster_use)-1],monster_read,monster_inventory_read)[5])
    atk_user = int(int(monster_inventory_stats(user_id_now,all_monster_id_user[int(monster_use)-1],monster_read,monster_inventory_read)[2])+(int(monster_inventory_stats(user_id_now,all_monster_id_user[int(monster_use)-1],monster_read,monster_inventory_read)[2])*((level_monster_user-1)*10)*0.01))
    def_user = int(int(monster_inventory_stats(user_id_now,all_monster_id_user[int(monster_use)-1],monster_read,monster_inventory_read)[3])+(int(monster_inventory_stats(user_id_now,all_monster_id_user[int(monster_use)-1],monster_read,monster_inventory_read)[3])*((level_monster_user-1)*10)*0.01))
    hp_user = int(int(monster_inventory_stats(user_id_now,all_monster_id_user[int(monster_use)-1],monster_read,monster_inventory_read)[4])+(int(monster_inventory_stats(user_id_now,all_monster_id_user[int(monster_use)-1],monster_read,monster_inventory_read)[4])*((level_monster_user-1)*10)*0.01))
    print(f"\nRAWRRR, Agent {user_read[int(user_id_now)][1]} mengeluarkan monster {monster_user} !!!")
    print(f"\nName      : {monster_user}")
    print(f"ATK Power : {atk_user}")
    print(f"DEF Power : {def_user}")
    print(f"HP        : {hp_user}")
    print(f"Level     : {level_monster_user}")

    matrix = [[monster_musuh,atk_musuh,def_musuh,hp_musuh,level_monster_musuh],[monster_user,atk_user,def_user,hp_user,level_monster_user]]
    result,damage_given,damage_taken, item_inventory_read = mekanisme_battle(user_id_now,matrix,item_inventory_read)
    
    if result=="Win":
        print(f"\nSelamat, Anda berhasil mengalahkan monster {monster_musuh} !!!")
        reward = random_number(5,30)
        print(f"\nTotal OC yang diperoleh: {reward}")
        for j in range(len(user_read)):
            if user_read[j][0]==user_id_now:
                user_read[j][4] = str(int(user_oc_now)-reward)
    else:
        print(f"\nYahhh, Anda dikalahkan monster {monster_musuh}. Jangan menyerah, coba lagi !!!")
    return (user_read)