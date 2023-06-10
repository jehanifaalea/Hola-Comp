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

def main_menu():
    clear_screen()
    print("Main Menu:")
    print("1. Laptop")
    print("2. Aksesoris Laptop")
    print("3. Keluar")
    choice = input("Masukkan pilihan (1/2/3): ")
    if choice == '1':
        laptop_spec()
    elif choice == '2':
        accessories()
    elif choice == '3':
        print("Terima kasih telah menggunakan program kami!")
    else:
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        input("\nTekan Enter untuk kembali ke menu...")
        clear_screen()
        laptop_spec()


def laptop_spec():
    clear_screen()
    print("Tampilkan Spesifikasi Laptop yang tersedia:")
    laptop_processor()
    
def laptop_processor():
    clear_screen()
    global selected_processor 
    selected_processor = [] 
    print("Tampilkan spesifikasi laptop berdasarkan prosessor? ")
    print("1. ya")
    print("2. tidak")
    chose = input("masukkan pilihan (1/2): ")

    if chose == '1':
        print("Pilih jenis prosesor (1/2):")
        print("1. Intel")
        print("2. Ryzen")
        choice = input("Masukkan pilihan (1/2): ")
        if choice == '1':
            clear_screen()
            selected_processor = "Intel"
            input_prosesor = input("Masukkan prosesor Intel yang diinginkan: ")
            selected_processor += " " + input_prosesor  
            laptop_ram()
        elif choice == '2':
            clear_screen()
            selected_processor = "Ryzen"
            input_prosesor = input("Masukkan prosesor Ryzen yang diinginkan: ")
            selected_processor += " " + input_prosesor  
            laptop_ram()
        else:
            clear_screen()
            print("Pilihan yang Anda masukkan belum benar, coba lagi.")
            input("\nTekan Enter untuk kembali ke menu...")
            clear_screen()
    elif chose == '2':
        laptop_ram()
    else:
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_processor()


def laptop_ram():
    clear_screen()
    global selected_ram
    selected_ram = []
    print("Tampilkan spesifikasi laptop berdasarkan ram? ")
    print("1. ya")
    print("2. tidak")
    chose = input("masukkan pilihan (1/2): ")
    if chose == '1':
        print("Pilih kapasitas RAM (1/2/3/4):")
        print("1. 4 GB")
        print("2. 8 GB")
        print("3. 12 GB")
        print("4. 16 GB")
        choice = input("Masukkan pilihan (1/2/3/4): ")
        if choice == '1':
            selected_ram = "4 GB"
            clear_screen()
            laptop_rom()
        elif choice == '2':
            selected_ram = "8 GB"
            clear_screen()
            laptop_rom()
        elif choice == '3':
            selected_ram = "12 GB"
            clear_screen()
            laptop_rom()
        elif choice == '4':
            selected_ram = "16 GB"
            clear_screen()
            laptop_rom()
        else:
            clear_screen()
            print("Pilihan yang Anda masukkan belum benar, coba lagi.")
            laptop_rom()
    elif chose == '2':
        laptop_rom()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_ram()


def laptop_rom():
    clear_screen()
    global selected_rom  
    selected_rom = []
    print("Tampilkan spesifikasi laptop berdasarkan rom? ")
    print("1. ya")
    print("2. tidak")
    chose = input("masukkan pilihan (1/2): ")
    if chose == '1':
        print("Pilih kapasitas ROM (1/2/3):")
        print("1. 256 GB")
        print("2. 512 GB")
        print("3. 1024 GB")
        choice = input("Masukkan pilihan (1/2/3): ")
        if choice == '1':
            selected_rom = "256 GB"
            clear_screen()
            laptop_price_range()
        elif choice == '2':
            selected_rom = "512 GB"
            clear_screen()
            laptop_price_range()
        elif choice == '3':
            selected_rom = "1024 GB"
            clear_screen()
            laptop_price_range()
        else:
            print("Pilihan yang Anda masukkan belum benar, coba lagi.")
            laptop_rom()  
    elif chose == '2':
        laptop_price_range()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_rom()


