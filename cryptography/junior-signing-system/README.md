# Junior Signing System

by prajnapras19

---

## Flag

```
COMPFEST13{ECdsA_i5_underAtt4cK}
```

## Description
Our last year intern is now a junior programmer. He is still learning about how to make signing systems. Now, he claimed that his implementation of ECDSA signing system is fast and secure. As an experiment, he created a special feature.<br>
`nc <HOST> <PORT>`<br>

Submit the flag with format `COMPFEST13{<flag_you_found>}`.

## Difficulty
medium-hard

## Hints
* I have told him that it is not secure to skip some part of double-and-add algorithm
* There exists a not-so-old paper about this on the internet, I guess it is just about 20 years ago


## Tags
ECDSA, fault attack, lattice attack

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

## Notes
> Intentionally left empty