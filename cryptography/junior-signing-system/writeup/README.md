# Writeup Junior Signing System
Soal ini terinsipirasi dari paper "A Fault Attack on ECDSA" dari Jörn-Marc Schmidt, Marcel Medwed (dapat ditemukan di [sini](https://ieeexplore.ieee.org/abstract/document/5412852)) dan "Lattice Attacks on Digital Signature Schemes" dari N.A. Howgrave-Graham, N.P. Smart (dapat ditemukan di [sini](https://www.researchgate.net/publication/225240686_Lattice_Attacks_on_Digital_Signature_Schemes)). Inti dari soal ini adalah memanfaatkan fault yang terjadi saat proses double-and-add algorithm sesuai pada paper tersebut dan menggunakannya dalam lattice attack.<br>

Referensi mengenai elliptic curve:
- https://andrea.corbellini.name/2015/05/23/elliptic-curve-cryptography-finite-fields-and-discrete-logarithms/
- https://en.m.wikipedia.org/wiki/Elliptic_curve
- https://en.m.wikipedia.org/wiki/Arithmetic_of_abelian_varieties
- https://en.m.wikipedia.org/wiki/Elliptic_curve_point_multiplication