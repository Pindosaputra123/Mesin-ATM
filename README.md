
# ATM Sederhana

Sebuah aplikasi konsol sederhana untuk simulasi penggunaan ATM, termasuk fitur cek saldo, transfer uang, dan tarik tunai. Aplikasi ini ditulis menggunakan Python dan cocok untuk pembelajaran konsep dasar pemrograman.

## Fitur
1. **Cek Saldo**  
   Menampilkan saldo berdasarkan nomor rekening yang valid.

2. **Transfer Uang**  
   Memungkinkan transfer uang dari satu rekening ke rekening lain yang terdaftar.

3. **Tarik Tunai**  
   Menarik sejumlah uang dari saldo rekening yang valid.

4. **Keamanan PIN**  
   Setiap nomor rekening dilengkapi dengan PIN untuk keamanan transaksi.

## Cara Penggunaan
1. **Clone repository ini:**
   ```bash
   git clone https://github.com/username/repository-name.git
   ```
2. **Masuk ke direktori proyek:**
   ```bash
   cd repository-name
   ```
3. **Jalankan program menggunakan Python:**
   ```bash
   python atm.py
   ```

## Struktur Data
Data pengguna disimpan dalam bentuk dictionary:
```python
data_pengguna = {
    "234567": {"pin": 1432, "saldo": 1000000},
    "998899": {"pin": 4567, "saldo": 500000},
    "237788": {"pin": 5543, "saldo": 450000}
}
```
- **Key**: Nomor rekening.
- **Value**: Dictionary berisi `pin` dan `saldo`.

## Kebutuhan Sistem
- Python 3.x
- Sistem operasi Windows, macOS, atau Linux
- Pustaka `os` (bawaan Python)

## Screenshot
Tampilan utama aplikasi:
```
|=========================================|
|     Selamat Datang Di ATM Sederhana     |
|=========================================|
| 1 | Cek Saldo                           |
| 2 | Transfer Uang                       |
| 3 | Tarik Tunai                         |
| 4 | Keluar                              |
|=========================================|
```

## Catatan
- Pastikan nomor rekening dan PIN benar untuk mengakses fitur.
- Setelah setiap aksi, tekan `Enter` untuk kembali ke menu utama.

## Kontribusi
1. Fork repositori ini.
2. Buat branch baru untuk fitur atau perbaikan Anda.
3. Kirimkan pull request dengan deskripsi jelas.

## Lisensi
Proyek ini menggunakan lisensi [MIT](LICENSE).
