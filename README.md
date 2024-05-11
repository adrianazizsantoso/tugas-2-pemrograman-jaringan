<div>

# Tugas 2 Pemrograman Jaringan

</div>

- Nama: Adrian Aziz Santoso (NRP 5025221229)
- Kelas: Pemrograman Jaringan C
- Tanggal: Sabtu, 11 Mei 2024

### Link penting:

- Tutorial install Docker pada Terminal Linux: www.youtube.com/watch?v=cVoR9rY31EQ
- Tutorial VPN: its.ac.id/dptsi/wp-content/uploads/sites/8/2024/03/Panduan-Akses-VPN.pdf
- Tutorial menjalankan Jupyter Notebook: www.youtube.com/watch?v=bWwqSXxf3iw

### Instruksi:

1. Buatlah sebuah program time server dengan ketentuan sebagai berikut
   - a. Membuka port di port 45000 dengan transport TCP 
   - b. Server harus dapat melayani request yang concurrent, gunakan contoh multithreading pada [ini](httpsgithub.comrm77progjarblobmasterprogjar3threading_examplesserver_thread.py)
   - c. Ketentuan request yang dilayani
      - i. Diawali dengan string “TIME dan diakhiri dengan karakter 13 dan karakter 10” 
      - ii. Setiap request dapat diakhiri dengan string “QUIT” yang diakhiri dengan karakter 13 dan 10 
   - d. Server akan merespon dengan jam dengan ketentuan 
      - i. Dalam bentuk string (UTF-8) 
      - ii. Diawali dengan “JAM<spasi><jam>” 
      - iii. <jam> berisikan info jam dalam format “hh:mm:ss” dan diakhiri dengan karakter 13 dan karakter 10 
2. Jalankan di lab environment 
   - a. Tuliskan dalam satu file PDF dengan nama TUGAS2.PDF 
      - i. Link menuju source code anda di github (masing-masing harus punya repository di github: https://github.com/adrianazizsantoso/tugas-2-pemrograman-jaringan/blob/main/Tugas2.py) 
      - ii. Capturelah hasil eksekusi program server anda

### Notes:

IP Address: `192.168.15.128/24`
Container ID dapat dicek di Terminal Linux dengan command `nmcli -p device show`
Selengkapnya dapat dilihat di: www.youtube.com/watch?v=XduCxUhUUdQ

### Screenshot:

<img width="510" alt="image" src="https://github.com/adrianazizsantoso/tugas-2-pemrograman-jaringan/assets/115202624/33d8028f-af56-45f6-83ff-c33fd6a25239">

<img width="510" alt="image" src="https://github.com/adrianazizsantoso/tugas-2-pemrograman-jaringan/assets/115202624/5b716e5c-1f5f-48dd-95df-26c569afa4a5">

<img width="510" alt="image" src="https://github.com/adrianazizsantoso/tugas-2-pemrograman-jaringan/assets/115202624/fb5f3d0f-cf21-42f1-bca5-58ca020a9cf5">


