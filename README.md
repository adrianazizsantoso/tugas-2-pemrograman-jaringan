# Tugas 2 Pemrograman Jaringan
oleh: Adrian Aziz Santoso (NRP 5025221229)
kelas: Pemrograman Jaringan C

- Tutorial install Docker pada Terminal Linux: www.youtube.com/watch?v=cVoR9rY31EQ
- Tutorial VPN: its.ac.id/dptsi/wp-content/uploads/sites/8/2024/03/Panduan-Akses-VPN.pdf
- Tutorial menjalankan Jupyter Notebook: www.youtube.com/watch?v=bWwqSXxf3iw

1. Buatlah sebuah program time server dengan ketentuan sebagai berikut 
  a. Membuka port di port 45000 dengan transport TCP 
  b. Server harus dapat melayani request yang concurrent, gunakan contoh multithreading pada ini 
  c. Ketentuan request yang dilayani 
    i. Diawali dengan string “TIME dan diakhiri dengan karakter 13 dan karakter 10” 
    ii. Setiap request dapat diakhiri dengan string “QUIT” yang diakhiri dengan karakter 13 dan 10 
  d. Server akan merespon dengan jam dengan ketentuan 
    i. Dalam bentuk string (UTF-8) 
    ii. Diawali dengan “JAM<spasi><jam>” 
    iii. <jam> berisikan info jam dalam format “hh:mm:ss” dan diakhiri dengan karakter 13 dan karakter 10 
2. Jalankan di lab environment 
  a. Tuliskan dalam satu file PDF dengan nama TUGAS2.PDF 
    i. Link menuju source code anda di github (masing-masing harus punya repository di github: )
    ii. Capturelah hasil eksekusi program server anda

IP Address:  `192.168.15.128/24`
Container ID dapat dicek di Terminal Linux dengan command `nmcli -p device show`
Selengkapnya dapat dilihat di: www.youtube.com/watch?v=XduCxUhUUdQ

<img width="510" alt="image" src="https://github.com/adrianazizsantoso/tugas-2-pemrograman-jaringan/assets/115202624/21f5a2e2-d584-4c97-aae7-5c700ad47335">

<img width="510" alt="image" src="https://github.com/adrianazizsantoso/tugas-2-pemrograman-jaringan/assets/115202624/caa1273f-160a-4f9e-818f-da01e3cacbf1">

<img width="510" alt="image" src="https://github.com/adrianazizsantoso/tugas-2-pemrograman-jaringan/assets/115202624/58d56d58-0343-43b5-b0dd-932d67f52b3d">









