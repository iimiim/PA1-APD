import json
from prettytable import PrettyTable


# load data
def load_user():
    with open("user.json") as user_json:
        return json.load(user_json)


def load_paket():
    with open("paket.json") as paket_json:
        return json.load(paket_json)


json_user = load_user()
json_paket = load_paket()


# save data
def save_user(json_user):
    with open("user.json", "w") as user_json:
        json.dump(json_user, user_json, indent=4)


def save_paket(json_paket):
    with open("paket.json", "w") as paket_json:
        json.dump(json_paket, paket_json, indent=4)


# create data
def create_user(new_data):
    if new_data in json_user:
        return "Akun sudah terdaftar!"
    else:
        json_user.append(new_data)
        save_user(json_user)
        return "Berhasil Teregistrasi!"


def create_paket(new_data):
    if new_data == json_paket:
        save_paket(new_data)
        return "Paket berhasil ditambahkan"
    return "Tidak ada paket yang ditambahkan"


# update data
def update_user(new_data, pilih, harga):
    if new_data["langganan"] == None:
        new_data["langganan"] = json_paket["harga"][pilih][harga]
        save_user(json_user)
        return f"Terima kasih karena sudah memilih membership paket {json_paket['harga'][pilih][harga]} kami."
    else:
        return "Anda memiliki langganan yang sedang aktif!"
    
def cancel_user_mem(index):
    if json_user[index]["langganan"] != None:
        json_user[index]["langganan"] = None
        save_user(json_user)
        return f"Membership user {json_user[index]["username"]} telah dibatalkan."
    else:
        return f"User {json_user[index]["username"]} belum memiliki langganan!"
    


def update_paket(new_data):
    if new_data != json_paket:
        save_paket(new_data)
        return "Paket Telah diperbarui"
    else:
        return "Tidak ada Paket yang berubah"


# delete data
def delete_user(index):
    del json_user[index]
    save_user(json_user)


def delete_package(index):
    del json_paket["harga"][index - 1]
    save_paket(json_paket)
    del json_paket["jenis"][index - 1]
    save_paket(json_paket)
    return "Paket berhasil dihapus"

def delete_harga(pilih, milih):
    del json_paket["harga"][pilih-1][milih-1]
    save_paket(json_paket)
    return "Harga & lama Paket dihapus"


def show_user():
    table_fields = ["username", "password", "role", "langganan"]
    table = PrettyTable()
    table.padding_width = 5
    table.field_names = ["N0."] + table_fields

    for i, row in enumerate(json_user[1:], start=1):
        row_to_display = [i] + [row[col] for col in table_fields]
        table.add_row(row_to_display)

    print(table)
