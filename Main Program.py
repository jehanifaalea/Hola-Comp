from datetime import datetime, timedelta
import json
import csv
import pandas as pd

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
        accessories1()
    elif choice == '3':
        clear_screen()
        print("Terima kasih telah menggunakan program kami!")
        main()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        input("\nTekan Enter untuk kembali ke menu...")
        laptop_spec()
        

def laptop_spec():
    clear_screen()
    print("Tampilkan Spesifikasi Laptop yang tersedia:")
    laptop_processor()

selected_processor = ""
selected_ram = ""
selected_rom = ""
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
                clear_screen()
                laptop_ram()
            if prosesor_ryzen == '2':
                selected_processor = 'AMD Ryzen 5'
                clear_screen()
                laptop_ram
            if prosesor_ryzen == '3':
                selected_processor = 'AMD Ryzen 7'
                clear_screen()
                laptop_ram()
        else:
            clear_screen()
            print("Pilihan yang Anda masukkan belum benar, coba lagi.")
            input("\nTekan Enter untuk kembali ke menu...")
    elif chose == '2':
        laptop_ram()
    else:
        clear_screen()
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
            selected_ram = 4
            clear_screen()
            laptop_rom()
        elif choice == '2':
            selected_ram = 8
            clear_screen()
            laptop_rom()
        elif choice == '3':
            selected_ram = 12
            clear_screen()
            laptop_rom()
        elif choice == '4':
            selected_ram = 16
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
            selected_rom = 256
            clear_screen()
            laptop_brand()
        elif choice == '2':
            selected_rom = 512
            clear_screen()
            laptop_brand()
        elif choice == '3':
            selected_rom = 1024
            clear_screen()
            laptop_brand()
        else:
            print("Pilihan yang Anda masukkan belum benar, coba lagi.")
            laptop_rom()  
    elif chose == '2':
        laptop_brand()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_rom()
 

def laptop_recommendation2():
    laptops = pd.read_csv('data_laptop.csv')

    condition = laptops

    if selected_processor != "":
        condition = condition[condition['prosesor'] == selected_processor]
        

    if selected_brand != "":
        condition = condition[condition['merk'] == selected_brand]

    if selected_ram != "":
        condition = condition[condition['ram'] == int(selected_ram)]

    if selected_rom != "":
        condition = condition[condition['rom'] == int(selected_rom)]

    if not condition.empty:
        clear_screen()
        print("Berikut adalah rekomendasi laptop:")
        print("="*100)
        
        print(condition[['merk', 'tipe', 'ram', 'rom', 'prosesor','harga']])
    else:
        print("Maaf, tidak ditemukan laptop yang sesuai dengan kriteria Anda.")


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
            laptop_recommendation2()
            print("="*100)
            input("Tekan ENTER untuk melajutkan")
            accessories()
        elif choice == '2':
            selected_brand = "Acer"
            laptop_recommendation2()
            print("="*100)
            input("Tekan ENTER untuk melajutkan")
            accessories()
        elif choice == '3':
            selected_brand = "Lenovo"
            laptop_recommendation2()
            print("="*100)
            input("Tekan ENTER untuk melajutkan")
            accessories()
        elif choice == '4':
            selected_brand = "HP"
            laptop_recommendation2()
            print("="*100)
            input("Tekan ENTER untuk melajutkan")         
            accessories()
        elif choice == '5':
            selected_brand = "Dell"
            laptop_recommendation2()
            print("="*100)
            input("Tekan ENTER untuk melajutkan")
            accessories()
        else:
            clear_screen()
            print("Pilihan yang Anda masukkan belum benar, coba lagi.")
            laptop_brand()
    elif chose == '2':
        laptop_recommendation2()
        print("="*100)
        input("Tekan ENTER untuk melajutkan")
        accessories()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_brand()
   
