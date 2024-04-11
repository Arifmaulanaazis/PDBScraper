
# PDB Scraper


Aplikasi ini adalah scraper sederhana yang dibuat menggunakan Python untuk mendapatkan data PDB (Protein Data Bank) dari situs web RCSB PDB. Data yang diambil meliputi informasi seperti deskripsi, klasifikasi, organisme, sistem ekspresi, mutasi, tanggal penyetoran dan pelepasan, serta penulis penyetoran.

## Instalasi

1. Pastikan Anda memiliki Python diinstal di sistem Anda.
2. Pastikan Chrome Driver telah diunduh dan ditempatkan di dalam direktori `./driver/`. Jika belum, Anda dapat mengunduhnya [di sini](https://chromedriver.chromium.org/downloads).
3. Instal dependensi Python dengan menjalankan perintah:
   ```
   pip install pandas bs4 selenium requests
   ```

## Penggunaan

1. Jalankan program dengan menjalankan perintah berikut:
   ```
   python PDB Scraper.py
   ```
2. Ikuti petunjuk yang muncul untuk memasukkan kata kunci pencarian.
3. Setelah proses selesai, hasil akan disimpan dalam file Excel di dalam direktori `./hasil/`.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi GPLV3. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## Kontribusi

Anda dipersilakan untuk berkontribusi pada proyek ini. Silakan buat pull request untuk saran perbaikan atau tambahan fitur.

## Kontak

Jika Anda memiliki pertanyaan atau masukan, jangan ragu untuk menghubungi saya melalui surel di [titandigitalsoft@gmail.com](mailto:titandigitalsoft@gmail.com) atau melalui [profil GitHub saya](https://github.com/Arifmaulanaazis).

Terima kasih telah menggunakan PDB Scraper!
