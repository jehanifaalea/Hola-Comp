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
        pilih()
    elif choice == '2':
        accessories()
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
            #clear_screen()
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
            laptop_price_range()
        elif choice == '2':
            selected_rom = 512
            clear_screen()
            laptop_price_range()
        elif choice == '3':
            selected_rom = 1024
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
    print("="*100)
    print("")

    filtered_data = data
    
    #TABEL

    if merek:
        filtered_data = filtered_data[filtered_data['merk'] == merek]
    if processor:
        filtered_data = filtered_data[filtered_data['prosesor'] == processor]
    if ram :
        filtered_data = filtered_data[filtered_data['ram'] == int(ram)]
    if rom :
        filtered_data = filtered_data[filtered_data['rom'] == int(rom)]
    if harga :
        filtered_data = filtered_data[filtered_data['harga'] == harga]
    print(filtered_data)
    print("="*100)
    nomor_laptop()


def laptop_recommendation2():
    laptops = pd.read_csv('D:/Hola Comp/Hola-Comp/data_laptop.csv')

    # Assign scores based on criteria
    condition = laptops

    if selected_processor != "":
        condition = condition[condition['prosesor'] == selected_processor]
        

    if selected_brand != "":
        condition = condition[condition['merk'] == selected_brand]
        #input("Tekan ENTER untuk melajutkan")

    if selected_ram != "":
        condition = condition[condition['ram'] == int(selected_ram)]
        #input("Tekan ENTER untuk melajutkan")

    if selected_rom != "":
        condition = condition[condition['rom'] == int(selected_rom)]
        #input("Tekan ENTER untuk melajutkan")

    if min_price > 0:
        condition = condition[condition['harga'] <= max_price]
        condition = condition[condition['harga'] >= min_price]
        input("Tekan ENTER untuk melanjutkan")

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


#TAMBAH SHOPPING CART    
def menu_accessories():
    clear_screen()
    aksesoris = pd.read_csv('D:/Hola Comp/Hola-Comp/data_aksesoris.csv')
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
        print("Berikut adalah rekomendasi laptop:")
        print(conditions)
        print("="*100)
        beli_aksesoris()
        #SAMA
    else:
        print("Maaf, tidak ditemukan laptop yang sesuai dengan kriteria Anda. \Lakuan pemilihan laptop ulang")
        input("Tekan ENTER untuk melajutkan")
        pilih()

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

nolap = ""
def nomor_laptop():
    global nolap
    print('Tekan ENTER untuk melanjutkan')
    chose = input("")
    if chose == '':
        nomor_laptop = input("Masukkan nomor laptop yang akan dibeli: ")
        nomor_laptop = int(nomor_laptop)
        if 1 <= nomor_laptop <= len(nolap):
             laptop = nolap[nomor_laptop - 1]
             print("Laptop ditemukan.")
             harga_laptop = int(laptop['Harga'])
             harga_aksesoris = beli_aksesoris()
             metode_pengiriman(harga_laptop, harga_aksesoris, laptop)
             accessories()
        else:
             print("Nomor laptop tidak valid.")

def beli_aksesoris():
    print("\n--- Beli Aksesoris ---")
    menu_accessories(aksesoris)
    pilihan_aksesoris = input("Masukkan nomor aksesoris yang akan dibeli (0 jika tidak membeli): ")
    if pilihan_aksesoris == '0':
        return 0
    elif pilihan_aksesoris.isdigit():
        pilihan_aksesoris = int(pilihan_aksesoris)
        if 1 <= pilihan_aksesoris <= len(aksesoris):
            aksesoris = aksesoris[pilihan_aksesoris - 1]
            harga_aksesoris = int(aksesoris['Harga'])
            print("Aksesoris ditemukan.")
            return harga_aksesoris
        else:
            print("Nomor aksesoris tidak valid.")
    else:
        print("Nomor aksesoris tidak valid.")
    return 0

def metode_pengiriman(harga_laptop, harga_aksesoris, nama_pelanggan, laptop, alamat, no_hp):
    print("\n--- Metode Pengiriman ---")
    print("Pilihan:")
    print("1. Pengiriman dengan kurir")
    print("2. Ambil langsung di toko")

    pilihan_pengiriman = input("Masukkan pilihan (1/2): ")
    if pilihan_pengiriman == '1':
        biaya_pengiriman = 5000
        informasi_pengiriman = f"Alamat: {alamat}, No. HP: {no_hp}"
        metode_pembayaran(nama_pelanggan, laptop, harga_laptop, harga_aksesoris, informasi_pengiriman, biaya_pengiriman)
    elif pilihan_pengiriman == '2':
        informasi_pengiriman = "Ambil langsung di toko"
        biaya_pengiriman = 0
        metode_pembayaran(nama_pelanggan, laptop, harga_laptop, harga_aksesoris, informasi_pengiriman, biaya_pengiriman)
    else:
        print("Pilihan tidak valid.")

