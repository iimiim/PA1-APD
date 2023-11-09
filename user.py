import os
from load_data import json_paket, update_user
from service import enter_kembali, clear_screen
from prettytable import PrettyTable

# program untuk user melihat info akun mereka
def profile(user):
    clear_screen()
    while True:
        table_fields = ["Username", "Password", "Role", "Langganan"]
        table = PrettyTable()
        table.padding_width = 5
        table.field_names = ["N0."] + table_fields

        for i, row in enumerate(user[1:], start=1):
            row_to_display = [i] + [row[col] for col in table_fields]
            table.add_row(row_to_display)
        enter_kembali()
        clear_screen()
        break


def paket():
    while True:
        try:
            urutan_paket = enumerate(json_paket["jenis"])
            print(f"Silahkan Pilih Paket yang ingin dibeli:")
            for nomor,kata in urutan_paket:
                print(f"{nomor+1}. {kata}")
            print(f"{len(json_paket["jenis"])+1}. Kembali")
            pilih = int(input("Masukkan angka yang anda pilih: "))
            clear_screen()
            return pilih
        except:
            clear_screen()
            print("Tolong masukkan data pake sesuai yang diminta!")


# program agar user dapat melakukan pembelian paket
def buy(user):
    while True:
        try:
            pilih = paket()
            if pilih == len(json_paket["jenis"])+1:
                break
            while True:
                urutan_paket = enumerate(json_paket["harga"][pilih-1])
                print(f"Silahkan Pilih Paket yang ingin dibeli:")
                for nomor,kata in urutan_paket:
                    print(f"{nomor+1}. {kata}")
                print(f"{len(json_paket["harga"][pilih-1])+1}. Kembali")
                harga = int(input("Masukkan pilihan harga: "))
                if harga == len(json_paket["harga"][pilih-1])+1:
                    clear_screen()
                    break
                elif harga >= 0 or harga < len(json_paket["harga"]):
                    yakin = input(
                        f"Anda akan membeli paket membership {json_paket['harga'][pilih-1][harga-1]}, yakin? (ya/tidak): "
                    )
                    if yakin == "ya":
                        clear_screen()
                        # user["langganan"] = json_paket["harga"][pilih-1][harga - 1]
                        print(update_user(user,pilih-1,harga-1))
                        return user
                    elif yakin == "tidak":
                        clear_screen()
                        return user
                    return harga
                else:
                    print("Pilihan tidak tersedia!")
                    break
        except:
            clear_screen()
            print("Tolong masukkan data harga sesuai yang diminta!")

