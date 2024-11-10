def login(user_read,user_id_now,username,user_oc_now,user_role_now,sudah_login):
    if sudah_login == False:
        username = input("Username: ")
        password = input("Password: ")

        all_username = [i[1] for i in user_read]
        if username not in all_username:
            print("\nUsername tidak terdaftar!")
        else:
            for i in range(len(user_read)):
                if user_read[i][1]==username:
                    if user_read[i][2]==password:
                        user_id_now = user_read[i][0]
                        user_role_now = user_read[i][3]
                        user_oc_now = int(user_read[i][4])
                        if user_role_now == 'agent':
                            print("Selamat datang, Agent "+username+"!")
                        elif user_role_now == 'admin':
                            print("Selamat datang, Admin "+username+"!")
                        sudah_login = True
                        break
                    else:
                        print("Password salah!")
                        break
    else:
        print("\nLogin gagal!")
        print(f"Anda telah login dengan username {username}, silahkan lakukan 'LOGOUT' sebelum melakukan login kembali.")
    
    return(user_id_now,username,user_role_now,user_oc_now,sudah_login)