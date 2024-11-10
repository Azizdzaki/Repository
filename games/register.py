from src.utility import isDigit

def register(user_read, monster_read, monster_inventory_read,sudah_login,username):
    if sudah_login == False:
        print(">>> REGISTER\n")
        username = input("Username: ")
        password = input("Password: ")
        user_id = str(len(user_read))
        username_valid = True
        for i in username:
            if not ((65<=ord(i)<=90) or (97<=ord(i)<=122) or (48<=ord(i)<=57) or (i=='_') or (i=='-')):
                username_valid = False
        for i in range(1,len(user_read)):
            if (user_read[i][1]) == username:
                print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
                return (user_read, monster_inventory_read)
        if not username_valid:
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        else:
            user_read += [[user_id,username,password,"agent",'0']]
            print("\nSilahkan pilih salah satu monster sebagai monster awalmu.")
            for i in range(1,len(monster_read)):
                print(f"{i}. {monster_read[i][1]}")
            print()
            monster_choice = input("Pilih nomor Monster pilihanmu: ")
            while not isDigit(monster_choice):
                print("Masukan tidak valid, pilih nomor monster yang tersedia!")
                monster_choice = input("Pilih nomor Monster pilihanmu: ")
            while int(monster_choice)<1 or int(monster_choice)>len(monster_read)-1:
                print("Masukan tidak valid, pilih nomor monster yang tersedia!")
                monster_choice = input("Pilih nomor Monster pilihanmu: ")
                while not isDigit(monster_choice):
                    print("Masukan tidak valid, pilih nomor monster yang tersedia!")
                    monster_choice = input("Pilih nomor Monster pilihanmu: ")
            for i in range(1, len(monster_read)):
                if monster_read[i][0] == monster_choice :
                    first_monster = monster_read[i][1]
            monster_inventory_read += [[user_id,monster_choice,'1']]
            print(f"Selamat datang agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {first_monster}!")
    else:
        print("\nRegister gagal!")
        print(f"Anda telah login dengan username {username}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
    return (user_read, monster_inventory_read)