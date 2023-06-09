import csv
import pandas as pd

def welcome_message():
    clear_screen()
    print("Selamat datang di Toko Hola-Comp!")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    with open('akun.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login berhasil!")
                return True

    print("Username atau password salah.")
    return False

def sign_up():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    with open('akun.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("Akun berhasil dibuat!")
    return True

def laptop_spec():
    print("Pilih spesifikasi laptop:")
    print("1. Prosesor")
    print("2. RAM")
    print("3. ROM")

    choice = input("Masukkan pilihan: ")

    if choice == '1':
        laptop_processor()
    elif choice == '2':
        laptop_ram()
    elif choice == '3':
        laptop_rom()
    else:
        print("Pilihan tidak valid!")

def laptop_processor():
    clear_screen()
    print("Pilih jenis prosesor:")
    print("1. Intel")
    print("2. Ryzen")

    choice = input("Masukkan pilihan: ")
    

def laptop_ram():
    clear_screen()
    print("Pilih kapasitas RAM:")
    print("1. 4 GB")
    print("2. 8 GB")
    print("3. 12 GB")
    print("4. 16 GB")

    choice = input("Masukkan pilihan: ")
   

def laptop_rom():
    clear_screen()
    print("Pilih kapasitas ROM:")
    print("1. 256 GB")
    print("2. 512 GB")
    print("3. 1024 GB")

    choice = input("Masukkan pilihan: ")


def laptop_recommendation(spec, price, brand):
  
    laptops = pd.read_csv('data_laptop.csv')

   
    filtered_laptops = laptops[
        (laptops['Spesifikasi'] == spec) &
        (laptops['Rentang Harga'] == price) &
        (laptops['Merk'] == brand)
    ]

    print("Berikut adalah rekomendasi laptop:")
    print(filtered_laptops)

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')



welcome_message()

choice = input("Menu: \n1. Login \n2. Sign Up \nPilih menu: ")
clear_screen()

if choice == '1':
    if login():
        clear_screen()
        laptop_spec()
        
elif choice == '2':
    if sign_up():
        clear_screen()
        laptop_spec()
        
else:
    print("Pilihan tidak valid!")
