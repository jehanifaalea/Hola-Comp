import pandas as pd

def welcome():
    print("Selamat datang di toko kami!")

def select_laptop():
    df = pd.read_csv('data_laptop.csv')

    prosesor = input("Masukkan tipe prosesor yang diinginkan: ")
    ram = int(input("Masukkan jumlah RAM yang diinginkan (dalam GB): "))
    rom = int(input("Masukkan kapasitas penyimpanan (ROM) yang diinginkan (dalam GB): "))
    harga_range = input("Masukkan rentang harga yang diinginkan (contoh: 5-10 jt): ")
    merk = input("Masukkan merk laptop yang diinginkan: ")

    filtered_df = df[(df['prosesor'] == prosesor) &
                     (df['ram'] == ram) &
                     (df['rom'] == rom) &
                     (df['merk'] == merk) &
                     (df['harga'].between(*map(int, harga_range.split('-'))))]

    if filtered_df.empty:
        print("Mohon maaf, laptop yang sesuai dengan spesifikasi Anda belum tersedia di toko kami.")
    else:
        print("Berikut adalah laptop yang sesuai dengan spesifikasi Anda:")
        print(filtered_df[['merk', 'prosesor', 'ram', 'rom', 'harga']])

def main():
    welcome()
    while True:
        choice = input("Pilih opsi:\n1. Pilih laptop berdasarkan spesifikasi\n2. Keluar\n")

        if choice == "1":
            select_laptop()
        elif choice == "2":
            break
        else:
            print("Opsi tidak valid.")

if _name_ == "_main_":
    main()