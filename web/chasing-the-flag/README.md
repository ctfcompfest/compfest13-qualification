# Chasing The Flag!

by William (Hori75)

---

## Flag

```
COMPFEST13{get-fifty-percent-off-in-CTF-Course-using-this-code_c765355330}
```

## Description
Hi! This contest might be over, but if you could generate the coupon. You might could get discount from a hidden course in this web! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
<link to web>

## Difficulty
medium

## Hints
* Search something that you need to know
* Filters

## Tags
Sql Injection

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

## Notes
- ~~The database should be safe from being dropped because it can't run multiple queries, but, who knows.~~
- The web app should be accessing MySQL via readonly user.

