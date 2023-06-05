from data_laptop import data_laptop

def rekomendasi_laptop():
    # Meminta input apakah pengguna ingin menampilkan berdasarkan spesifikasi
    tampilkan_spesifikasi = input("Apakah Anda ingin menampilkan berdasarkan spesifikasi? (ya/tidak): ")
    
    if tampilkan_spesifikasi.lower() == "ya":
        # Meminta input apakah pengguna ingin menampilkan berdasarkan prosesor
        tampilkan_prosesor = input("Apakah Anda ingin menampilkan berdasarkan prosesor? (ya/tidak): ")
        
        if tampilkan_prosesor.lower() == "ya":
            # Meminta input prosesor
            prosesor = input("Masukkan jenis prosesor yang diinginkan: ")
            
            # Mencari laptop berdasarkan prosesor
            laptop_rekomendasi = [laptop for laptop in data_laptop if data_laptop[laptop]['prosesor'] == prosesor]
        else:
            laptop_rekomendasi = list(data_laptop.keys())  # Menampilkan semua laptop
        
        # Meminta input apakah pengguna ingin menampilkan berdasarkan RAM
        tampilkan_ram = input("Apakah Anda ingin menampilkan berdasarkan RAM? (ya/tidak): ")
        
        if tampilkan_ram.lower() == "ya":
            # Meminta input RAM
            ram = int(input("Masukkan ukuran RAM (GB) yang diinginkan: "))
            
            # Mencari laptop berdasarkan RAM
            laptop_rekomendasi = [laptop for laptop in laptop_rekomendasi if data_laptop[laptop]['ram'] == ram]
        
        # Meminta input apakah pengguna ingin menampilkan berdasarkan ROM
        tampilkan_rom = input("Apakah Anda ingin menampilkan berdasarkan ROM? (ya/tidak): ")
        
        if tampilkan_rom.lower() == "ya":
            # Meminta input ROM
            rom = int(input("Masukkan ukuran ROM (GB) yang diinginkan: "))
            
            # Mencari laptop berdasarkan ROM
            laptop_rekomendasi = [laptop for laptop in laptop_rekomendasi if data_laptop[laptop]['rom'] == rom]
        
        # Menampilkan spesifikasi laptop yang dipilih
        print("Laptop rekomendasi berdasarkan spesifikasi:")
        for laptop in laptop_rekomendasi:
            print("- Merk:", data_laptop[laptop]['merk'])
            print("- Prosesor:", data_laptop[laptop]['prosesor'])
            print("- RAM:", data_laptop[laptop]['ram'], "GB")
            print("- ROM:", data_laptop[laptop]['rom'], "GB")
            print("- Harga:", data_laptop[laptop]['harga'])
    else:
        # Meminta input apakah pengguna ingin menampilkan berdasarkan rentang harga
        tampilkan_harga = input("Apakah Anda ingin menampilkan berdasarkan rentang harga? (ya/tidak): ")
        
        if tampilkan_harga.lower() == "ya":
            # Meminta input rentang harga
            min_harga = int(input("Masukkan harga minimum: "))
            max_harga = int(input("Masukkan harga maksimum: "))
            
            # Mencari laptop berdasarkan rentang harga
            laptop_rekomendasi = [laptop for laptop in data_laptop if min_harga <= data_laptop[laptop]['harga'] <= max_harga]
        else:
            laptop_rekomendasi = list(data_laptop.keys())  # Menampilkan semua laptop
        
        # Meminta input apakah pengguna ingin menampilkan berdasarkan merk
        tampilkan_merk = input("Apakah Anda ingin menampilkan berdasarkan merk? (ya/tidak): ")
        
        if tampilkan_merk.lower() == "ya":
            # Meminta input merk
            merk = input("Masukkan merk yang diinginkan: ")
            
            # Mencari laptop berdasarkan merk
            laptop_rekomendasi = [laptop for laptop in laptop_rekomendasi if data_laptop[laptop]['merk'] == merk]
        
        # Menampilkan spesifikasi laptop yang dipilih
        print("Laptop rekomendasi:")
        if laptop_rekomendasi:
            for laptop in laptop_rekomendasi:
                print("- Merk:", data_laptop[laptop]['merk'])
                print("- Prosesor:", data_laptop[laptop]['prosesor'])
                print("- RAM:", data_laptop[laptop]['ram'], "GB")
                print("- ROM:", data_laptop[laptop]['rom'], "GB")
                print("- Harga:", data_laptop[laptop]['harga'])
        else:
            print("Tidak ada laptop yang ditemukan sesuai dengan pilihan Anda.")

# Memanggil fungsi rekomendasi_laptop()
rekomendasi_laptop()

# biodata pelanggan
input("masukkan nama anda : ")
input("masukkan alamat anda : ")
input("masukkan nomor handphone anda : ")