def laptop_price_range():
    global selected_price_range
    selected_price_range = []
    clear_screen()
    print("Tampilkan spesifikasi laptop berdasarkan rentang harga? ")
    print("1. ya")
    print("2. tidak")
    chose = input("masukkan pilihan (1/2): ")
    if chose == '1':
        print("Pilih rentang harga laptop (1/2/3/4):")
        print("1. 5-10 juta")
        print("2. 11-15 juta")
        print("3. 16-20 juta")
        print("4. > 20 juta")
        choice = input("Masukkan pilihan (1/2/3/4): ")
        if choice == '1':
            selected_price_range = "5000000 - 10000000"
            clear_screen()
            laptop_brand()
        elif choice == '2':
            selected_price_range = "11000000 - 15000000"
            clear_screen()
            laptop_brand()
        elif choice == '3':
            selected_price_range = "16000000 - 20000000"
            clear_screen()
            laptop_brand()
        elif choice == '4':
            selected_price_range = "> 20000000"
            clear_screen()
            laptop_brand()
        else:
            clear_screen()
            print("Pilihan yang Anda masukkan belum benar, kembali ke menu awal.")
            laptop_price_range()  
    elif chose == '2':
        laptop_brand()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_price_range()
        

def laptop_brand():
    global selected_brand
    selected_brand = ""
    clear_screen()
    print("Tampilkan spesifikasi laptop berdasarkan merk? ")
    print("1. ya")
    print("2. tidak")
    chose = input("masukkan pilihan (1/2): ")
    if chose == '1':
        print("Pilih merk laptop (1/2/3/4/5/6):")
        print("1. Asus")
        print("2. Acer")
        print("3. Lenovo")
        print("4. HP")
        print("5. Dell")
        choice = input("Masukkan pilihan (1/2/3/4/5/6): ")
        if choice == '1':
            selected_brand = "Asus"
            clear_screen()
            laptop_recommendation()
        elif choice == '2':
            selected_brand = "Acer"
            clear_screen()
            laptop_recommendation()
        elif choice == '3':
            selected_brand = "Lenovo"
            clear_screen()
            laptop_recommendation()
        elif choice == '4':
            selected_brand = "HP"
            clear_screen()
            laptop_recommendation()
        elif choice == '5':
            selected_brand = "Dell"
            clear_screen()
            laptop_recommendation()
        else:
            clear_screen()
            print("Pilihan yang Anda masukkan belum benar, coba lagi.")
            laptop_brand()
    elif chose == '2':
        laptop_recommendation()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_brand()

def laptop_recommendation(spec, price, brand):
    laptops = pd.read_csv('data laptop.csv')

    filtered_laptops = laptops[
        (laptops['merk'] == brand) |
        (laptops['prosesor'] == spec) |
        (laptops['ram'] == selected_ram) |
        (laptops['rom'] == selected_rom) |
        (laptops['harga'] == price)
    ]

    if not filtered_laptops.empty:
        print("Berikut adalah rekomendasi laptop:")
        print(filtered_laptops)
    else:
        print("Maaf, tidak ditemukan laptop yang sesuai dengan kriteria Anda.")

def accessories():
    clear_screen()
    print("Tampilkan macam - macam aksesoris? ")
    print("1. ya")
    print("2. tidak")
    chose = input("masukkan pilihan (1/2): ")
    if chose == '1':
        print("Pilih aksesoris (1/2/3/4):")
        print("1. tas")
        print("2. keyboard")
        print("3. headset")
        print("4. mouse")
        choice = input("Masukkan pilihan (1/2/3/4): ")
        if choice == '1':
            selected_accessories = "tas"
            clear_screen()
            menu_accessories()
        elif choice == '2':
            selected_accessories = "keyboard"
            clear_screen()
            menu_accessories()
        elif choice == '3':
            selected_accessories = "headset"
            clear_screen()
            menu_accessories()
        elif choice == '4':
            selected_price_range = "mouse"
            clear_screen()
            menu_accessories()
        else:
            clear_screen()
            print("Pilihan yang Anda masukkan belum benar, kembali ke menu awal.")
            laptop_price_range()  
    elif chose == '2':
        laptop_brand()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_price_range()
    
def menu_accessories(brand, name, price):
    aksesoris = pd.read_csv('data_aksesoris.csv')

    filtered_aksesoris = aksesoris[
        (aksesoris['merk'] == brand) |
        (aksesoris['nama'] == name) |
        (aksesoris['harga'] == price)
    ]

    if not filtered_aksesoris.empty:
        print("Berikut adalah rekomendasi laptop:")
        print(filtered_aksesoris)
    else:
        print("Maaf, tidak ditemukan laptop yang sesuai dengan kriteria Anda.")



def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

welcome_message()

choice = input("Menu: \n1. Login \n2. Sign Up \n3. Exit \nPilih menu (1/2/3): ")
clear_screen()

if choice == '1':
    if login():
        clear_screen()
        main_menu()
        
        
elif choice == '2':
    if sign_up():
        clear_screen()
        laptop_spec()
elif choice == '3':
    clear_screen()
    print("Terima kasih telah menggunakan program kami!")
        
else:
    print("Pilihan tidak valid!")
