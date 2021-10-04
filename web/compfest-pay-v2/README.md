# COMPFEST Pay v2

by Bonceng

## Flag

```
COMPFEST13{everyONE_n33d5_m0n3y_money_MoNeY_c289b51c8d}
```

## Description
We come back with new features and security. To make up for our mistake last year, we were given free credits for all accounts.

[http://link-to-web/](#)

## Difficulty
medium

## Hints
Rich person always transfer their money to the fictive account to avoid taxes. Maybe you can steal it?

## Tags
XSS, Logic Error, Mass Injection

## Deployment
#### Bot
- Change website link using `HOST` environment variables
- Change credentials if needed
- Run using `src/bot/Dockerfile` or docker-compose

#### Server
- Change flag and the price in `src/server/compfestpay2/secret.py`
- Install module requirements using `pip install -r src/server/requirements.txt` 
- Migrate data run:
    ```
    python3 manage.py migrate
    python3 manage.py loaddata seed
    ```
- Run the program using `python3 manage.py runserver`

## Notes
- https://javascript.info/modules-dynamic-imports