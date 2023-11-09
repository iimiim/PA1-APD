import os
from load_data import create_user, json_user
from service import clear_screen


# Mengecek yang login admin atau user biasa
def cek_admin(admin):
    if admin["role"] == "admin":
        return True
    return False


# Program untuk melakukan registrasi user baru
def daftar():
    clear_screen()
    print("REGISTER\n")
    username = input("Masukkan Username anda: ")
    password = input("Masukkan Password anda: ")
    if username == "admin":
        clear_screen()
        print("Username tidak boleh 'admin'")
    else:
        user = {
            "username": username,
            "password": password,
            "role": "user",
            "langganan": None,
        }
        clear_screen()
        print(create_user(user))


# Program untuk melakukan login
def login():
    k = 3
    while k >= 1:
        try:
            clear_screen()
            print("LOGIN\n")
            username = input("Masukkan Username anda: ")
            password = input("Masukkan Password anda: ")

            cek_user = [
                x
                for x in json_user
                if x["username"] == username and x["password"] == password
            ]
            if len(cek_user) == 0:
                clear_screen()
                k -= 1
                print(f"Gagal login, sisa percobaan login anda adalah: {k} kali.")
                print("Periksa apakah data yang dimassukkan sudah sesuai!")
                if k > 0:
                    while True:
                        ulang_login = input("Apakah mau mengulang login? (ya/tidak): ")
                        if ulang_login == "ya":
                            break
                        elif ulang_login == "tidak":
                            clear_screen()
                            return
                        else:
                            clear_screen()
                            print("Tolong masukkan data sesuai yang diminta!")
                else:
                    clear_screen()
                    print(f"Gagal login, sisa percobaan login anda adalah: {k} kali.")
                    print("Pilih login untuk mencoba lagi.")
                    return False
            else:
                clear_screen()
                print("Login Berhasil")
                return cek_user[0]
        except:
            print("Tolong masukkan data sesuai yang diminta!")
