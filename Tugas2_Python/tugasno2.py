member = 5 
tot = int(input("Masukkan Total Belanja : "))
pil = input(print("Apakah Member ?, Y/N "))
if pil == "Y" : 
       if (tot >= 500000 and tot <= 1000000) : 
        totaldiskon = member + 2
        print("Selamat anda mendapatkan diskon sebanyak : ", totaldiskon)
       if (tot > 1000000): 
        totaldiskon = member + 3 
else : 
    print("Tidak ada")