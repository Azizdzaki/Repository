from src.utility import monster_inventory_stats, random_number,mekanisme_battle, isDigit

def arena(user_id_now,user_oc_now,user_read, monster_read, monster_inventory_read, item_inventory_read):
    all_monster_id_database = [i[0] for i in monster_read]
    all_monster_id_user = []

    print("\n>>> ARENA")
    print("\nSelamat datang di Arena !")
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
    max_hp_user = hp_user
    print(f"\nRAWRRR, Agent {user_read[int(user_id_now)][1]} mengeluarkan monster {monster_user} !!!")
    print(f"\nName      : {monster_user}")
    print(f"ATK Power : {atk_user}")
    print(f"DEF Power : {def_user}")
    print(f"HP        : {hp_user}")
    print(f"Level     : {level_monster_user}")

    result = "Win"
    stage = 1
    reward = [0,30,50,100,150,200]
    total_damage_given = 0
    total_damage_taken = 0
    while stage<=5 and result=="Win":
        print(f"\n============= STAGE {stage} =============")
        monster_id_musuh = random_number(1,len(all_monster_id_database)-1)
        monster_musuh = monster_read[monster_id_musuh][1]
        level_monster_musuh = stage
        atk_musuh = int(int(monster_read[monster_id_musuh][2])+(int(monster_read[monster_id_musuh][2])*((level_monster_musuh-1)*10)*0.01))
        def_musuh = int(int(monster_read[monster_id_musuh][3])+(int(monster_read[monster_id_musuh][3])*((level_monster_musuh-1)*10)*0.01))
        hp_musuh = int(int(monster_read[monster_id_musuh][4])+(int(monster_read[monster_id_musuh][4])*((level_monster_musuh-1)*10)*0.01))
        print(f"\nRAWRRR, Monster {monster_musuh} telah muncul !!!\n")
        print(f"Name      : {monster_musuh}")
        print(f"ATK Power : {atk_musuh}")
        print(f"DEF Power : {def_musuh}")
        print(f"HP        : {hp_musuh}")
        print(f"Level     : {level_monster_musuh}")

        matrix = [[monster_musuh,atk_musuh,def_musuh,hp_musuh,level_monster_musuh],[monster_user,atk_user,def_user,hp_user,level_monster_user]]
        result,damage_given,damage_taken, item_inventory_read = mekanisme_battle(user_id_now,matrix,item_inventory_read)
        total_damage_given += damage_given
        total_damage_taken += damage_taken

        if result=="Win":
            if stage<5:
                print(f"\nSelamat, Anda berhasil mengalahkan monster {monster_musuh} !!!")
                print(f"\nSTAGE CLEARED! Anda akan mendapatkan {reward[stage]} OC pada sesi ini!")
                print("\nMemulai stage berikutnya...")
            else:
                print(f"\nSelamat, Anda berhasil mengalahkan monster {monster_musuh} !!!")
                print(f"\nSTAGE CLEARED! Anda akan mendapatkan 200 OC pada sesi ini!")
                print(f"\nSelamat, Anda berhasil menyelesaikan seluruh stage Arena !!!")
                print("\n============== STATS ==============")
                print(f"Total hadiah      : 200 OC")
                print(f"Jumlah stage      : {stage}")
                print(f"Damage diberikan  : {total_damage_given}")
                print(f"Damage diterima   : {total_damage_taken}")
                total_reward = 200
            stage += 1
                
        else:
            print(f"\nYahhh, Anda dikalahkan monster {monster_musuh}. Jangan menyerah, coba lagi !!!")
            print(f"\nGAME OVER! Sesi latihan berakhir pada stage {stage}!")
            print("\n============== STATS ==============")
            print(f"Total hadiah      : {reward[stage-1]} OC")
            print(f"Jumlah stage      : {stage}")
            print(f"Damage diberikan  : {total_damage_given}")
            print(f"Damage diterima   : {total_damage_taken}")
            result = "lose"
            total_reward = reward[stage-1]
    for j in range(len(user_read)):
        if user_read[j][0]==user_id_now:
            user_read[j][4] = str(int(user_oc_now)+total_reward)
    return (user_read)