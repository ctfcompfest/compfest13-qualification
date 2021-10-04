# Writeup Chocolate With Nuts

# tl;dr
- Dari process chrome.exe, dapet link google drive. Dapet link `https://drive.google.com/file/d/1BbVHDz1TlIYrUzAaiAODqTZ3YExNjCsm/view?usp=sharing` (Arahan dari deskripsi soal)
- Dari clipboard, dapet .encfs6.xml, yang merupakan key untuk decrypt EncFS (Dibantu hint1)
- Dari environment variables, dapet password EncFS, yaitu `Maple Beetle Saturn` (Dibantu hint2)
- Decrypt dengan EncFS pakai password, flag didapat dari bagian akhir nama setiap gambar yang didecode dengan base64

# Writeup
1. Peserta diberi memory image. Dengan menggunakan volatility, pertama kita perlu menentukan profile. Hal ini dilakukan dengan command `vol.py -f Win7_100820211048.raw imageinfo`. Pada writeup ini kita menggunakan profile Win7SP1x64.

2. Setelah itu kita harus melihat process apa saja yang running di memory image bersama dengan process id nya. Hal ini dilakukan dengan command `vol.py -f Win7_100820211048.raw --profile Win7SP10x64 pstree`. Terlihat process yang non system process, yaitu chrome dan notepad.

3. Berdasarkan soal, hal pertama yang harus dicari dari memory image ini adalah link http. Oleh karena itu, kita dump memory process chrome dengan command `vol.py -f Win7_100820211048.raw --profile Win7SP0x64 memdump --dump-dir="." -p 2240`

4. Kita filter file dengan command `strings 2240.dmp |grep https://`. Kita dapat link google drive `https://drive.google.com/file/d/1BbVHDz1TlIYrUzAaiAODqTZ3YExNjCsm/view?usp=sharing`.

5. Setelah buka file di google drive, terdapat zip file yang berisi file yang terenkripsi. Untuk melanjutkan, kita perlu mencari info lain dari memory image.

6. Jika kita menganalisa clipboard (ditekankan dengan hint soal juga), dengan command, `vol.py -f Win7_100820211048.raw --profile Win7SP0x64 clipboard -v`, kita dapat sekumpulan text. Dari baris `<creator>EncFS "1.9.5"</creator>` kita tahu bahwa ini adalah key untuk enkripsi file dengan EncFS. Kita perlu buat file `.encfs6.xml` dengan mengcopy bytes dari cliboard (jangan strings) dan juga menghapus 2 bit  di belakang setiap karakter (3c 00 3f 00 --> 3c3f).

7.  Masukkan file `.encfs6.xml` tersebut ke dalam folder Chocolate. Kita decrypt folder tersebut menggunakan EncFS MP (untuk windows) atau EncFS untuk linux dengan meng-mount folder Chocolate, namun kita membutuhkan password. Password didapat dari environment variables dengan command, `vol.py -f Win7_100820211048.raw --profile Win7SP0x64 envars`, dan dari System Variable "Passwords" kita dapat, `Chocolate ENCFS: Maple Beetle Saturn; add more password here`

8. Masukkan password, lalu decrypt folder Chocolate tersebut dengan EncFS. Setelah itu, kita dapat sekumpulan gambar Spongebob. Flag kita dapatkan dengan mengdecode bagian akhir nama setiap gambar dengan base64.
