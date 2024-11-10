def logout(sudah_login):
    if sudah_login==True:
        sudah_login = False
        print("\nBerhasil logout!")
    else:
        print("\nLogout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return (sudah_login)