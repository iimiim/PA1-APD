from load_data import json_paket
import os

data = {
    "jenis": ["Single", "Couple"],
    "harga": [
            [
                "Rp 350.000/Bulan",
                "Rp 650.000/2 Bulan",
                "Rp 950.000/3 Bulan",
                "Rp 1.750.000/6 Bulan",
                "Rp 3.000.000/1 Tahun"
            ],
            [
                "Rp 650.000/Bulan",
                "Rp 1.000.000/2 Bulan",
                "Rp 1.600.000/3 Bulan",
                "Rp 3.000.000/6 Bulan",
                "Rp 5.500.000/1 Tahun"
            ]  
            ]
}

def create_paket(data):
    jenis = input("Masukkan jenis paket (0 untuk kembali): ")
    if jenis == "0":
        return ""
    else:
        data["jenis"].append(jenis)
        daf_harga = []
        while True:
            for i in daf_harga:
                print(i)
            harga = input("Masukkan harga langganan (0 untuk selesai): ")
            lama = input("Masukkan lama bulan (0 untuk selesai): ")
            if harga == "" or lama == "":
                os.system("cls")
                print("Masukkan Angka yang valid")
                continue
            else:
                os.system("cls")
                baru = f"Rp{harga}/{lama} Bulan"
                if harga == "0" or lama == "0":
                    break
                else:
                    daf_harga.append(baru)
        data["harga"].append(daf_harga)
        return data
    
print(create_paket(data))

pilih = int(input("Masukkan pilihan paket: "))
pilih2 = int(input("Masukkan pilihan harga: "))
if pilih >= 0 or pilih < len(data["harga"]):
    print(data["harga"][pilih][pilih2])

def buy():
    while True:
        if user["langganan"] != None:
            pilih = paket()
            while True:
                harga = int(input("Masukkan pilihan harga: "))
                if pilih >= 0 or pilih < len(data["harga"]):
                    print(data["harga"][pilih][harga])