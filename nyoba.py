import csv
import pandas as pd 

def welcome_message():
    clear_screen()
    print("Selamat datang di Toko Hola-Comp!")

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

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


def laptop_spec_menu():
    clear_screen()
    print("Menu Spesifikasi Laptop:")
    print("1. Prosesor")
    print("2. RAM")
    print("3. ROM")
    print("4. Kembali ke Menu Laptop")


def laptop_recommendation(processor, ram, rom, price):
    laptops = pd.read_csv('C:/Users/USER/Documents/baru lagi/Hola-Comp/data laptop.csv')

    filtered_laptops = laptops[
        (laptops['prosesor'] == processor) &
        (laptops['ram'] == ram) &
        (laptops['rom'] == rom) &
        (laptops['harga'] == price)
    ]

    if filtered_laptops.empty:
        print("Maaf, tidak ada laptop yang cocok dengan spesifikasi yang Anda pilih.")
    else:
        print("Berikut adalah rekomendasi laptop:")
        print(filtered_laptops)

def laptop_main():
    print("Menu Laptop:")
    print("1. Tampilkan berdasarkan Spesifikasi")
    print("2. Tampilkan berdasarkan Rentang Harga")
    print("3. Tampilkan berdasarkan Merk Laptop")
    print("4. Rekomendasi Laptop")
    
    choice = input("Masukkan pilihan (1/2/3/4): ")
    
    if choice == '1':
        laptop_spec()
    elif choice == '2':
        laptop_price_range()
    elif choice == '3':
        laptop_brand()
    elif choice == '4':
        laptop_recommended()
    else:
        print("Pilihan tidak valid!")

def laptop_recommended():
    clear_screen()
    print("Masukkan spesifikasi laptop yang diinginkan:")
    processor = input("Prosesor: ")
    ram = input("RAM: ")
    rom = input("ROM: ")
    price = input("Rentang Harga: ")

    laptop_recommendation(processor, ram, rom, price)

    input("\nTekan Enter untuk kembali ke menu...")
    clear_screen()
    laptop_main()

def laptop_spec():
    laptop_spec_menu()
    choice = input("Masukkan pilihan (1/2/3/4): ")

    if choice == '1':
        laptop_processor()
    elif choice == '2':
        laptop_ram()
    elif choice == '3':
        laptop_rom()
    elif choice == '4':
        laptop_main()
    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter untuk kembali ke menu spesifikasi...")
        laptop_spec()

def laptop_processor():
    clear_screen()
    global selected_processor

    print("Pilih jenis prosesor (1/2):")
    print("1. Intel")
    print("2. Ryzen")

    choice = input("Masukkan pilihan: ")

    if choice == '1':
        clear_screen()
        selected_processor = "Intel"
        input_processor = input("Masukkan prosesor Intel yang diinginkan: ")
        selected_processor += " " + input_processor
        input("\nTekan Enter untuk kembali ke menu...")
        laptop_spec()
    elif choice == '2':
        clear_screen()
        selected_processor = "Ryzen"
        input_processor = input("Masukkan prosesor Ryzen yang diinginkan: ")
        selected_processor += " " + input_processor
        input("\nTekan Enter untuk kembali ke menu...")
        laptop_spec()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        input("\nTekan Enter untuk kembali ke menu...")
        laptop_spec()

def laptop_ram():
    clear_screen()
    global selected_ram

    print("Pilih kapasitas RAM (1/2/3/4):")
    print("1. 4 GB")
    print("2. 8 GB")
    print("3. 12 GB")
    print("4. 16 GB")

    choice = input("Masukkan pilihan (1/2/3/4): ")

    if choice == '1':
        selected_ram = "4 GB"
        clear_screen()
        print("Kapasitas RAM: 4 GB")
    elif choice == '2':
        selected_ram = "8 GB"
        clear_screen()
        print("Kapasitas RAM: 8 GB")
    elif choice == '3':
        selected_ram = "12 GB"
        clear_screen()
        print("Kapasitas RAM: 12 GB")
    elif choice == '4':
        selected_ram = "16 GB"
        clear_screen()
        print("Kapasitas RAM: 16 GB")
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")

    input("\nTekan Enter untuk kembali ke menu...")
    clear_screen()
    laptop_spec()

def laptop_rom():
    clear_screen()
    global selected_rom

    print("Pilih kapasitas ROM (1/2/3):")
    print("1. 256 GB")
    print("2. 512 GB")
    print("3. 1024 GB")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == '1':
        selected_rom = "256 GB"
    elif choice == '2':
        selected_rom = "512 GB"
    elif choice == '3':
        selected_rom = "1024 GB"
    else:
        print("Pilihan yang Anda masukkan belum benar, kembali ke menu spesifikasi.")
        input("\nTekan Enter untuk kembali ke menu...")
        clear_screen()
        laptop_spec()

    input("\nTekan Enter untuk kembali ke menu...")
    clear_screen()
    laptop_spec()

def laptop_price_range():
    clear_screen()
    print("Pilih rentang harga laptop (1/2/3/4):")
    print("1. 5-10 juta")
    print("2. 11-15 juta")
    print("3. 16-20 juta")
    print("4. > 20 juta")

    choice = input("Masukkan pilihan (1/2/3/4): ")

    # Tambahkan kode untuk memproses rentang harga laptop

def laptop_brand():
    clear_screen()
    print("Pilih merk laptop (1/2/3/4/5/6):")
    print("1. Asus")
    print("2. Acer")
    print("3. Lenovo")
    print("4. Apple")
    print("5. HP")
    print("6. Dell")

    choice = input("Masukkan pilihan (1/2/3/4/5/6): ")

    # Tambahkan kode untuk memproses merk laptop


selected_processor = ""
selected_ram = ""
selected_rom = ""

welcome_message()
choice = input("Menu: \n1. Login \n2. Sign Up \n3. Exit \nPilih menu (1/2/3): ")

while choice != '3':
    if choice == '1':
        if login():
            clear_screen()
            main_menu()
            choice = input("Pilih menu (1/2/3): ")

            while choice != '3':
                if choice == '1':
                    laptop_main()
                elif choice == '2':
                    # Tambahkan kode untuk menu aksesoris laptop
                    pass
                else:
                    print("Pilihan tidak valid!")

                input("\nTekan Enter untuk kembali ke Main Menu...")
                clear_screen()
                main_menu()
                choice = input("Pilih menu (1/2/3): ")

            clear_screen()
            print("Terima kasih telah menggunakan program kami!")
            break

    elif choice == '2':
        if sign_up():
            clear_screen()
            main_menu()
            choice = input("Pilih menu (1/2/3): ")
    else:
        print("Pilihan tidak valid!")

    clear_screen()
    welcome_message()
    choice = input("Menu: \n1. Login \n2. Sign Up \n3. Exit \nPilih menu (1/2/3): ")

clear_screen()
print("Terima kasih telah menggunakan program kami!")
