import os
from load_data import json_user, json_paket, delete_user, delete_package, show_user, create_paket, update_paket, cancel_user_mem, delete_harga, save_paket
from service import enter_kembali, enter_lanjut, clear_screen
from prettytable import PrettyTable

table = PrettyTable()


# Program agar admin dapat melihat list member yang telah bergabung
def data_member():
    if len(json_user) == 1:
        print("Tidak Ada User Terdaftar!")
    else:
        for i in json_user:
            if len(json_user) == 1:
                print("Tidak Ada User Terdaftar!")
            elif i["role"] == "admin":
                continue
        show_user()
    enter_kembali()
    clear_screen()


# Program untuk menghapus user oleh admin
def hapus_user():
    clear_screen()
    while True:
        try:
            print("Pilih data member yang akan dihapus: ")
            if len(json_user) == 1:
                print("Tidak Ada User Terdaftar!")
                enter_kembali()
                return
            else:
                for i in json_user:
                    if len(json_user) == 1:
                        print("Tidak Ada User Terdaftar!")
                        enter_kembali()
                        return
                    elif i["role"] == "admin":
                        continue
                show_user()
                pilih = int(
                    input("Masukkan angka yang dipilih (Tekan 0 untuk kembali): ")
                )
                if pilih == 0:
                    clear_screen()
                    return ""
                else:
                    delete_user(pilih)
                    clear_screen()
                    show_user()
                    enter_kembali()
                    clear_screen()
                    return "Data user berhasil dihapus"
        except:
            clear_screen()
            print("Pilihan tidak tersedia!")

def buat_paket(data):
    clear_screen()
    jenis = input("Masukkan jenis paket (0 atau kosongkan untuk kembali): ")
    if jenis == "0" or jenis == "":
        clear_screen()
        return "Tidak Ada Paket yang ditambahkan."
    else:
        daf_harga = []
        while True:
            for i in daf_harga:
                print(i)
            harga = input("Masukkan harga langganan (0 atau untuk selesai): ")
            lama = input("Masukkan lama bulan (0 untuk selesai): ")
            if harga.isdigit() and lama.isdigit():
                clear_screen()
                baru = f"Rp{harga}/{lama} Bulan"
                if harga == "0" or lama == "0":
                    break
                else:
                    daf_harga.append(baru)
            else:
                clear_screen()
                print("Masukkan Angka yang valid")
                continue
        if len(daf_harga) == 0:
            clear_screen()
            return "tidak ada paket yg ditambahkan"
        else:
            data["harga"].append(daf_harga)
            data["jenis"].append(jenis)
    return create_paket(data)

def hapus_paket():
    while True:
        clear_screen()
        table = PrettyTable()
        table.field_names = ["Pilihan Hapus"]
        table.padding_width = 5
        table.add_row(["1. Paket"])
        table.add_row(["2. Harga & lama Paket"])
        table.add_row(["3. Kembali"])
        print(table)
        pilih = input("Masukkan pilihan Menu: ")
        clear_screen()
        if pilih == "1":
            urutan_paket = enumerate(json_paket["jenis"])
            print(f"Pilih Paket yang ingin dihapus:")
            for nomor,kata in urutan_paket:
                print(f"{nomor+1}. {kata}")
            print(f"{len(json_paket["jenis"])+1}. Kembali")
            pilih = int(input("Masukkan angka yang anda pilih: "))
            clear_screen()
            if pilih == len(json_paket["jenis"])+1:
                return "Tidak ada paket yang telah dihapus"
            else:
                hasil = delete_package(pilih)
                return hasil
        elif pilih == "2":
            while True:
                clear_screen()
                urutan_paket = enumerate(json_paket["jenis"])
                print(f"Pilih Paket yang ingin diubah:")
                for nomor,kata in urutan_paket:
                    print(f"{nomor+1}. {kata}")
                print(f"{len(json_paket["jenis"])+1}. Kembali")
                milih = int(input("Masukkan angka yang anda pilih: "))
                clear_screen()
                if milih == len(json_paket["jenis"])+1:
                    clear_screen()
                    break
                else:
                    while True:
                        urutan_paket = enumerate(json_paket["harga"][milih-1])
                        print(f"Silahkan Pilih Paket yang ingin dirubah:")
                        for nomor,kata in urutan_paket:
                            print(f"{nomor+1}. {kata}")
                        print(f"{len(json_paket["harga"][milih-1])+1}. Kembali")
                        harga = int(input("Masukkan pilihan harga yang ingin diubah: "))
                        if harga == len(json_paket["harga"][milih-1])+1:
                            clear_screen()
                            break
                        elif harga >= 0 or harga < len(json_paket["harga"]):
                            hasil = delete_harga(milih,harga)
                            return hasil
        elif pilih == "3":
            return "Tidak ada paket yang telah dihapus"


