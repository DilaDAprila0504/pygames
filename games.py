def main():
    print("\n")
    print("Pilih Salah Satu!")
    print("1. Kertas")
    print("2. Batu")
    print("3. Gunting")
    print("\n")
    pilih = int(input("Masukkan Pilihan Anda: "))
    
    import random
    comp = random.randint(1,3)
    
    if pilih == 1:
        if comp == 1:
            print("\nKamu Memilih Kertas")
            print("Komputer Memilih Kertas")
            print("Seri!")
        elif comp == 2:
            print("\nKamu Memilih Kertas")
            print("Komputer Memilih Batu")
            print("Komputer Menang!")
        else:
            print("\nKamu Memilih Kertas")
            print("Komputer Memilih Gunting") 
            print("Kamu Menang!")
    
    elif pilih == 2:
        if comp == 1:
            print("\nKamu Memilih Batu")
            print("Komputer Memilih Kertas")
            print("Kamu Menang!")
        elif comp == 2:
            print("\nKamu Memilih Batu")
            print("Komputer Memilih Batu")
            print("Seri!")
        else:
            print("\nKamu Memilih Batu")
            print("Komputer Memilih Gunting")
            print("Komputer Menang!")

    elif pilih == 3:
        if comp == 1:
            print("\nKamu Memilih Gunting")
            print("Komputer Memilih Kertas")
            print("Komputer Menang!")
        elif comp == 2:
            print("\nKamu Memilih Gunting")
            print("Komputer Memilih Batu")
            print("Kamu Menang!")
        else:
            print("\nKamu Memilih Gunting")
            print("Komputer Memilih Gunting")
            print("Seri!")
            
    else:    
        print("\nPilihan Tidak Tersedia")

main()