# Writeup <alogus>

# tl;dr
- Dari process python. Dapet script keylogger. Perlu grep hasil memdump pid pythonw, kalo dumpfiles akan menghasilkan file kosong.(Dibantu hint kedua dan ketiga)
- Dari clipboard, dapet link `https://drive.google.com/file/d/1V1bEBWNN_BpioPxNuMi53oBzAtJ2xACE/view?usp=sharing`. Dapet zip file. (Dibantu hint pertama)
- Filter pcap dengan IP dan Port yang terdapat di script keylogger. Ambil key dan hasil log nya. Reverse script keylogger tersebut (xor key dengan hasil log). Dapet password zip file.
- Extract zip dengan password. Readjust color, brightness, atau hue/saturation. Dapet flag. (Arahan dari soal)

# Writeup
1. Peserta diberi memory image `ORION-PC_150820211534.raw`. Dengan menggunakan volatility, pertama kita perlu menentukan profile yang dilakukan dengan menjalankan command `vol.py -f ORION-PC_150820211534.raw imageinfo`. Pada writeup ini kita menggunakan profile Win7SP1x64.

2. Setelah itu, kita harus melihat process apa saja yang sedang berjalan di memory image beserta process id nya. Hal ini dilakukan dengan menjalankan command `vol.py -f ORION-PC_150820211534.raw --profile Win7SP1x64 pstree`. Terlihat banyak process yang (mungkin) memiliki clue, namun process yang paling suspicious adalah pythonw.exe. Berdasarkan hint kedua, dapat diasumsikan bahwa Pak Santoso menanam script keylogging ke setiap device karyawannya.

3. Untuk mengetahui script keylogger nya, kita perlu `dumpfiles` dari volatility. Akan tetapi, command tersebut menghasilkan empty file. Oleh karena itu, kita perlu melakukan dengan cara lain, yaitu strings dan grep, yang ditekankan dengan hint ketiga soal. Untuk mempercepat proses grep, kita pisahkan (dump) proses python tersebut dari memory image dengan menjalankan command `vol.py -f ORION-PC_150820211534.raw --profile Win7SP1x64 memdump --dump-dir="." -p 1104`. 1104 adalah pid pythonw.exe.

4. Kita filter file 1104.dmp tersebut dengan command `strings 1104.dmp |grep "import -C 15"` yang ditekankan juga dengan hint ketiga. Kita juga dapat meng-grep dengan kata kunci yang menurut kita sudah dipastikan ada pada script keylogger tersebut, misal `grep "if __name__ == \"__main__\"" -C 15`, atau `grep pynput -C 15`, dan sebagainya. (Berapa baris yang diinginkan muncul setelah/sebelum kemunculan hasil grep dapat disesuaikan)

5. Setelah itu, kita dapat script keylogger milik Pak Santoso. Terlihat bahwa tepat sebelum client mengirim hasil log, client mengirim panjang hasil log tersebut, lalu server mengirim key sepanjang hasil log tersebut. Hasil log di-XOR-kan dengan key, lalu dikirim ke address tujuan, yaitu `169.254.236.147 dengan port 31678`

6. Dengan informasi tersebut, kita perlu menganalisa file packet capture `ORION-PC_150820211534.pcap` menggunakan Wireshark dengan memberi filter `ip.addr==169.254.236.147 && port==31678`. Kita dapat 9 key dan 9 encrypted message.

7. Setelah itu, kita perlu meng-XOR-kan masing-masing encrypted message dengan masing-masing key. (Lebih jelas pada `solver.py`). Lalu kita dapat hasil keylog Dillan (tertulis pada `Hasil log.txt`) dan password zip, yaitu `h0rs3sHoe t4bl3top eutr0ph1cAtIoN`. 

8. Dengan bantuan hint pertama, kita tahu bahwa Dillan meng-copy link yang dibagikan oleh Pak Susanto, sehingga link tersebut tersimpan pada clipboard memory image. Untuk mendapatkannya, kita perlu menjalankan command `vol.py -f ORION-PC_150820211534.raw --profile Win7SP1x64 clipboard -v`. Kita dapat sebuah link google drive, `https://drive.google.com/file/d/1V1bEBWNN_BpioPxNuMi53oBzAtJ2xACE/view?usp=sharing`. Kita dapat `Dillan_Duck.zip`

9. Extract `Dillan_Duck.zip` dengan menggunakan password yang ditemukan pada poin ketujuh. Kita dapat `a.png`.

10. Berdasarkan deskripsi soal, kita dapat asumsikan bahwa flag didapatkan dengan mengatur color, hue\saturation, dan/atau brightness gambar. Dengan menggunakan Photoshop, flag dapat ditemukan dengan cara menaikkan saturation +100, dan menurunkan lightness secukupnya. Terlihat tulisan `sU5tos0_S4nt0so_5b2e135` pada bagian kaca helm karakter among us pada gambar tersebut.
