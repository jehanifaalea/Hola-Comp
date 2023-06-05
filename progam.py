import json

def baca_data_laptop():
    with open('data_laptop.json', 'r') as file:
        data = json.load(file)
    return data

def rekomendasi_laptop():
    data_laptop = baca_data_laptop()
    
    # Meminta input spesifikasi laptop
    jenis_prosesor = input("Masukkan jenis prosesor yang diinginkan: ")
    ram = int(input("Masukkan ukuran RAM (GB) yang diinginkan: "))
    rom = int(input("Masukkan ukuran ROM (GB) yang diinginkan: "))
    rentang_harga = int(input("Masukkan rentang harga yang diinginkan: "))
    merk = input("Masukkan merk yang diinginkan: ")
    
    # Mencari laptop yang sesuai dengan spesifikasi
    laptop_rekomendasi = []
    for laptop in data_laptop:
        spesifikasi = data_laptop[laptop]
        if (
            (jenis_prosesor == spesifikasi['prosesor'] or jenis_prosesor == '') and
            (ram == spesifikasi['ram'] or ram == 0) and
            (rom == spesifikasi['rom'] or rom == 0) and
            (rentang_harga >= spesifikasi['harga'] or rentang_harga == 0) and
            (merk == spesifikasi['merk'] or merk == '')
        ):
            laptop_rekomendasi.append(laptop)
    
    # Menampilkan daftar laptop rekomendasi
    print("Laptop rekomendasi:")
    for laptop in laptop_rekomendasi:
        print("- Merk:", data_laptop[laptop]['merk'])
        print("- Prosesor:", data_laptop[laptop]['prosesor'])
        print("- RAM:", data_laptop[laptop]['ram'], "GB")
        print("- ROM:", data_laptop[laptop]['rom'], "GB")
        print("- Harga:", data_laptop[laptop]['harga'])
    
    # Meminta input pengiriman
    pengiriman = input("Pilih pengiriman (dikirim/diambil sendiri): ")
    
    # Meminta input pembayaran
    pembayaran = input("Pilih pembayaran (cash/debit): ")
    
    if pembayaran == "debit":
        jenis_debit = input("Pilih jenis debit (e-wallet/bank): ")
    
    # Menampilkan struk pembelian
    print("===== Struk Pembelian =====")
    print("Laptop yang dibeli:")
    for laptop in laptop_rekomendasi:
        print("- Merk:", data_laptop[laptop]['merk'])
        print("- Prosesor:", data_laptop[laptop]['prosesor'])
        print("- RAM:", data_laptop[laptop]['ram'], "GB")
        print("- ROM:", data_laptop[laptop]['rom'], "GB")
        print("- Harga:", data_laptop[laptop]['harga'])
    print("Metode Pengiriman:", pengiriman)
    print("Metode Pembayaran:", pembayaran)
    if pembayaran == "debit":
        print("Jenis Debit:", jenis_debit)

# Memanggil fungsi rekomendasi_laptop()
rekomendasi_laptop()