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

while True:
    print("============ Toko Laptop ==============")
    print("1. Tampilkan Shopping Cart")
    print("2. Tambahkan Produk ke Shopping Cart")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == '1':
        tampilkan_keranjang(keranjang)
    elif pilihan == '2':
        nama = input("Masukkan nama produk: ")
        tipe = input("Masukkan tipe produk: ")
        harga = float(input("Masukkan harga produk: "))
        tambahkan_ke_keranjang(keranjang, nama, tipe, harga)
    elif pilihan == '3':
        print("Terima kasih telah berbelanja!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
