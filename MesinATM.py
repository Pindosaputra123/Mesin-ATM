import os

# Sebagai Tempat Untuk Menyimpan Data Use Dari No Rekening Dan Pin
data_pengguna = {
    "234567": {"pin": 1432, "saldo": 1000000},
    "998899": {"pin": 4567, "saldo": 500000},
    "237788": {"pin": 5543, "saldo": 450000}
}

# Fungsi Membersihkan Layar
def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungdi Untuk Mengecek Saldo Berdasarkan Data Pengguna ATM
def cek_saldo(nomor_rekening):
    if nomor_rekening in data_pengguna:
        print("Saldo Anda :", data_pengguna[nomor_rekening]["saldo"])
    else:
        print("Nomor Rekening Tidak Ditemukan.")

# Fungsi Untuk Menarik Uang Berdasarkan Data Pengguna ATM
def tarik_uang(nomor_rekening, jumlah):
    if nomor_rekening in data_pengguna:
        if data_pengguna[nomor_rekening]["saldo"] >= jumlah:
            data_pengguna[nomor_rekening]["saldo"] -= jumlah
            print("Penarikan Berhasil. Saldo Anda Sekarang", data_pengguna[nomor_rekening]["saldo"])
        else:
            print("Saldo Tidak Mencukupi.")
    else:
        print("Nomor Rekening Tidak Ditemukan.")

# Fungsi Untuk Mentransfer Uang Ke No Rekening Pengguna Yang Setuju
def transfer(nomor_rekening_pengirim, nomor_rekening_tujuan, jumlah):
    if nomor_rekening_pengirim in data_pengguna and nomor_rekening_tujuan in data_pengguna:
        if data_pengguna[nomor_rekening_pengirim]["saldo"] >= jumlah:
            data_pengguna[nomor_rekening_pengirim]["saldo"] -= jumlah
            data_pengguna[nomor_rekening_tujuan]["saldo"] += jumlah
            print("Transfer Berhasil.")
        else:
            print("Saldo Tidak Mencukupi.")
    else:
        print("Nomor Rekening Tidak Ditemukan.")
    
# Program Utama
while True:
    bersihkan_layar()
    print("|=========================================|")
    print("|     Selamat Datang Di ATM Sederhana     |")
    print("|=========================================|")
    nomor_rekening = input("Masukkan Nomor Rekening : ")
    pin = int(input("Masukkan PIN            : "))
    if nomor_rekening in data_pengguna and data_pengguna[nomor_rekening]["pin"] == pin:

        while True:
            bersihkan_layar()
            print("\n|=========================================|")
            print("|     Selamat Datang Di ATM Sederhana     |")
            print("|=========================================|")
            print("| 1 | Cek Saldo                           |")
            print("| 2 | Transfer Uang                       |")
            print("| 3 | Tarik Tunai                         |")
            print("| 4 | Keluar                              |")
            print("|=========================================|")
            pilihan = input("Pilih Menu (1/2/3/4) : ")

            if pilihan == "1":
                bersihkan_layar()
                cek_saldo(nomor_rekening)
                input("\nTekan Enter Untuk Melanjutkan.")
            elif pilihan == "2":
                bersihkan_layar()
                nomor_rekening_tujuan = input("Masukkan Nomor Rekening Tujaun : ")
                jumlah = int(input("Masukkan Jumlah Yang Ingin Ditransfer : "))
                transfer(nomor_rekening, nomor_rekening_tujuan, jumlah)
                input("\nTekan Enter Untuk Melanjutkan.")
            elif pilihan == "3":
                bersihkan_layar()
                jumlah = int(input("Masukkan Jumlah Yang Ingin Ditarik : "))
                tarik_uang(nomor_rekening, jumlah)
                input("\nTekan Enter Untuk Melanjutkan.")
            elif pilihan == "4":
                print("Terima Kasih Telah Menggunakan ATM Kami!\n")
                break
            else:
                print("Pilihan Tidak Valid.")
                input("\nTekan Enter Untuk Melanjutkan.")
    else:
        print("Nomor Rekening Atau PIN Salah.\n")
        input("\nTekan Enter Untuk Melanjutkan.")