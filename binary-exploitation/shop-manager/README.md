# Shop Manager

by prajnapras19

---

## Flag

```
COMPFEST13{I_us3_st4Ck_p1v0T1ng_How_bouT_Y0u_dd4dfcc265}
```

## Description
A simple shop simulator

## Difficulty
Easy

## Hints
* short on space for chain? why don't use the heap?

## Tags
Heap overflow, ret2libc, rop

## Deployment
- How to compile (no need to recompile for now):
    ```
    gcc -fno-stack-protector -no-pie -o chall chall.c
    ```

- Run:
    ```
    ./chall
    ```

- ubuntu 18.04 (libc-2.27)

- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

## Notes
- Mungkin perlu diberi rate limit, karena bisa saja ada yang bruteforce dengan melakukan sekitar 80 - 160 koneksi