def perbarui_paket():
    clear_screen()
    while True:
        try:
            table = PrettyTable()
            table.field_names = ["Pilihan Ubah"]
            table.padding_width = 5
            table.add_row(["1. Nama Paket"])
            table.add_row(["2. Harga & lama Paket"])
            table.add_row(["3. Menambahkan varian harga & lama paket"])
            table.add_row(["4. Kembali"])
            print(table)
            pilih = input("Masukkan pilihan Menu: ")
            clear_screen()
            if pilih == "1":
                while True:
                    try:
                        urutan_paket = enumerate(json_paket["jenis"])
                        print(f"Pilih Paket yang ingin diubah:")
                        for nomor,kata in urutan_paket:
                            print(f"{nomor+1}. {kata}")
                        print(f"{len(json_paket["jenis"])+1}. Kembali")
                        milih = int(input("Masukkan angka yang anda pilih: "))
                        if milih == len(json_paket["jenis"])+1:
                            clear_screen()
                            break
                        else:
                            baru = input("Masukkan nama paket pengganti: ")
                            json_paket["jenis"][milih-1] = baru
                            clear_screen()
                            save_paket(json_paket)
                            print("Nama Paket telah dirubah.")
                    except:
                        clear_screen()
                        print("Masukkan data sesuai yang diminta!")
            elif pilih == "2":
                while True:
                    try:
                        clear_screen()
                        urutan_paket = enumerate(json_paket["jenis"])
                        print(f"Pilih Paket yang ingin diubah:")
                        for nomor,kata in urutan_paket:
                            print(f"{nomor+1}. {kata}")
                        print(f"{len(json_paket["jenis"])+1}. Kembali")
                        milih = int(input("Masukkan angka yang anda pilih: "))
                        clear_screen()
                        if milih == len(json_paket["jenis"])+1:
                            clear_screen()
                            break
                        else:
                            while True:
                                urutan_paket = enumerate(json_paket["harga"][milih-1])
                                print(f"Silahkan Pilih Paket yang ingin dirubah:")
                                for nomor,kata in urutan_paket:
                                    print(f"{nomor+1}. {kata}")
                                print(f"{len(json_paket["harga"][milih-1])+1}. Kembali")
                                harga = int(input("Masukkan pilihan harga yang ingin diubah: "))
                                if harga == len(json_paket["harga"][milih-1])+1:
                                    clear_screen()
                                    break
                                elif harga >= 0 or harga < len(json_paket["harga"]):
                                    harga = input("Masukkan harga langganan (0 untuk selesai): ")
                                    lama = input("Masukkan lama bulan (0 untuk selesai): ")
                                    if harga.isdigit() and lama.isdigit():
                                        clear_screen()
                                        baru = f"Rp{harga}/{lama} Bulan"
                                        if harga == "0" or lama == "0":
                                            break
                                        else:
                                            json_paket["harga"][milih-1] = baru
                                            save_paket(json_paket)
                                            print("Harga dan Lama Langganan telah dirubah")
                                    else:
                                        clear_screen()
                                        print("Masukkan Angka yang valid")
                                        continue
                    except:
                        clear_screen()
                        print("Masukkan data seusai yang diminta!")                
            elif pilih == "3":
                while True:
                    try:
                        urutan_paket = enumerate(json_paket["jenis"])
                        print(f"Pilih Paket yang ingin diubah:")
                        for nomor,kata in urutan_paket:
                            print(f"{nomor+1}. {kata}")
                        print(f"{len(json_paket["jenis"])+1}. Kembali")
                        milih = int(input("Masukkan angka yang anda pilih: "))
                        clear_screen()
                        if milih == len(json_paket["jenis"])+1:
                            clear_screen()
                            break
                        else:
                            harga = input("Masukkan harga langganan (0 untuk selesai): ")
                            lama = input("Masukkan lama bulan (0 untuk selesai): ")
                            if harga == "" or lama == "":
                                clear_screen()
                                print("Masukkan Angka yang valid")
                                continue
                            else:
                                clear_screen()
                                baru = f"Rp{harga}/{lama} Bulan"
                                if harga == "0" or lama == "0":
                                    break
                                else:
                                    json_paket["harga"].append(baru) 
                                    save_paket(json_paket)
                    except:
                        clear_screen()
                        print("Masukkan data seusai yang diminta!")
            elif pilih == "4":
                print(update_paket(json_paket))
                break
            else:
                print("Pilihan tidak terdapat dimenu!")
        except:
            clear_screen()
            print('Masukkan Input sesuai yang diminta!')


def cancel_mem_user():
    clear_screen()
    while True:
        try:
            print("Pilih member yang akan membatalkan langganan: ")
            if len(json_user) == 1:
                print("Tidak Ada User Terdaftar!")
                enter_kembali()
                return
            else:
                for i in json_user:
                    if len(json_user) == 1:
                        print("Tidak Ada User Terdaftar!")
                        enter_kembali()
                        return
                    elif i["role"] == "admin":
                        continue
                show_user()
                pilih = int(
                    input("Masukkan angka yang dipilih (Tekan 0 untuk kembali): ")
                )
                if pilih == 0:
                    clear_screen()
                    return ""
                else:
                    hasil = cancel_user_mem(pilih)
                    clear_screen()
                    show_user()
                    enter_kembali()
                    clear_screen()
                    return hasil
        except:
            clear_screen()
            print("Pilihan tidak tersedia!")
