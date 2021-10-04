# Moneypoly

by prajnapras19

---

## Flag

```
COMPFEST13{R3memb3r1nG_y0ur__Ch1lDh00D_eh_95f63e868a}
```

## Description
Your favorite board game from your childhood :D.

## Difficulty
medium

## Hints
- Many people don't want to go to the jail, but this jail is special.
- The last house before the start line is the most expensive, if you can buy it, why don't give it a long name to be remembered?

## Tags
format string, rop, shellcode

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

## Notes
- How to compile:
    ```
    gcc -o chall -static chall.c
    ```
- Tolong beri rate limit, solusi yang optimal kadang butuh sedikit keberuntungan pada bagian random, jadi perlu terhubung beberapa kali sampai dapat.