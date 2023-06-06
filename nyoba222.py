from data_laptop import data_laptop

def rekomendasi_laptop():
    tampilkan_spesifikasi = input("Apakah Anda ingin menampilkan berdasarkan spesifikasi? (ya/tidak): ")
    
    if tampilkan_spesifikasi.lower() == "ya":
        tampilkan_prosesor = input("Apakah Anda ingin menampilkan berdasarkan prosesor? (ya/tidak): ")
        if tampilkan_prosesor.lower() == "ya":
            prosesor = input("Masukkan jenis prosesor yang diinginkan: ")
            laptop_rekomendasi = [laptop for laptop in data_laptop if data_laptop[laptop]['prosesor'] == prosesor]
        

        tampilkan_ram = input("Apakah Anda ingin menampilkan berdasarkan RAM? (ya/tidak): ")
        if tampilkan_ram.lower() == "ya":
            ram = int(input("Masukkan ukuran RAM (GB) yang diinginkan: "))
            laptop_rekomendasi = [laptop for laptop in data_laptop if data_laptop[laptop]['ram'] == ram]
        

        tampilkan_rom = input("Apakah Anda ingin menampilkan berdasarkan ROM? (ya/tidak): ")
        if tampilkan_rom.lower() == "ya":
            rom = int(input("Masukkan ukuran ROM (GB) yang diinginkan: "))
            laptop_rekomendasi = [laptop for laptop in data_laptop if data_laptop[laptop]['rom'] == rom]
        
        else:
            tampilkan_harga = input("Apakah Anda ingin menampilkan berdasarkan rentang harga? (ya/tidak): ")
        
            if tampilkan_harga.lower() == "ya":
                min_harga = int(input("Masukkan harga minimum: "))
                max_harga = int(input("Masukkan harga maksimum: "))
                laptop_rekomendasi = [laptop for laptop in data_laptop if min_harga <= data_laptop[laptop]['harga'] <= max_harga]
            else:
                laptop_rekomendasi = list(data_laptop.keys())  
        

            tampilkan_merk = input("Apakah Anda ingin menampilkan berdasarkan merk? (ya/tidak): ")
        
            if tampilkan_merk.lower() == "ya":
                merk = input("Masukkan merk yang diinginkan: ")
                laptop_rekomendasi = [laptop for laptop in laptop_rekomendasi if data_laptop[laptop]['merk'] == merk]
        
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

        print("Laptop rekomendasi berdasarkan spesifikasi:")
        for laptop in laptop_rekomendasi:
            print("- Merk:", data_laptop[laptop]['merk'])
            print("- Prosesor:", data_laptop[laptop]['prosesor'])
            print("- RAM:", data_laptop[laptop]['ram'], "GB")
            print("- ROM:", data_laptop[laptop]['rom'], "GB")
            print("- Harga:", data_laptop[laptop]['harga'])
    else:
        tampilkan_harga = input("Apakah Anda ingin menampilkan berdasarkan rentang harga? (ya/tidak): ")
        
        if tampilkan_harga.lower() == "ya":
            min_harga = int(input("Masukkan harga minimum: "))
            max_harga = int(input("Masukkan harga maksimum: "))
            laptop_rekomendasi = [laptop for laptop in data_laptop if min_harga <= data_laptop[laptop]['harga'] <= max_harga]
        else:
            laptop_rekomendasi = list(data_laptop.keys())  
        

        tampilkan_merk = input("Apakah Anda ingin menampilkan berdasarkan merk? (ya/tidak): ")
        
        if tampilkan_merk.lower() == "ya":
            merk = input("Masukkan merk yang diinginkan: ")
            laptop_rekomendasi = [laptop for laptop in laptop_rekomendasi if data_laptop[laptop]['merk'] == merk]
        
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

rekomendasi_laptop()
#data struk
print("======================================")
input("masukkan nama anda : ")
input("masukkan alamat anda : ")
input("masukkan nomor handphone anda : ")
