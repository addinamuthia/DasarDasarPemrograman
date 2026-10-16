# tugas no 1
kendaraan = ["aerox", "motor", 150, "pink", 2]
kendaraan.append(5000)
kendaraan.append("matic")
kendaraan.insert(2,"yamaha")
print(kendaraan)

# tugas no 2
print("=== Alat hitung luas bangun datar ===")
print("Pilih 1 untuk menghitung luas persegi")
print("Pilih 2 untuk menghitung luas lingkaran")
print("Pilih 3 untuk menghitung luas segitiga")

pilihan =int(input("Masukan pilihan (1/2/3):"))

match pilihan: 
    case 1:
        s = int(input("masukan panjang sisi persegi:"))
        luas = s * s
        print(f"Luas persegi adalah: {luas}")
        
    case 2:
        r = int(input("Masukan jari jari lingkaran: "))
        pi = 3.14
        luas = pi * r**2
        print(f"Luas lingkaran adalah: {luas}")
        
    case 3:
        a = int(input("Masukan panjang alas segitiga: "))
        t = int(input("Masukan panjang tinggi segitiga: "))
        luas = a * t / 2
        print(f"Luas segitiga adalah: {luas}")
        
    case _:
        print("Masukan pilihan dengan benar")