# Writeup Secure Channel
Misal:
```
A: Alice's key
B: Bob's key
p: a prime number
g: a number we can forge
pow(a, b) = a pangkat b
pow(a, b, c) = (a pangkat b) modulo c
```

Kita tahu beberapa fakta berikut:
- Kita bisa mendapatkan `pow(g, A, p)` and `pow(g, B, p)` jika kita connect ke conversation.
- Key untuk decrypt pesan adalah `pow(g, A * B, p)`.

Perhatikan bahwa `pow(g, A * B, p) == pow(pow(g, A, p), B, p)`. Karena key yang dipakai sama, maka kita bisa connect ke Bob dan kirim `g = pow(g, A, p), secret = 1` dan mendapatkan `pow(pow(g, A, p), B, q)` untuk suatu bilangan prima `q` sebagai bagian public key Bob.

Jika kita connect terus ke Bob, maka kita mendapatkan:
```
pow(pow(g, A, p), B, q_1)
pow(pow(g, A, p), B, q_2)
pow(pow(g, A, p), B, q_3)
...
```
Yang mana kita dapat mencari solusi unik dari `pow(g, A, p)` apabila `pow((pow(g, A, p), B) < perkalian seluruh prima q` dengan menggunakan [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem). Karena `B` tidak terlalu besar (hanya antara 1 - 99 inklusif), maka kita bisa mengirim 100 requests ke Bob dan mendapatkan nilai dari `pow(g, A, p)` seperti dijelaskan sebelumnya. Lalu, kita hanya perlu mendekripsi seluruh pesan.

Solusi lainnya adalah dengan menggunakan brute force nilai `B` karena `B` tidak terlalu besar, dan sisanya adalah mendekripsi seluruh pesan. Pesan perlu didekripsi lagi menggunakan base85 (varian original, `base64.a85decode` pada python).