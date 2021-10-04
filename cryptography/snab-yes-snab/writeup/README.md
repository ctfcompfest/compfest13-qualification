# Writeup Snab? Yes, Snab
Kita diberikan variabel
```
s = pow(p + q, 2)
n = p*q
a = pow(s + mr, 3, r)
b = (s - q*(2*p + q))*r
e = 0x10001
c_list yang berisi list of ciphertexts
```

Untuk decrypt ciphertext, kita butuh d sementara d butuh totient. Totient function bisa didapat dari n dan s, dengan cara, 
```
tot  = (p - 1)(q - 1)
     = pq - p - q + 1
     = n - (sqrt(s) - 1)
```
Setelah kita dapat totient tentunya kita mendapatkan mr. Di sana kita lihat bahwa `a ≡ (s^3) mod r`, sehingga dapat kita simpulkan bahwa `r| a - s^3`. Oleh karena itu, `GCD(mr, a - (s^3)) = r`, atau m (jika a - (s^3) = m).

Kita bagi masing-masing ciphertexts dengan r untuk mendapatkan pesan sebenarnya. Pesan sebenarnya merupakan lanjutan kodingan cara membuat flag. Kita tinggal balik saja proses pembuatan flagnya, namun kita butuh either p atau q. Variabel p sendiri bisa kita dapat dari b dengan cara, 
```
b = (s - q*(2*p + q))*r
  = (p^2)*r
p = sqrt(b/r)  
```
Setelah dapat p, dapatkan q dari n/p. Selanjutnya kita hanya perlu membalikkan potongan kode proses pembuatan flag dari pesan yang didecrypt sebelumnya.
