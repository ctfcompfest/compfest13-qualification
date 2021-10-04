#!/usr/bin/env python3
from base64 import a85encode
flag = b'COMPFEST13{4fd29464a28a1b39559f4fc500b41c4b17ec8ad74512394a830b51506AIUEOuh_f8facf99fe}'

dialogues = [
    b'Hey',
        b'Hey?',
    b'Bob..',
        b'What',
    b'Do you like a secret?',
        b'Who doesn\'t like?',
    b'Nice. I have this flag.',
        b'What?',
    flag[:20],
        b'Hmm. Just the first 20 characters?',
    b'I\'m pretty sure you have the rest',
        b'Yeah, flag[20:60]',
    b'I have the flag[60:] too...',
        b'Ok, I will send it after you. Go on.',
    flag[60:],
        flag[20:60],
    b'Nice, we have the flag now!',
        b'I hope hackers cannot see this.',
    b'This channel is secure right?',
        b'Yeah.',
    b'I hope you\'re right.',
        b'I hope so.',
    b'Ok then',
        b'Bye.',
    b'Bye',
        b'bye',
]

assert len(dialogues) % 2 == 0

alice_dialogue = [
    a85encode(dialogues[i]) for i in range(0, len(dialogues), 2) 
]

bob_dialogue = [
    a85encode(dialogues[i]) for i in range(1, len(dialogues), 2)
]