import tkinter as tk

def tombol12():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=390,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=390,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Tampilkan spesifikasi laptop berdasarkan rentang harga?", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=390,y=203)

    button_ya = tk.Button(root, text="Yaa",bg="grey", fg="white", command=lambda:{root.destroy(),tombol11()})
    button_ya.place(x=510,y=310, width=100, height=30)
    button_tidak = tk.Button(root, text="Tidakk",bg="grey", fg="white", command=lambda:{root.destroy(),tombol11()})
    button_tidak.place(x=510,y=370, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

def tombol11():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=370,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=370,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Pilih kapasitas ROM", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=460,y=203)

    button_Rom1 = tk.Button(root, text="256",bg="grey", fg="white", command=lambda:{root.destroy(),tombol12()})
    button_Rom1.place(x=480,y=280, width=100, height=30)
    button_Rom2 = tk.Button(root, text="512",bg="grey", fg="white", command=lambda:{root.destroy(),tombol12()})
    button_Rom2.place(x=480,y=330, width=100, height=30)
    button_Rom3 = tk.Button(root, text="1024",bg="grey", fg="white", command=lambda:{root.destroy(),tombol12()})
    button_Rom3.place(x=480,y=380, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

def tombol10():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=390,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=390,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Tampilkan spesifikasi laptop berdasarkan Rom? ", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=390,y=203)

    button_ya = tk.Button(root, text="Yaa",bg="grey", fg="white", command=lambda:{root.destroy(),tombol11()})
    button_ya.place(x=510,y=310, width=100, height=30)
    button_tidak = tk.Button(root, text="Tidakk",bg="grey", fg="white", command=lambda:{root.destroy(),tombol12()})
    button_tidak.place(x=510,y=370, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()



def tombol9():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=370,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=370,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Pilih kapasitas RAM", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=460,y=203)

    button_Ram1 = tk.Button(root, text="4",bg="grey", fg="white", command=lambda:{root.destroy(),tombol10()})
    button_Ram1.place(x=480,y=280, width=100, height=30)
    button_Ram2 = tk.Button(root, text="8",bg="grey", fg="white", command=lambda:{root.destroy(),tombol10()})
    button_Ram2.place(x=480,y=330, width=100, height=30)
    button_Ram3 = tk.Button(root, text="12",bg="grey", fg="white", command=lambda:{root.destroy(),tombol10()})
    button_Ram3.place(x=480,y=380, width=100, height=30)
    button_Ram4 = tk.Button(root, text="16",bg="grey", fg="white", command=lambda:{root.destroy(),tombol10()})
    button_Ram4.place(x=480,y=430, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

def tombol8():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=390,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=390,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Tampilkan spesifikasi laptop berdasarkan ram? ", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=390,y=203)

    button_ya = tk.Button(root, text="Yaa",bg="grey", fg="white", command=lambda:{root.destroy(),tombol9()})
    button_ya.place(x=510,y=310, width=100, height=30)
    button_tidak = tk.Button(root, text="Tidakk",bg="grey", fg="white", command=lambda:{root.destroy(),tombol10()})
    button_tidak.place(x=510,y=370, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

def tombol7():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=390,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=390,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Pilih jenis prosesor!", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=390,y=203)

    button_ryzen1= tk.Button(root, text="AMD Ryzen 5600H",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_ryzen1.place(x=510,y=240, width=100, height=30)
    button_ryzen2= tk.Button(root, text="AMD Ryzen 5",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_ryzen2.place(x=510,y=290, width=100, height=30)
    button_ryzen3= tk.Button(root, text="AMD Ryzen 7",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_ryzen3.place(x=510,y=340, width=100, height=30)

def tombol6():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=390,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=390,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Pilih jenis prosesor!", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=390,y=203)

    button_intel1 = tk.Button(root, text="Intel i3",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_intel1.place(x=510,y=240, width=100, height=30)
    button_intel2 = tk.Button(root, text="Intel i5",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_intel2.place(x=510,y=290, width=100, height=30)
    button_intel3 = tk.Button(root, text="Intel Core i3",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_intel3.place(x=510,y=340, width=100, height=30)
    button_intel4 = tk.Button(root, text="Intel Core i5",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_intel4.place(x=510,y=390, width=100, height=30)
    button_intel5 = tk.Button(root, text="Intel Core i7",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_intel5.place(x=510,y=440, width=100, height=30)
    button_intel6 = tk.Button(root, text="Intel Core i9",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_intel6.place(x=510,y=490, width=100, height=30)
    button_intel7 = tk.Button(root, text="Intel UHD Graphics 600",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_intel7.place(x=510,y=540, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

def tombol5():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=390,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=390,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Pilih jenis prosesor!", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=390,y=203)

    button_intel = tk.Button(root, text="Intel",bg="grey", fg="white", command=lambda:{root.destroy(),tombol6()})
    button_intel.place(x=510,y=310, width=100, height=30)
    button_ryzen = tk.Button(root, text="Ryzen",bg="grey", fg="white", command=lambda:{root.destroy(),tombol7()})
    button_ryzen.place(x=510,y=370, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

def tombol4():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=330, height=30, bg= 'grey')
    kotak1.place(x=390,y=200)
    kotak2 = tk.Frame(root,width=330, height=300, bg= 'white')
    kotak2.place(x=390,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja (user)!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Tampilkan spesifikasi laptop berdasarkan prosessor?", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=390,y=203)

    button_ya = tk.Button(root, text="Yaa",bg="grey", fg="white", command=lambda:{root.destroy(),tombol5()})
    button_ya.place(x=510,y=310, width=100, height=30)
    button_tidak = tk.Button(root, text="Tidakk",bg="grey", fg="white", command=lambda:{root.destroy(),tombol8()})
    button_tidak.place(x=510,y=370, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

def tombol3():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=300, height=30, bg= 'grey')
    kotak1.place(x=400,y=200)
    kotak2 = tk.Frame(root,width=300, height=300, bg= 'white')
    kotak2.place(x=400,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.pack()
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.pack()
    label3 = tk.Label(root, text="Selamat Berbelanja! (user)", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.pack()
    label4 = tk.Label(root, text="Anda ingin membeli laptop atas rekomendasi kami atau ngisi manual?", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=420,y=203)

    button_filtering = tk.Button(root, text="Filtering",bg="grey", fg="white", command=lambda:{root.destroy(),tombol4()})
    button_filtering.place(x=510,y=310, width=100, height=30)
    button_manual = tk.Button(root, text="Manual",bg="grey", fg="white", command=lambda:{root.destroy(),tombol()})
    button_manual.place(x=511,y=370, width=100, height=30)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

def tombol2():

    root = tk.Tk()
    root.title("Toko Hola-Comp")
    root.geometry("1080x720")
    root.resizable(False,False)
    root.configure(background="purple")

    kotak1 =tk.Frame(root,width=300, height=30, bg= 'grey')
    kotak1.place(x=400,y=200)
    kotak2 = tk.Frame(root,width=300, height=300, bg= 'white')
    kotak2.place(x=400,y=230)

    label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
    label1.place(x=70,y=50)
    label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label2.place(x=390,y=110)
    label3 = tk.Label(root, text="Selamat Berbelanja!", font=("Times New Roman", 16),bg="purple", fg= "white")
    label3.place(x=465,y=150)
    label4 = tk.Label(root, text="Buatlah Username dan Password anda", font=("Times New Roman", 12),bg="grey", fg= "white")
    label4.place(x=420,y=203)

    # Tambahkan komponen login
    label_username = tk.Label(root, text="Username")
    label_username.place(x=515,y=260)
    entry_username = tk.Entry(root)
    entry_username.place(x=480,y=290)

    label_password = tk.Label(root, text="Password")
    label_password.place(x=515,y=320)
    entry_password = tk.Entry(root, show="*")
    entry_password.place(x=480,y=350)

    button_signup = tk.Button(root, text="Sign Up", command=lambda:{root.destroy(),tombol3()})
    button_signup.place(x=520,y=380)


    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

root = tk.Tk()
root.title("Toko Hola-Comp")
root.geometry("1080x720")
root.resizable(False,False)
root.configure(background="purple")

kotak1 =tk.Frame(root,width=300, height=30, bg= 'grey')
kotak1.place(x=400,y=200)
kotak2 = tk.Frame(root,width=300, height=300, bg= 'white')
kotak2.place(x=400,y=230)

label1 = tk.Label(root, text="================WELCOME================", font=("Times New Roman", 30),bg="purple", fg= "white")
label1.place(x=70,y=50)
label2 = tk.Label(root, text="Selamat datang di Toko Hola-Comp!", font=("Times New Roman", 16),bg="purple", fg= "white")
label2.place(x=390,y=110)
label3 = tk.Label(root, text="Selamat Berbelanja!", font=("Times New Roman", 16),bg="purple", fg= "white")
label3.place(x=465,y=150)
label4 = tk.Label(root, text="Masukkan Username dan Password anda", font=("Times New Roman", 12),bg="grey", fg= "white")
label4.place(x=420,y=203)

# Tambahkan komponen login
label_username = tk.Label(root, text="Username")
label_username.place(x=515,y=260)
entry_username = tk.Entry(root)
entry_username.place(x=480,y=290)

label_password = tk.Label(root, text="Password")
label_password.place(x=515,y=320)
entry_password = tk.Entry(root, show="*")
entry_password.place(x=480,y=350)

button_login = tk.Button(root, text="Login", command=lambda:{root.destroy(),tombol3()})
button_login.place(x=520,y=380)

label5 = tk.Label(root, text="Jika belum punya akun, silahkan Sign Up!", font=("Times New Roman", 12),bg="white", fg= "black")
label5.place(x=420,y=440)

button_signup = tk.Button(root, text="Sign Up", command=lambda:{root.destroy(),tombol2()})
button_signup.place(x=515,y=470)



root.mainloop()