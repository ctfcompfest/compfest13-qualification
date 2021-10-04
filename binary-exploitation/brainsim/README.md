# BrainSim

by xMaximusKl

---

## Flag

```
COMPFEST13{570PPPP_I7___937_0U7_0f_my_H34d___b6fc1236d6}
```

## Description
Heyy! So, I found this BF simulator thing. I thought it's hackable-ish? Because my friend told me there's flag file in it. Maybe you could help me while I'm having my breakfast ? Ehehe...

## Difficulty
easy

## Hints
* Simple BOF using brainfuck, I wonder what you could with that ? Maybe *hanging* around in a forbidden place ? :)

## Tags
Brainfuck, Buffer Overflow, Shellcode

## Deployment
Use latest docker & docker-compose:
```
docker-compose up --build --detach
```

## Notes
Compile with:
```
gcc BrainSim.c -o BrainSim -fno-stack-protector -Wl,-z,execstack -g 
```