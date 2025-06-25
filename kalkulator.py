import math
# Kalkulator Sederhana
print("===Kalkulator Sederhana===")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
print("5. Eksponen (**)")
print("6. Modulus (%)")
print("7. Logaritma (log)")
print("8. Akar (sqrt)")
print("9. Floor Division (//)")
print("10. Exit")
print("========HAVE_FUN!=========")




# Looping
while True:
    pilihan = input("Pilih operasi (1-10): ")
    if pilihan == "10":
        print("Thanks for using my calculator!")
        break

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

# Proses Data & Output 
    if pilihan == "1":
        hasil = angka1 + angka2
        print("Hasil Penjumlahan: ", hasil)
    elif pilihan == "2":
        hasil = angka1 - angka2
        print("Hasil Pengurangan: ", hasil)
    
    elif pilihan == "3":
        hasil = angka1 * angka2
        print("Hasil Perkalian: ", hasil)
    
    elif pilihan == "4":
        if angka2 != 0: # bilangan yang dibagi 0 hasilnya tak terhingga (infinite)
            hasil = angka1 / angka2
            print("Hasil Pembagian: ", hasil)
        else:
            print("Error! Pembagian tidak dapat dibagi dengan angka 0")
    
    elif pilihan == "5":
        hasil = angka1 ** angka2
        print("Hasil Eksponen: ", hasil)
    
    elif pilihan == "6":
        if angka2 != 0:
            hasil = angka1 % angka2
            print("Hasil Modulus: ", hasil)
        else:
            print("Error! Tidak bisa modulus dengan angka 0")
    
    elif pilihan == "7":
        if angka1 > 0 and angka2 > 0 and angka2 != 1:
            hasil = math.log(angka1, angka2)
            print("Hasil Logaritma: ", hasil)
        else:
            print("Error! Logaritma tidak dapat dihitung jika: ")
            print("- Angka Negatif")
            print("- Basis ≤ 0")
            print("- Basis = 1")
    
    elif pilihan == "8":
        hasil = angka1 ** (1/angka2)
        print(f"Hasil Akar {angka2} dari {angka1} adalah: ", hasil)
    
    elif pilihan == "9":
        hasil = angka1 // angka2
        print("Hasil Floor Division: ", hasil)
   
    else:
        print("Pilihan tidak tersedia")

    print("======================")


