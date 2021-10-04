# Secure Channel

by prajnapras19

---

## Flag

```
COMPFEST13{4fd29464a28a1b39559f4fc500b41c4b17ec8ad74512394a830b51506AIUEOuh_f8facf99fe}
```

## Description
You are able to watch the encrypted chat of Alice and Bob. They are talking about the flag right now. Can you get the flag from them?<br>
P.S.: Alice and Bob once have said that they will communicate with some trivial encoding, so people will not notice their message at first glance. Although, people will know it if they search it on the internet! Sure, all of it is printable characters.<br>
Watch the conversation: `nc <HOST> <PORT>`<br>
Talk with Alice: `nc <HOST> <PORT>`<br>
Talk with Bob: `nc <HOST> <PORT>`<br>

## Difficulty
Easy-medium

## Hints
* My trusted source said Bob's key is too low. And they use the same key everytime.

## Tags
Cryptography, CRT, modular maths, Diffie-Hellman key exchange

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

## Notes
* There are 3 services: to watch the conversation, to talk to Alice, to talk to Bob.
* Expected connections to services ~100.
