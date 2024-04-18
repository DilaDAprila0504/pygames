def main():
    print("\n")
    print("Pilih Salah Satu!")
    print("1. Kertas")
    print("2. Batu")
    print("3. Gunting")
    print("4. Keluar/Ga Main")
    print("\n")
    pilih = int(input("Masukkan Pilihan Anda: "))
    
    import random
    comp = random.randint(1,3)
    
    if pilih == 1:
        if comp == 1:
            print("\nKamu Memilih Kertas")
            print("Komputer Memilih Kertas")
            print("Seri!\n")
        elif comp == 2:
            print("\nKamu Memilih Kertas")
            print("Komputer Memilih Batu")
            print("Komputer Menang!\n")
        else:
            print("\nKamu Memilih Kertas")
            print("Komputer Memilih Gunting") 
            print("Kamu Menang!\n")
    
    elif pilih == 2:
        if comp == 1:
            print("\nKamu Memilih Batu")
            print("Komputer Memilih Kertas")
            print("Kamu Menang!\n")
        elif comp == 2:
            print("\nKamu Memilih Batu")
            print("Komputer Memilih Batu")
            print("Seri!\n")
        else:
            print("\nKamu Memilih Batu")
            print("Komputer Memilih Gunting")
            print("Komputer Menang!\n")

    elif pilih == 3:
        if comp == 1:
            print("\nKamu Memilih Gunting")
            print("Komputer Memilih Kertas")
            print("Komputer Menang!\n")
        elif comp == 2:
            print("\nKamu Memilih Gunting")
            print("Komputer Memilih Batu")
            print("Kamu Menang!\n")
        else:
            print("\nKamu Memilih Gunting")
            print("Komputer Memilih Gunting")
            print("Seri!\n")

    elif pilih == 4:
        print("Terimakasih.\n")
        exit()
            
    else:    
        print("\nPilihan Tidak Tersedia\n")

main()