def menu_accessories():
    global aksesoris
    aksesoris = pd.read_csv('data_aksesoris.csv')
    aksesoris = pd.read_csv('Keyboard.csv')
    aksesoris = pd.read_csv('mouse.csv')
    aksesoris = pd.read_csv('tas.csv')
    aksesoris = pd.read_csv('headset.csv')
    print("="*100)
    
    conditions = aksesoris

    if selected_accessories != "":
        conditions = conditions[conditions['nama'] == selected_accessories]
        print("="*100)
        input("Tekan ENTER untuk melanjutkan")
    elif selected_accessories != "":
        conditions = conditions[['merek'] == selected_accessories]
        print("="*100)
        input("Tekan ENTER untuk melanjutkan")
    elif selected_accessories != "":
        conditions = conditions[['harga'] == selected_accessories]
        print("="*100)
        input("Tekan ENTER untuk melanjutkan")
    elif not conditions.empty:
        print("Berikut adalah rekomendasi Accessories:")
        print(conditions)
        print("="*100)
    else:
        print("Maaf, tidak ditemukan laptop yang sesuai dengan kriteria Anda. \Lakuan pemilihan laptop ulang")
        input("Tekan ENTER untuk melajutkan")
        laptop_spec()

def exit():
    clear_screen()
    print("===================== T H A N K Y O U",(username), "=====================")
    print("Main Menu:")
    print("1. Belanja lagi")
    print("2. Log Out")
    choice = input("Masukkan pilihan (1/2): ")
    if choice == '1':
        main_menu(username)
    elif choice == '2':
        main()
    else:
        clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        input("\nTekan Enter untuk kembali ke menu...")
        laptop_spec()

def metode_pengiriman():
    global biaya_pengiriman
    global alamat
    global nama_pelanggan
    global no_hp
    print("Pilihan")
    print("1. Pengiriman dengan kurir")
    print("2. Ambil langsung di toko")
    pilihan_pengiriman = input("Masukkan pilihan (1/2): ")
    
    if pilihan_pengiriman == '1':
        print("Anda memilih metode pengiriman dengan kurir")
        nama_pelanggan = input("Masukkan Nama Anda : ")
        jarak = float(input("Masukkan Jarak Alamat Pengiriman (km): "))
        alamat = input("Masukkan Alamat Anda : ")
        no_hp = int(input("Masukkan No HP Anda : "))
        biaya_pengiriman = 2000 * jarak
        metode_pembayaran()
    elif pilihan_pengiriman == '2':
        # Lakukan proses pengiriman dengan ambil langsung di toko
        print("Anda memilih metode pengiriman ambil langsung di toko")
        nama_pelanggan = input("Masukkan Nama Anda : ")
        no_hp = int(input("Masukkan No HP Anda : "))
        alamat = input("Masukkan Alamat Anda : ")
        biaya_pengiriman = 0
        metode_pembayaran()
    else:
        print("Pilihan yang Anda masukkan tidak valid.")


def metode_pembayaran():
    print("=================== Metode Pembayaran ==============")
    print("Pilihan:")
    print("1. Transfer Bank")
    print("2. COD")
    
    pilihan_pembayaran = input("Masukkan pilihan (1/2): ")
    
    # Lakukan operasi sesuai pilihan pembayaran
    if pilihan_pembayaran == '1':
        print("Anda memilih metode pembayaran Transfer Bank")
        print("Silakan transfer ke rekening bank berikut:")
        print("Bank: BNI")
        print("Nomor Rekening: 1400672548 a/n Toko Hola Comp")
        print("Jumlah yang harus ditransfer: Rp{:,}".format(harga_laptop + harga_aksesoris + biaya_pengiriman))
        print("Konfirmasi pembayaran dengan mengirimkan bukti transfer.")
        input("Tekan ENTER untuk melanjutkan")
        clear_screen()
        tampilkan_struk()
    elif pilihan_pembayaran == '2':
        print("Anda memilih COD")
        tampilkan_struk1()
    else:
        print("Pilihan yang Anda masukkan tidak valid.")


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

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
            tas = pd.read_csv('tas.csv')
            selected_accessories = "tas"
            print("="*100)
            print("Berikut Rekomendasi Tas:")
            print(tas)
            input("Tekan ENTER untuk melanjutkan")
            clear_screen()
            shopping()
        elif choice == '2':
            selected_accessories = "keyboard"
            print("="*100)
            key = pd.read_csv('Keyboard.csv')
            print("Berikut Rekomendasi Keyboard:")
            print(key)
            print("="*100)
            input("Tekan ENTER untuk melanjutkan")
            clear_screen()
            shopping()

        elif choice == '3':
            selected_accessories = "headset"
            headset = pd.read_csv('headset.csv')
            print("Berikut Rekomendasi Headset:")
            print(headset)
            input("Tekan ENTER untuk melanjutkan")
            clear_screen()
            shopping()
        elif choice == '4':
            selected_accessories = "mouse"
            mouse = pd.read_csv('mouse.csv')
            print("Berikut Rekomendasi Mouse:")
            print(mouse)
            input("Tekan ENTER untuk melanjutkan")
            clear_screen()
            shopping()
        else:
            print("Pilihan yang Anda masukkan belum benar, kembali ke menu awal.")
            accessories()  
    elif chose == '2':
        shopping1()
    else:
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        accessories()

