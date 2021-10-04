# Writeup - Magical Mystery Club

Diberikan sebuah binary ELF 64-bit. Dengan Ghidra kita dapat melakukan dekompilasi yang cukup mudah dibaca karena binary tidak di*strip*.

![img0](https://cdn.discordapp.com/attachments/870696024027566150/876108331352227880/unknown.png)

Cara kerja program adalah melakukan *loop* terhadap *array* char yang diinputkan, lalu mengganti setiap elemen char dengan nilai yang dikembalikan oleh fungsi `cast_magic()` dengan parameter char tersebut. Lalu, fungsi `memcmp()` dipanggil untuk membandingkan *char array* tersebut dengan data dengan offset 34 dari awal *memory block flag* dan perbandingan dilakukan untuk 0x62 *byte* pertama, maka dapat diasumsikan bahwa *flag* sepanjang 98 karakter. Sehingga, kita mengetahui bahwa tidak semua *fields* dari struktur data flag perlu diperhatikan, hanya *byte* ke-5 dari *field* ke-7 hingga *byte* ke-6 dari *field* ke-19. Kita tinggal mengonversi dari *little endian* nantinya.

![img1](https://cdn.discordapp.com/attachments/870696024027566150/876110070675554314/unknown.png)

Lalu, kita perlu untuk memeriksa transformasi yang dilakukan terhadap karakter-karakter input. Ternyata, dua fungsi misterius dipanggil dengan argumen yaitu karakter yang sedang ditransformasi dan juga suatu nilai acak dari 0 - 0xff yang dihasilkan oleh pemanggilan fungsi `rand()`. Terdapat juga suatu variabel state yang dikalikan tiga untuk setiap pemanggilan fungsi.

![img2](https://cdn.discordapp.com/attachments/870696024027566150/876111584664125480/unknown.png)

Pemanggilan fungsi tersebut mengembalikan nilai dari pemanggilan fungsi lain, dengan parameter kedua yang telah dimodifikasi.

![img3](https://cdn.discordapp.com/attachments/870696024027566150/876112526134353930/unknown.png)

Hingga pada ujungnya, dilakukan operasi penjumlahan dan modulo 0xff. Sehingga, kita perlu untuk menelusuri dan mencatat tiap operasi yang dilakukan terhadap variabel acak hingga akhirnya menjadi konstan untuk transformasi.

![img4](https://cdn.discordapp.com/attachments/870696024027566150/876112258248372224/unknown.png)

Konstan yang digunakan untuk penjumlahan dihasilkan oleh operasi-operasi aljabar pada fungsi-fungsi sebelumnya. Sebenarnya ini hanyalah salah satu *magic trick* aljabar yang sering dipamerkan saat kita SD yaitu dengan mengeliminasi variabel, sehingga berapapun nilai yang dihasilkan `rand()`, hasil operasi tetap merupakan konstan.

![img5](https://cdn.discordapp.com/attachments/870696024027566150/876113717140537434/unknown.png)

Persamaan konstan untuk operasi pada fungsi transformasi char adalah sebagai berikut.

![img6](https://cdn.discordapp.com/attachments/870696024027566150/876114444944568372/unknown.png)

Sedangkan untuk fungsi transformasi state adalah

![img7](https://cdn.discordapp.com/attachments/870696024027566150/876114938861584404/unknown.png)

Maka, kita dapatkan bahwa fungsi transformasi char `c` adalah `((c + 19) % 256) ^ ((state - 55) % 256)`. Kita tinggal melakukan bruteforce setiap karakter yang sesuai dengan bytes yang terdapat pada struktur data `flag`.

![img8](https://cdn.discordapp.com/attachments/870696024027566150/876115633652252762/unknown.png)

![img9](https://cdn.discordapp.com/attachments/870696024027566150/876115839672283136/unknown.png)

## Flag
```
COMPFEST13{n3Ver_Tru5t_M4tHemAg1cKal_tR1cK5s_n0BoDY_tH0u6hT_No_0ne_W0ulD_n0t1c3_4nYw4Y_98f66ab185}
```