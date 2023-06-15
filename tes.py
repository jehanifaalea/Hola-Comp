
def welcome_message():
   
    print("===================== WELCOME =====================")
    print("        Selamat datang di Toko Hola-Comp!")
    print("===================================================")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    with open('akun.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login berhasil!")
                return True

    print("Username atau password salah.")
    return False

def sign_up():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    # Validasi panjang password
    if len(password) < 8:
        print("Panjang password harus minimal 8 karakter.")
        return False

    # Validasi minimal 1 angka dan 1 huruf kapital
    if not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
        print("Password harus mengandung minimal 1 angka dan 1 huruf kapital.")
        return False

    with open('akun.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                print("Username sudah terdaftar.")
                return False

    with open('akun.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("Akun berhasil dibuat!")
    return True

# Kode lainnya ...

welcome_message()

choice = input("Menu: \n1. Login \n2. Sign Up \n3. Exit \nPilih menu (1/2/3): ")
clear_screen()

if choice == '1':
    if login():
        clear_screen()
        main_menu()
elif choice == '2':
    if sign_up():
        clear_screen()
        main_menu()
elif choice == '3':
    clear_screen()
    print("Terima kasih telah menggunakan program kami!")
else:
    print("Pilihan tidak valid!")
