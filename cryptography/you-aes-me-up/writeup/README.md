# Writeup You AES Me Up

Misal:
```
F(x) = block cipher encryption dari x
G(x) = block cipher decryption dari x
G(F(x)) = x
```
`IV` tidak diketahui, sementara `m1` (didapat dari dekripsi blok pertama flag), `c1`, `c2`, ..., `cn` diketahui.<br>

Blok kedua dari flag adalah `c2 = F(m1 ^ c1  ^ m2)`. Jika `c2` didekripsi, maka didapat:
```
G(c2) ^ IV = m1 ^ c1 ^ m2 ^ IV	...(1)
```

Karena kita sudah tahu `m1` dan `c1`, dengan melakukan xor `(1)` dengan `m1` dan `c1`, maka didapatkan:
```
G(c2) ^ IV ^ m1 ^ c1 = m2 ^ IV	...(2)
```

Jika `(2)` di-enkripsi, maka didapatkan:
```
F(m2 ^ IV ^ IV) = F(m2)	...(3)
```

Jika `(3)` di-xor dengan `m1`, lalu enkripsi (mekanismenya adalah enkripsi dua blok: `m2 ^ IV` dan `m1`), maka didapatkan:
```
F(F(m2) ^ m1)	...(4)
```

Jika `(4)` didekripsi, maka didapatkan:
```
G(F(F(m2) ^ m1)) ^ IV = F(m2) ^ m1 ^ IV	...(5)
```
Karena `F(m2)` sudah didapatkan di `(3)`, maka kita mendapat `m1 ^ IV`.<br>
Karena `m1` diketahui, `IV` didapatkan dengan melakukan xor, dan kita bisa melakukan dekripsi dari sisa flag dengan decrypt oracle.