import time

'''___________________________________________________UTILITY___________________________________________________'''
def random_number(x,y):
    a = 2**4
    c = 999
    m = 177
    angka = int(time.time_ns())
    random = (a*angka+c)%m
        
    hasil = x+(random % y-x+1)
    return hasil

def fungsi_split(string, indikator):
    indeks = 0
    hasil = []
    for i in range(len(string)):
        if string[i]==indikator:
            hasil.append(string[indeks:i])
            indeks = i+1
    hasil.append(string[indeks:])
    return hasil

def read_csv(csv):
    file = open(csv, 'r')
    matrix = [fungsi_split(i[:-1],';') for i in file]
    return matrix

def write_csv(data, file_path):
    with open(file_path, 'w') as file:
        for row in data:
            file.write(';'.join(row) + '\n')

def isDigit(s):
    if s=='':
        return False
    for char in s:
        if not (ord('0')<=ord(char)<=ord('9')):
            return False
    return True

def monster_stats(monster_id, monster_read):
    monster_detail = [str(monster_id),monster_read[int(monster_id)][1],monster_read[int(monster_id)][2],monster_read[int(monster_id)][3],monster_read[int(monster_id)][4]]
    return monster_detail

def monster_inventory_stats(user_id_now,monster_id,monster_read,monster_inventory_read):
    for i in monster_inventory_read:
        if i[0]==str(user_id_now) and i[1]==str(monster_id):
            monster_level = i[2]
    monster_detail = [str(monster_id),monster_read[int(monster_id)][1],monster_read[int(monster_id)][2],monster_read[int(monster_id)][3],monster_read[int(monster_id)][4],monster_level]
    return monster_detail

def potion_list(user_id_now, item_inventory_read):
    potion = []
    for i in range(len(item_inventory_read)):
        if item_inventory_read[i][0]==user_id_now:
            if item_inventory_read[i][1]=="strength":
                potion_type = "Strength Potion"
                effect = "Increases ATK Power"
            elif item_inventory_read[i][1]=="resilience":
                potion_type = "Resilience Potion"
                effect = "Increases DEF Power"
            elif item_inventory_read[i][1]=="healing":
                potion_type = "Healing Potion"
                effect = "Restores Health"
            potion += [[potion_type,item_inventory_read[i][2],effect,item_inventory_read[i][1]]]
    return potion

