import pandas as pd
import datetime

def hitung_total_harga(laptop_id, aksesoris_id, biaya_pengiriman):
    df_laptop = pd.read_csv('D:\Hola Comp\Hola-Comp\data_laptop.csv')
    df_aksesoris = pd.read_csv('D:\Hola Comp\Hola-Comp\data_aksesoris.csv')

    # Mengambil harga laptop berdasarkan laptop_id
    laptop_row = df_laptop[df_laptop['id'] == laptop_id]
    harga_laptop = laptop_row['harga'].values[0]

    # Mengambil harga aksesoris berdasarkan aksesoris_id
    aksesoris_row = df_aksesoris[df_aksesoris['id'] == aksesoris_id]
    harga_aksesoris = aksesoris_row['harga'].values[0]

    # Menghitung total harga
    total_harga = harga_laptop + harga_aksesoris + biaya_pengiriman
    return total_harga

def generate_struk(nama_pelanggan, laptop_row, aksesoris_row, biaya_pengiriman, metode_pembayaran):
    struk = "===== Struk Pembelian =====\n"
    struk += "Tanggal/Waktu: {}\n".format(datetime.datetime.now())
    struk += "Nama Pelanggan: {}\n".format(nama_pelanggan)
    struk += "Merk Laptop: {}\n".format(laptop_row['merk'].values[0])
    struk += "Harga Laptop: {}\n".format(laptop_row['harga'].values[0])
    if not aksesoris_row.empty:
        struk += "Aksesoris: {}\n".format(aksesoris_row['nama'].values[0])
        struk += "Harga Aksesoris: {}\n".format(aksesoris_row['harga'].values[0])
    struk += "Spesifikasi Laptop:\n"
    struk += " - Prosesor: {}\n".format(laptop_row['prosesor'].values[0])
    struk += " - RAM: {}\n".format(laptop_row['ram'].values[0])
    struk += " - ROM: {}\n".format(laptop_row['rom'].values[0])
    if biaya_pengiriman > 0:
        struk += "Biaya Pengiriman: {}\n".format(biaya_pengiriman)
    struk += "Metode Pembayaran: {}\n".format(metode_pembayaran)

    return struk

def main():
    df_laptop = pd.read_csv('D:\Hola Comp\Hola-Comp\data_laptop.csv')
    df_aksesoris = pd.read_csv('D:\Hola Comp\Hola-Comp\data_aksesoris.csv')

    print("Selamat datang di toko kami!")
    nama_pelanggan = input("Masukkan nama Anda: ")

    print("Berikut adalah pilihan laptop yang tersedia:")
    print(df_laptop[['id', 'merk', 'prosesor', 'ram', 'rom', 'harga']])

    laptop_id = input("Masukkan ID laptop yang ingin Anda beli: ")
    aksesoris_id = input("Masukkan ID aksesoris yang ingin Anda beli (kosongkan jika tidak ada): ")

    # Memilih metode pengiriman
    metode_pengiriman = input("Pilih metode pengiriman:\n1. Kirim ke Alamat\n2. Diambil di Toko\n")
    if metode_pengiriman == "1":
        alamat = input("Masukkan alamat pengiriman: ")
        jarak = float(input("Masukkan jarak (km) dari toko ke alamat Anda: "))
        biaya_pengiriman = jarak * 5000
    else:
        biaya_pengiriman = 0

    total_harga = hitung_total_harga(laptop_id, aksesoris_id, biaya_pengiriman)

    # Memilih metode pembayaran
    metode_pembayaran = input("Pilih metode pembayaran:\n1. Cash\n2. Bank atau e-wallet\n")

    if metode_pembayaran == "1":
        # Cash
        struk = generate_struk(nama_pelanggan, df_laptop[df_laptop['id'] == laptop_id],
                               df_aksesoris[df_aksesoris['id'] == aksesoris_id],
                               biaya_pengiriman, "Cash")
        print(struk)
        print("Pembelian berhasil!")
    elif metode_pembayaran == "2":
        # Bank atau e-wallet
        rekening = "1234567890"  # Contoh nomor rekening toko
        qr_code = "https://example.com/qrcode"  # Contoh QR code

        print("Transfer ke rekening {} dengan total harga {}".format(rekening, total_harga))
        pembayaran_berhasil = input("Apakah pembayaran berhasil? (Y/N): ")

        if pembayaran_berhasil.upper() == "Y":
            struk = generate_struk(nama_pelanggan, df_laptop[df_laptop['id'] == laptop_id],
                                   df_aksesoris[df_aksesoris['id'] == aksesoris_id],
                                   biaya_pengiriman, "Bank atau e-wallet")
            print(struk)
            print("Selamat pembayaran telah berhasil!")
            print("QR Code: {}".format(qr_code))
        else:
            print("Pembayaran belum berhasil. Silakan coba lagi.")
    else:
        print("Metode pembayaran tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

