import csv

def welcome():
    print("Selamat datang di toko kami!")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Logika untuk verifikasi username dan password
    with open('akun.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login berhasil!")
                return

    print("Username atau password salah.")

def signup():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    # Logika untuk mendaftarkan pengguna baru
    with open('akun.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    
    print("Pendaftaran berhasil!")

def main():
    welcome()
    choice = input("Pilih opsi:\n1. Login\n2. Sign up\n")

    if choice == "1":
        login()
    elif choice == "2":
        signup()
    else:
        print("Opsi tidak valid.")

if __name__ == "__main__":
    main()

