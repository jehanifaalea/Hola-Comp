#Fungsi untuk menampilkan struk pembelian
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

# Fungsi untuk memilih metode pembayaran
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

# Fungsi untuk memilih metode pengiriman
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

# Menjalankan program utama
if __name__ == '__main__':
    main()