def accessories1():
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
            menu_accessories()
        elif choice == '2':
            selected_accessories = "keyboard"
            print("="*100)
            key = pd.read_csv('D:/Hola Comp/Hola-Comp/Keyboard.csv')
            print("Berikut Rekomendasi Keyboard:")
            print(key)
            print("="*100)
            input("Tekan ENTER untuk melanjutkan")
            clear_screen()
            shopping2()

        elif choice == '3':
            selected_accessories = "headset"
            menu_accessories()
        elif choice == '4':
            selected_accessories = "mouse"
            menu_accessories()
        else:
            print("Pilihan yang Anda masukkan belum benar, kembali ke menu awal.")
            accessories()  
    elif chose == '2':
        shopping1()
    else:
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        accessories()

import json

def tambahkan_ke_keranjang():
    global keranjang
    global tipe_laptop
    global harga_laptop
    global nama_produk
    global nama_accessories
    global tipe_accessories
    global harga_aksesoris
    nama_produk = input("Masukkan Merk Laptop (Tekan Enter Untuk Melewati): ")
    tipe_laptop = input("Masukkan Tipe laptop (Tekan Enter Untuk Melewati): ")
    harga_laptop = int(input("Harga (Tekan 0 Untuk Melewati): "))
    nama_accessories = input("masukkan Merk Aksesoris (Tekan Enter untuk Melewati): ")
    tipe_accessories = input("Masukkan Tipe Aksesoris (Tekan Enter Untuk Melewati)")
    harga_aksesoris = int(input("Masukkan Harga (Tekan 0 Untuk Melewati): "))
    keranjang = {
        'Merk Laptop': nama_produk,
        'Tipe Laptop': tipe_laptop,
        'Merk Aksesoris' : nama_accessories,
        'Tipe Aksesoris': tipe_accessories,
        'Harga': harga_laptop,
        'aksesoris': harga_aksesoris
    }

    # Menyimpan data ke file JSON
    with open('keranjang.json', 'w') as file:
        json.dump(keranjang, file)

    print(f"{nama_produk,tipe_laptop,nama_accessories,tipe_accessories} telah ditambahkan ke keranjang.")
    clear_screen()

def tampilkan_struk():
    total_harga = harga_laptop + harga_aksesoris + biaya_pengiriman
    now = datetime.now() 
    file = open("STRUK.txt","w")
    file.write(f"\nNama Pelanggan: {nama_pelanggan}\nMerk Laptop: {nama_produk}\nTipe Laptop: {tipe_laptop}\nAcessories:{nama_accessories}\nHarga Laptop:{harga_laptop}\nHarga Aksesoris:{harga_aksesoris}\n".format(nama_pelanggan,
            nama_produk,tipe_laptop,nama_accessories,harga_laptop,harga_aksesoris))
    print("=============================================================")
    print("                         HOLA COMP")
    print("                      Struk Pembelian")
    print("=============================================================")
    print(now)
    print("Nama Pelanggan:", nama_pelanggan)
    print("Merk Laptop:", nama_produk)
    print("Tipe Laptop:", tipe_laptop)
    print("Acessories:", nama_accessories)
    print("Tipe Aksesoris:",tipe_accessories)
    print("Harga Laptop: Rp{:,}".format(harga_laptop))
    if harga_aksesoris > 0:
        print("Harga Aksesoris: Rp{:,}".format(harga_aksesoris))
    print("Informasi Pengiriman:", alamat)
    print("Biaya Pengiriman: Rp{:,}".format(biaya_pengiriman))
    print("==================================")
    print("Total Harga: Rp{:,}".format(total_harga))
    print("=============================================================")
    print("Terima kasih telah berbelanja di Hola Comp🙏")
    print("=============================================================")
    input("TEKAN ENTER UNTUK KELUAR")
    exit()

