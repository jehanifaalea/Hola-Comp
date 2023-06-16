import csv
import pandas as pd

def welcome_message():
    clear_screen()
    print("===================== WELCOME =====================")
    print("        Selamat datang di Toko Hola-Comp!")
    print("===================================================")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    with open('akun.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login berhasil!")
                main_menu(username)
                return True

    print("Username atau password salah. ")
    if login():
        clear_screen()
        welcome_message()
        main_menu()
    return False

def sign_up():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    with open('akun.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                print("Username sudah terdaftar.")
                if sign_up():
                    clear_screen()
                    main()
                return False
    with open('akun.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        print("Akun berhasil dibuat!")
        return True 

username = ""

def main_menu(username):
    clear_screen()
    print("===================== WELCOME =====================")
    print("             Selamat datang",username)
    print("===================================================")
    print("Main Menu:")
    print("1. Laptop")
    print("2. Aksesoris Laptop")
    print("3. Log Out")
    choice = input("Masukkan pilihan (1/2/3): ")
    if choice == '1':
        laptop_spec()
    elif choice == '2':
        accessories()
    elif choice == '3':
        clear_screen()
        print("Terima kasih telah menggunakan program kami!")
        login()
    else:
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        input("\nTekan Enter untuk kembali ke menu...")
        clear_screen()
        laptop_spec()


def laptop_spec():
    clear_screen()
    print("Tampilkan Spesifikasi Laptop yang tersedia:")
    laptop_processor()

selected_processor = ""
selected_ram = 0
selected_rom = 0
max_price = 0
min_price = 0
selected_brand = ""

    
def laptop_processor():
    clear_screen()
    global selected_processor 
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
            input_prosesor = print("Masukkan prosesor Intel yang diinginkan: \n1. Intel i3 \n2. Intel i5 \n3. Intel core i3 \n4. Intel core i5 \n5. Intel core i7 \n6. Intel core i9 \n7. Intel UHD Graphics 600")
            prosesor_intel = input("Masukkan pilihan (1/2/3/4/5/6/7): ")
            if prosesor_intel == '1':
                selected_processor = 'Intel i3'
                clear_screen()
                laptop_ram()
            if prosesor_intel == '2':
                selected_processor = 'Intel i5'
                clear_screen()
                laptop_ram()
            if prosesor_intel == '3':
                selected_processor = 'Intel core i3'
                clear_screen()
                laptop_ram()
            if prosesor_intel == '4':
                selected_processor = 'Intel core i5'
                clear_screen()
                laptop_ram()
            if prosesor_intel == '5':
                selected_processor = 'Intel core i7'
                clear_screen()
                laptop_ram()
            if prosesor_intel == '6': 
                selected_processor = 'Intel core i9'
                clear_screen()
                laptop_ram()
            if prosesor_intel == '7':
                selected_processor = 'Intel UHD Graphics 600'
                clear_screen()
                laptop_ram()
        elif choice == '2':
            clear_screen()
            selected_processor = "Ryzen"
            input_prosesor = print("Masukkan prosesor Ryzen yang diinginkan: \n1. AMD Ryzen 5600H \n2. AMD Ryzen 5 \n3. AMD Ryzen 7")
            prosesor_ryzen = input("Masukkan pilihan(1/2): ")
            if prosesor_ryzen == '1':
                selected_processor = 'AMD Ryzen 5600H'
                clear_screen
                laptop_ram()
            if prosesor_ryzen == '2':
                selected_processor = 'AMD Ryzen 5'
                clear_screen
                laptop_ram
            if prosesor_ryzen == '3':
                selected_processor = 'AMD Ryzen 7'
                clear_screen
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

def laptop_recommendation():
    data = pd.read_csv('D:/Hola Comp/Hola-Comp/data_laptop.csv')

    merek = input("Masukkan merek laptop (atau tekan Enter untuk melewati): ")
    processor = input("Masukkan processor (atau tekan Enter untuk melewati): ")
    ram = input("Masukkan RAM (atau tekan Enter untuk melewati): ")
    rom = input("Masukkan ROM (atau tekan Enter untuk melewati): ")
    harga = input("Masukkan Rentang Harga (atau tekan Enter untuk melewati): ")

    filtered_data = data
    if merek:
        filtered_data = filtered_data[filtered_data['merk'] == merek]
    if processor:
        filtered_data = filtered_data[filtered_data['prosesor'] == processor]
    if ram :
        filtered_data = filtered_data[filtered_data['ram'] == ram]
    if rom :
        filtered_data = filtered_data[filtered_data['rom'] == processor]
    if harga :
        filtered_data = filtered_data[filtered_data['harga'] == harga]
    print(filtered_data)


def laptop_brand():
    global selected_brand
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
            laptop_recommendation()
            accessories()
        elif choice == '2':
            selected_brand = "Acer"
            laptop_recommendation()
            accessories()
        elif choice == '3':
            selected_brand = "Lenovo"
            laptop_recommendation()
            accessories()
        elif choice == '4':
            selected_brand = "HP"
            laptop_recommendation()           
            accessories()
        elif choice == '5':
            selected_brand = "Dell"
            laptop_recommendation()
            accessories()
        else:
            clear_screen()
            print("Pilihan yang Anda masukkan belum benar, coba lagi.")
            laptop_brand()
    elif chose == '2':
        laptop_recommendation()
        accessories()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_brand()


#def laptop_recommendation():
    data = pd.read_csv('D:/Hola Comp/Hola-Comp/data_laptop.csv')

    merek = input("Masukkan merek laptop (atau tekan Enter untuk melewati): ")
    processor = input("Masukkan processor (atau tekan Enter untuk melewati): ")
    ram = input("Masukkan RAM (atau tekan Enter untuk melewati): ")
    rom = input("Masukkan ROM (atau tekan Enter untuk melewati): ")
    harga = input("Masukkan Rentang Harga (atau tekan Enter untuk melewati): ")

    filtered_data = data
    if merek:
        filtered_data = filtered_data[filtered_data['merk'] == merek]
    if processor:
        filtered_data = filtered_data[filtered_data['prosesor'] == processor]
    if ram :
        filtered_data = filtered_data[filtered_data['ram'] == ram]
    if rom :
        filtered_data = filtered_data[filtered_data['rom'] == processor]
    if harga :
        filtered_data = filtered_data[filtered_data['harga'] == harga]
    print(filtered_data)

    

selected_accessories = ""

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
            selected_accessories = "mouse"
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
    
def menu_accessories():
    aksesoris = pd.read_csv('D:/Hola Comp/Hola-Comp/data_aksesoris.csv')
    conditions = aksesoris

    if selected_accessories != "":
        conditions = conditions[conditions['nama'] == selected_accessories]
    if selected_accessories != "":
        conditions = conditions[['merek'] == selected_accessories]
    if selected_accessories != "":
        conditions = conditions[['harga'] == selected_accessories]

    if not conditions.empty:
        print("Berikut adalah rekomendasi laptop:")
        print(conditions)
    else:
        print("Maaf, tidak ditemukan laptop yang sesuai dengan kriteria Anda.")


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    welcome_message()
    choice = input("Menu: \n1. Login \n2. Sign Up \nPilih menu (1/2): ")
    clear_screen()
    
    if choice == '1':
        clear_screen()
        main()
        
        
    elif choice == '2':
        clear_screen()
        sign_up()
        laptop_spec()
        
    else:
        print("Pilihan tidak valid!")


if __name__ == '__main__':
    main()
