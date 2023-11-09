import os
from regis_login import daftar, login, cek_admin
from admin import data_member, hapus_user, hapus_paket, buat_paket, perbarui_paket, cancel_mem_user
from user import profile, buy
from load_data import json_paket
from service import clear_screen
from prettytable import PrettyTable

# Program utama untuk menjalankan semua program yang diatas
def main():
    clear_screen()
    while True:
        print(
            """
SELAMAT DATANG DI GYM BRO
""")
        table = PrettyTable()
        table.field_names = ["MENU"]
        table.padding_width = 5
        table.add_row(["1. Register"])
        table.add_row(["2. Login"])
        table.add_row(["3. Quit"])
        print(table)

        pilih = input("Pilih angka menu: ")
        if pilih == "1":
            daftar()
        elif pilih == "2":
            user = login()
            if user:
                if cek_admin(user):
                    menu_admin(user)
                else:
                    menu_user(user)
        elif pilih == "3":
            clear_screen()
            print("PROGRAM BERHENTI!")
            break
        else:
            clear_screen()
            print(f"Pilihan tidak tersedia!")


# program menu untuk admin
def menu_admin(admin):
    while True:
        print(
            """
SELAMAT DATANG ADMIN
""")
        table = PrettyTable()
        table.field_names = ["MENU"]
        table.padding_width = 5
        table.add_row(["1. List Member"])
        table.add_row(["2. Create Package"])
        table.add_row(["3. Update Package"])
        table.add_row(["4. Delete Package"])
        table.add_row(["5. Cancel Membership User"])
        table.add_row(["6. Delete Member"])
        table.add_row(["7. log Out"])
        print(table)

        pilih = input("Pilih angka menu: ")
        if pilih == "1":
            clear_screen()
            data_member()
        elif pilih == "2":
            clear_screen()
            print(buat_paket(json_paket))
        elif pilih == "3":
            clear_screen()
            perbarui_paket()
        elif pilih == "4":
            clear_screen()
            print(hapus_paket())
        elif pilih == "5":
            clear_screen()
            print(cancel_mem_user())
        elif pilih == "6":
            clear_screen()
            print(hapus_user())
        elif pilih == "7":
            clear_screen()
            print("Sampai Jumpa lagi Admin.")
            break
        else:
            clear_screen()
            print(f"Pilihan tidak tersedia!")


# program menu untuk user
def menu_user(user):
    while True:
        print(
            f"""
SELAMAT DATANG {user['username'].title()}
""")
        table = PrettyTable()
        table.field_names = ["MENU"]
        table.padding_width = 5
        table.add_row(["1. Profile"])
        table.add_row(["2. Beli Membership"])
        table.add_row(["3. Log Out"])
        print(table)

        pilih = input("Pilih angka menu: ")
        if pilih == "1":
            profile(user)
        elif pilih == "2":
            clear_screen()
            buy(user)
        elif pilih == "3":
            clear_screen()
            print(f"Sampai Jumpa lagi {user['username'].title()}")
            return user
        else:
            clear_screen()
            print(f"Pilihan tidak tersedia!")


main()