def mekanisme_battle(user_id_now,matrix,item_inventory_read):
    monster_musuh = matrix[0][0]
    atk_musuh = matrix[0][1]
    def_musuh = matrix[0][2]
    hp_musuh = matrix[0][3]
    level_monster_musuh = matrix[0][4]
    monster_user = matrix[1][0]
    atk_user = matrix[1][1]
    def_user = matrix[1][2]
    hp_user = matrix[1][3]
    level_monster_user = matrix[1][4]

    max_hp_user = hp_user
    turn = 1
    switch = 1
    atk_potion_use = 0 
    def_potion_use = 0
    hp_potion_use = 0
    damage_given = 0
    damage_taken = 0
    while hp_musuh>0 and hp_user>0:
        if switch%2==1:
            ask_action = True
            while ask_action:
                print(f"\n============ TURN {turn} ({monster_user}) ============")
                print("1. Attack")
                print("2. Use Potion")
                print("3. Quit\n")
                action = input("Pilih perintah: ")
                while not isDigit(action):
                    print("Masukan tidak valid, pilih nomor yang tersedia!")
                    action = input("Pilih perintah: ")
                while int(action)>3:
                    print("Masukan tidak valid, pilih nomor yang tersedia!")
                    action = input("Pilih perintah: ")
                    while not isDigit(action):
                        print("Masukan tidak valid, pilih nomor yang tersedia!")
                        action = input("Pilih perintah: ")
                if action == '1':
                    rng_atk_user = random_number(-30,30)
                    atk_user_after_rng = atk_user + (atk_user*rng_atk_user*0.01)
                    damage_given += atk_user_after_rng
                    hp_musuh = int((hp_musuh-(atk_user_after_rng-(atk_user_after_rng*def_musuh*0.01)))//1)
                    if hp_musuh<0:
                        hp_musuh=0
                        result = "Win"
                    print(f"\nSCHWINKKK, {monster_user} menyerang {monster_musuh} !!!")
                    for char in (". . ."):
                        print(char, end='', flush=True)
                        time.sleep(0.2)
                    print(f"\nName      : {monster_musuh}")
                    print(f"ATK Power : {atk_musuh}")
                    print(f"DEF Power : {def_musuh}")
                    print(f"HP        : {hp_musuh}")
                    print(f"Level     : 1")
                    print(f"\nPenjelasan: ATT: {atk_user_after_rng} ({rng_atk_user}%), Reduced by: {atk_user_after_rng*def_musuh*0.01} ({def_musuh}%), ATT Results: {atk_user_after_rng-(atk_user_after_rng*def_musuh*0.01)}")
                    switch += 1
                    ask_action = False
                elif action == '2':
                    ask_potion = True
                    while ask_potion:
                        print("\n============ POTION LIST ============")
                        for i in range(len(potion_list(user_id_now, item_inventory_read))):
                            print(f"{i+1}. {potion_list(user_id_now, item_inventory_read)[i][0]} (Qty: {potion_list(user_id_now, item_inventory_read)[i][1]}) - {potion_list(user_id_now, item_inventory_read)[i][2]}")
                            idx = i+2
                        print(f"{idx}. Cancel")
                        print()
                        potion_choose = input("Pilih Potion: ")
                        while not isDigit(potion_choose):
                            print("Masukan tidak valid, pilih nomor yang tersedia!")
                            potion_choose = input("Pilih Potion: ")
                        while int(potion_choose)>idx:
                            print("Masukan tidak valid, pilih nomor yang tersedia!")
                            potion_choose = input("Pilih Potion: ")
                            while not isDigit(potion_choose):
                                print("Masukan tidak valid, pilih nomor yang tersedia!")
                                potion_choose = input("Pilih Potion: ")
                        if int(potion_choose)==idx:
                            ask_potion = False
                        elif int(potion_choose)<idx:
                            if potion_list(user_id_now, item_inventory_read)[int(potion_choose)-1][0]=="Strength Potion":
                                type_potion = "strength"
                                if atk_potion_use == 0:
                                    print(f"Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {monster_user} dan gerakannya menjadi lebih cepat dan mematikan.")
                                    atk_user += (atk_user*0.05)
                                    atk_potion_use = 1
                                    switch += 1
                                    ask_potion = False
                                    ask_action = False
                                    for i in range(len(item_inventory_read)):
                                        if item_inventory_read[i][0]==user_id_now and item_inventory_read[i][1]==type_potion:
                                            item_inventory_read[i][2] = str(int(item_inventory_read[i][2])-1)
                                else:
                                    print(f"Kamu mencoba memberikan ramuan ini kepada {monster_user}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                            elif potion_list(user_id_now, item_inventory_read)[int(potion_choose)-1][0]=="Resilience Potion":
                                type_potion = "resilience"
                                if def_potion_use == 0:
                                    print(f"Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {monster_user} yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
                                    def_user += (def_user*0.05)
                                    def_potion_use = 1
                                    switch += 1
                                    ask_potion = False
                                    ask_action = False
                                    for i in range(len(item_inventory_read)):
                                        if item_inventory_read[i][0]==user_id_now and item_inventory_read[i][1]==type_potion:
                                            item_inventory_read[i][2] = str(int(item_inventory_read[i][2])-1)
                                else:
                                    print(f"Kamu mencoba memberikan ramuan ini kepada {monster_user}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                            elif potion_list(user_id_now, item_inventory_read)[int(potion_choose)-1][0]=="Healing Potion":
                                type_potion = "healing"
                                if hp_potion_use == 0:
                                    print(f"Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {monster_user} sembuh dengan cepat. Dalam sekejap, {monster_user} terlihat kembali prima dan siap melanjutkan pertempuran.")
                                    hp_user += (max_hp_user*0.25)
                                    if hp_user>max_hp_user:
                                        hp_user = max_hp_user
                                    hp_potion_use = 1
                                    switch += 1
                                    ask_potion = False
                                    ask_action = False
                                    for i in range(len(item_inventory_read)):
                                        if item_inventory_read[i][0]==user_id_now and item_inventory_read[i][1]==type_potion:
                                            item_inventory_read[i][2] = str(int(item_inventory_read[i][2])-1)
                                else:
                                    print(f"Kamu mencoba memberikan ramuan ini kepada {monster_user}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                elif action == '3':
                    print("\nAnda berhasil kabur dari BATTLE!")
                    result = "Lose"
                    return (result,damage_given,damage_taken,item_inventory_read)
        else:
            rng_atk_musuh = random_number(-30,30)
            atk_musuh_after_rng = atk_musuh + (atk_musuh*rng_atk_musuh*0.01)
            damage_taken += atk_musuh_after_rng
            hp_user = int((hp_user-(atk_musuh_after_rng-(atk_musuh_after_rng*def_user*0.01)))//1)
            if hp_user<0:
                hp_user=0
                result = "Lose"
            print(f"\n============ TURN {turn} ({monster_musuh}) ============")
            print(f"\nSCHWINKKK, {monster_musuh} menyerang {monster_user} !!!")
            for char in (". . ."):
                print(char, end='', flush=True)
                time.sleep(0.2)
            print(f"\nName      : {monster_user}")
            print(f"ATK Power : {atk_user}")
            print(f"DEF Power : {def_user}")
            print(f"HP        : {hp_user}")
            print(f"Level     : {level_monster_user}")
            print(f"\nPenjelasan: ATT: {atk_musuh_after_rng} ({rng_atk_musuh}%), Reduced by: {atk_musuh_after_rng*def_user*0.01} ({def_user}%), ATT Results: {atk_musuh_after_rng-(atk_musuh_after_rng*def_user*0.01)}")
            switch += 1
            turn += 1
    return (result,damage_given,damage_taken,item_inventory_read)