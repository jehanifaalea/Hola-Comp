import pandas as pd

def welcome():
    print("Selamat datang di toko kami!")

def select_laptop():
    df = pd.read_csv('C:/Users/USER/Documents/project team prokom/Hola-Comp/data laptop.csv')

    # Memilih laptop berdasarkan spesifikasi
    prosesor = input("Pilih prosesor (Intel/AMD Ryzen): ")
    ram = input("Pilih RAM (4/8/10/12/16 GB): ")
    rom = input("Pilih ROM (256/512/1024 GB): ")

    filtered_df = df[(df['prosesor'] == prosesor) & (df['ram'] == int(ram)) & (df['rom'] == int(rom))]

    if filtered_df.empty:
        print("Tidak ada laptop yang sesuai dengan spesifikasi yang dipilih. Silakan coba lagi.")
        return

    print("Berikut adalah laptop yang sesuai dengan spesifikasi:")
    print(filtered_df[['Nama', 'Harga']])

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

if __name__ == "__main__":
    main()