def metode_pembayaran(nama_pelanggan, laptop, harga_laptop, harga_aksesoris, informasi_pengiriman, biaya_pengiriman):
    print("\n--- Metode Pembayaran ---")
    print("Pilihan:")
    print("1. Transfer Bank/E-Wallet")
    print("2. Cash On Delivery (COD)")

    pilihan_pembayaran = input("Masukkan pilihan (1/2): ")
    if pilihan_pembayaran == '1':
        print("Silakan transfer ke rekening bank berikut:")
        print("Bank: XXXX")
        print("Nomor Rekening: XXXX")
        print("QR code: XXXX")
        print("Jumlah yang harus ditransfer: Rp{:,}".format(harga_laptop + harga_aksesoris + biaya_pengiriman))
        print("Konfirmasi pembayaran dengan mengirimkan bukti transfer.")
        tampilkan_struk(nama_pelanggan, laptop, harga_laptop, harga_aksesoris, informasi_pengiriman, biaya_pengiriman)
    elif pilihan_pembayaran == '2':
        tampilkan_struk(nama_pelanggan, laptop, harga_laptop, harga_aksesoris, informasi_pengiriman, biaya_pengiriman)
    else:
        print("Pilihan tidak valid.")

def tampilkan_struk(nama_pelanggan, laptop, harga_laptop, harga_aksesoris, informasi_pengiriman, biaya_pengiriman):
    total_harga = harga_laptop + harga_aksesoris + biaya_pengiriman
    print("==================================")
    print("            HOLA COMP")
    print("        Struk Pembelian")
    print("==================================")
    print("Nama Pelanggan:", nama_pelanggan)
    print("Merk Laptop:", laptop['Merk'])
    print("Tipe Laptop:", laptop['Tipe'])
    print("Harga Laptop: Rp{:,}".format(harga_laptop))
    if harga_aksesoris > 0:
        print("Harga Aksesoris: Rp{:,}".format(harga_aksesoris))
    print("Informasi Pengiriman:", informasi_pengiriman)
    print("Biaya Pengiriman: Rp{:,}".format(biaya_pengiriman))
    print("==================================")
    print("Total Harga: Rp{:,}".format(total_harga))
    print("==================================")
    print("Terima kasih telah berbelanja di Hola Comp🙏")

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
            selected_accessories = "tas"
            #clear_screen()
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
            shopping()

        elif choice == '3':
            selected_accessories = "headset"
            #clear_screen()
            menu_accessories()
        elif choice == '4':
            selected_accessories = "mouse"
            #clear_screen()
            menu_accessories()
        else:
            #clear_screen()
            print("Pilihan yang Anda masukkan belum benar, kembali ke menu awal.")
            laptop_price_range()  
    elif chose == '2':
        print("Pilih laptop lagi?:")
        print("1. Ya")
        print("2. Tidak")
        laptop_brand()
    else:
        #clear_screen()
        print("Pilihan yang Anda masukkan belum benar, coba lagi.")
        laptop_price_range()

import json

# Fungsi untuk menampilkan isi shopping cart
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

# Fungsi untuk menambahkan item ke shopping cart
def tambahkan_ke_keranjang(keranjang, nama, tipe, harga):
    item = {
        'nama': nama,
        'tipe': tipe,
        'harga': harga
    }
    keranjang.append(item)

    # Menyimpan data ke file JSON
    with open('keranjang.json', 'w') as file:
        json.dump(keranjang, file)

    print(f"{nama} telah ditambahkan ke keranjang.")

# Fungsi untuk memuat data dari file JSON
def muat_keranjang():
    try:
        with open('keranjang.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main program
keranjang = muat_keranjang()

def shopping():
    laptop_recommendation2()
    print("===================================== Toko Halo Comp ==================================")
    print("1. Tampilkan Shopping Cart")
    print("2. Tambahkan Produk ke Shopping Cart")
    print("3. Keluar")
    while True :
        pilihan = input("Masukkan pilihan (1/2/3): ")
        if pilihan == '1':
            tampilkan_keranjang(keranjang)
            input("Tekan ENTER jika ingin kembali ke Shopping Chart")
            clear_screen()
            shopping()
        elif pilihan == '2':
            nama = input("Masukkan nama produk: ")
            tipe = input("Masukkan tipe produk: ")
            harga = float(input("Masukkan harga produk: "))
            tambahkan_ke_keranjang(keranjang, nama, tipe, harga)
            shopping()
        elif pilihan == '3':
            clear_screen()
            exit()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        print()


def main():
        welcome_message()
        choice = input("Menu: \n1. Login \n2. Sign Up \nPilih menu (1/2): ")
        #clear_screen()
        
        if choice == '1':
            clear_screen()
            login()
            
            
        elif choice == '2':
            clear_screen()
            sign_up()
            #laptop_spec()
            
        else:
            print("Pilihan tidak valid!")
        

def pilih():
    clear_screen()
    print("Anda ingin membeli laptop atas rekomendasi kami atau ngisi manual?")
    print("Menu: \n1. Filtering \n2. Manual")
    milih = input("Masukkan pilihan (1/2): ")
    if milih == '1':
            laptop_processor()
            clear_screen()
    
    elif milih == '2':
            laptop_recommendation()
            clear_screen()      
    else:
        print("Pilihan tidak valid!!!!!!!!!!!!!!")

def welcome_message():
    clear_screen()
    print("===================== WELCOME =====================")
    print("        Selamat datang di Toko Hola-Comp!")
    print("===================================================")
#welcome_message()
        
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
                #main_menu(username)
                return True
            print("Username atau password salah. ")
        if login():
                clear_screen()
        #welcome_message()
        #main_menu()
                return False
#login()


def sign_up():
    welcome_message()
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    with open('akun.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        print("Akun berhasil dibuat!")
        pilih()
        return True

    with open('akun.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                print("Username sudah terdaftar.")
                if sign_up():
                    clear_screen()
                    main()
                return False



username = ""
#sign_up()




main()
#if __name__ == '__main__':
#    main()
