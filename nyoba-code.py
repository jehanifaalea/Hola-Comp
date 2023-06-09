import csv

def welcome_message():
    print("Selamat datang di Aplikasi Toko Laptop!")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan passw1ord: ")

    with open('akun1.csv', 'r') as file:
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

    with open('akun1.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("Akun berhasil dibuat!")
    return True

def get_laptop_data():
    laptop_data = []

    with open('data laptop.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            laptop_data.append(row)

    return laptop_data

def laptop_spec():
    clear_screen()
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
    return choice

def laptop_ram():
    clear_screen()
    print("Pilih kapasitas RAM:")
    print("1. 4 GB")
    print("2. 8 GB")
    print("3. 12 GB")
    print("4. 16 GB")

    choice = input("Masukkan pilihan: ")
    return choice

def laptop_rom():
    clear_screen()
    print("Pilih kapasitas ROM:")
    print("1. 256 GB")
    print("2. 512 GB")
    print("3. 1024 GB")

    choice = input("Masukkan pilihan: ")
    return choice

def laptop_recommendation(spesifikasi, harga, merk):
    laptops = get_laptop_data()
    recommended_laptops = []

    for laptop in laptops:
        if (
            laptop[1].lower() == merk.lower() and
            laptop[2].lower() == spesifikasi.lower() and
            int(laptop[5]) >= int(harga)
        ):
            recommended_laptops.append(laptop)

    if len(recommended_laptops) > 0:
        print("Berikut adalah rekomendasi laptop:")
        for laptop in recommended_laptops:
            print(laptop)
    else:
        print("Mohon maaf, laptop yang sesuai dengan kriteria tidak tersedia.")

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


# Main program
welcome_message()

choice = input("Menu: \n1. Login \n2. Sign Up \nPilih menu ")
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

rentang_harga = None
merk = None

while rentang_harga is None:
    clear_screen()
    print("Pilih rentang harga:")
    print("1. 5-10 juta")
    print("2. 11-15 juta")
    print("3. 16-20 juta")
    print("4. >20 juta")

    rentang_harga = input("Masukkan pilihan: ")

    if rentang_harga == '1':
        rentang_harga = '5-10 juta'
    elif rentang_harga == '2':
        rentang_harga = '11-15 juta'
    elif rentang_harga == '3':
        rentang_harga = '16-20 juta'
    elif rentang_harga == '4':
        rentang_harga = '>20 juta'
    else:
        print("Pilihan tidak valid!")

while merk is None:
    clear_screen()
    print("Pilih merk laptop:")
    print("1. Asus")
    print("2. Acer")
    print("3. HP")

    merk = input("Masukkan pilihan: ")

    if merk == '1':
        merk = 'Asus'
    elif merk == '2':
        merk = 'Acer'
    elif merk == '3':
        merk = 'HP'
    else:
        print("Pilihan tidak valid!")

laptop_recommendation(rentang_harga, merk)
