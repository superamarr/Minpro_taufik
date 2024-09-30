# menampung NIM dan password sementara
NIM = 2409116001
pw = 12345678

# login sederhana
while True:
    try:
        Login_us = int(input("NIM      : ")) 
        Login_pw = int(input("Password : "))

        if Login_us == NIM and Login_pw == pw:
            print("\nLogin Berhasil! \n\n Hi, Taufik Ramadhani")
            break  # keluar dari loop jika NIM dan password benar
        else:
            print("Masukkan NIM dan password yang benar!")
    except ValueError:
        print("Masukkan NIM dan password dengan angka yang benar!")

# menghitung gaji dan perulangan
while True:
    try: 
        jam_kerja = float(input("\nSilahkan masukkan jam kerja: ")) 
        tarif_per_jam = float(input("Silahkan masukkan tarif gaji per jam: "))  
        
        gaji_total = jam_kerja * tarif_per_jam  
        bonus = 0  

        # membuat percabangan jika jam kerja lebih dari 160
        if jam_kerja > 160:
            bonus = 0.1 * gaji_total  # menghitung bonus 10%
            gaji_total += bonus  # menambahkan bonus ke gaji total
            print("Jam kerja lebih dari 160 jam, Anda akan mendapatkan bonus 10%.")
        else:
            print("Jam kerja tidak lebih dari 160 jam, Anda tidak mendapatkan bonus.")

        print("=========================")
        print("Total bonus : Rp", bonus) 
        print("Total gaji  : Rp", gaji_total)  
        print("=========================")

    except ValueError:
        print("Masukkan jam kerja dan tarif gaji dengan benar!") 
        continue  # kembali ke awal loop untuk meminta input lagi

    # membuat perulangan dan percabangan jika ingin menghitung gaji lagi
    lanjut = input("Apakah Anda ingin menghitung gaji lagi? (y/n): ")
    if lanjut.lower() != 'y': # lower di gunakan untuk meminimalisir capslock user
        print("======== SELESAI ========")  # menampilkan pesan selesai
        break  # keluar dari loop
