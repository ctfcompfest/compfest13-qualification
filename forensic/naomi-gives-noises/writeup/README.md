# Writeup Naomi Gives Noises

Aplikasi yang digunakan: Audacity, steghide

Kita diberikan dua file, pass.wav dan Flag.jpg
Setelah membuka pass.wav, cukup jelas bahwa itu adalah beberapa audio kode morse dalam frekuensi berbeda-beda yang digabung di dalam satu file. Dengan melihat plot spectrum, terlihat terdapat 6 frekuensi dominan pada audio tersebut. Berdasarkan frekuensi pada plot spectrum tersebut, atau secara langsung dengan trial-and-error, kita dapat mengekstrak kode morse pada frekuensi tertentu dengan `High-Pass Filter`, `Low-Pass Filter`, dan `Noise Reduction`.

Sebagai contoh, salah satu frekuensi dominan adalah sekitar 1378 Hz. Kita perlu mengfilter suara di atas dan di bawah frekuensi tersebut, sehingga kita perlu menggunakan High-Pass Filter pada frekuensi 1300 Hz untuk menghapus frekuensi di bawah 1300 Hz dan perlu menggunakan Low-Pass Filter pada frekuensi 1450 Hz untuk menghapus frekuensi di atas 1450Hz. Jika masih ada sisa noise kode morse lain, kita perlu menggunakan Noise Reduction dengan memberi sampel kode morse noise tersebut.

Berikut frekuensi dan pesan masing-masing kode morse.
```
Frekuensi    -  Transcript
(approx)   
~420         -  2Never8 gonna gi0ve you 5up
~2805        -  Never1 gon3na le7t you dow8n
~1378        -  2Never gonn3a run aroun6d and desert8 you
~2368        -  N7ever gonna8 make you 0cry
~780         -  N1ever 8gonna 7say good9bye
~1879        -  Never4 gonna tell a 2lie and hurt 0you
```
Angka-angka pada transcript juga sebenarnya menunjuk ke frekuensi pesan lainnya.

Setelah itu, soal (dan bantuan hint) mengimplikasi bahwa flag tersebut berada di dalam file Flag.jpg, sehingga kita perlu mengekstrak file flag tersebut. Dengan bantuan `Steghide`, kita dapat mengekstrak file tersebut, namun kita membutuhkan password. Password tersebut bisa ditemukan dengan menyocokkan lirik transcript dengan Flag.jpg. Password untuk ekstrak flag tersebut adalah `naomiyuu5808`

*Writeup ini menggunakan audacity. Peserta mungkin saja dapat mengfilter audio menggunakan python script atau aplikasi lain.