def tampilkan_struk1():
    total_harga = harga_laptop + harga_aksesoris
    now = datetime.now() 
    file = open("STRUK.txt","w")
    file.write(f"\nNama Pelanggan: {nama_pelanggan}\nMerk Laptop: {nama_produk}\nTipe Laptop: {tipe_laptop}\nAcessories:{nama_accessories}\nHarga Laptop:{harga_laptop}\nHarga Aksesoris:{harga_aksesoris}\n".format(nama_pelanggan,
            nama_produk,tipe_laptop,nama_accessories,harga_laptop,harga_aksesoris))
    print("=============================================================")
    print("                         HOLA COMP")
    print("                      Struk Pembelian")
    print("=============================================================")
    print(now)
    print("Nama Pelanggan:", nama_pelanggan)
    print("Merk Laptop:", nama_produk)
    print("Tipe Laptop:", tipe_laptop)
    print("Acessories:", nama_accessories)
    print("Tipe Aksesoris:",tipe_accessories)
    print("Harga Laptop: Rp{:,}".format(harga_laptop))
    if harga_aksesoris > 0:
        print("Harga Aksesoris: Rp{:,}".format(harga_aksesoris))
    print("==================================")
    print("Total Harga: Rp{:,}".format(total_harga))
    print("=============================================================")
    print("Terima kasih telah berbelanja di Hola Comp🙏")
    print("=============================================================")
    input("TEKAN ENTER UNTUK KELUAR")
    exit()

def tampilkan_keranjang(keranjang):
    print("===============================================")
    print("Isi Shopping Cart:")
    total_harga = 0

    if not keranjang:
        print("Keranjang kosong.")
    else:
        for item in keranjang:
            print(f"Nama: {item['nama']}")
            print(f"Tipe : {item ['tipe']}")
            print(f"Harga: Rp {item['harga']}")
            total_harga += item['harga']
            print("")


    print(f"Total Harga: Rp {total_harga}")
    print("===============================================")

# Fungsi untuk memuat data dari file JSON
def muat_keranjang():
    try:
        with open('keranjang.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
    tampilkan_keranjang()
    print(muat_keranjang())

def shopping():
    clear_screen()
    laptop_recommendation2()
    menu_accessories()
    print("===================================== Toko Halo Comp ==================================")
    print("1. Tambahkan Produk ke Shopping Cart")
    print("2. Keluar")
    while True :
        pilihan = input("Masukkan pilihan (1/2): ")
       
        if pilihan == '1':
            tambahkan_ke_keranjang()
            muat_keranjang()
            metode_pengiriman()
        elif pilihan == '3':
            clear_screen()
            exit()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        print()


def shopping1():
    clear_screen()
    laptop_recommendation2()
    print("===================================== Toko Halo Comp ==================================")
    print("1. Tambahkan Produk ke Shopping Cart")
    print("2. Keluar")
    while True :
        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == '1':
            tambahkan_ke_keranjang()
            muat_keranjang()
            metode_pengiriman()
        
        elif pilihan == '2':
            clear_screen()
            exit()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        print()

def shopping2():
    clear_screen()
    menu_accessories()
    print("===================================== Toko Halo Comp ==================================")
    print("1. Tambahkan Produk ke Shopping Cart")
    print("2. Keluar")
    while True :
        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == '1':
            tambahkan_ke_keranjang()
            muat_keranjang()
            metode_pengiriman()
            
        elif pilihan == '2':
            clear_screen()
            exit()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        print()

def main():
        welcome_message()
        choice = input("Menu: \n1. Login \n2. Sign Up \nPilih menu (1/2): ")
        
        if choice == '1':
            clear_screen()
            login()
            
            
        elif choice == '2':
            clear_screen()
            sign_up()
            
        else:
            print("Pilihan tidak valid!")

def welcome_message():
    clear_screen()
    print("===================== WELCOME =====================")
    print("        Selamat datang di Toko Hola-Comp!")
    print("===================================================")
        
def login():
    global username
    welcome_message()
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
                return False

def sign_up():
    welcome_message()
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    while not (len(password)>=8 and password.isalnum()):
        print("Masukkan password minimal 8 karakter dengan kombinasi angka dan huruf")
        password = input("Masukkan kembali Password : ")

    with open('akun.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        print("Akun berhasil dibuat!")
        return True 


with open('akun.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == username:
            print("Username sudah terdaftar.")
            if sign_up():
                clear_screen()
                main()
 
    
username = ""


main()