from time import sleep
import os
from datetime import datetime


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print()


def translate(text):
    text = str(text)
    letters = []
    lines = ['', '', '', '', '', '', '', '', '']
    for letter in text:
        letters.append(LETTERS[letter])
    for i in range(9):
        for letter in letters:
            lines[i] = lines[i] + "  " + letter.splitlines()[i]

    for i in range(9):
        print(lines[i])


LETTERS = {
    "1": u"""\
     ⬛⬛    
     ⬛⬛    
⬛⬛⬛⬛    
     ⬛⬛    
     ⬛⬛    
     ⬛⬛    
     ⬛⬛    
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
""",
    "2": u"""\
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
        ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛        
⬛⬛        
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
""",
    "3": u"""\
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
       ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
       ⬛⬛
       ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
""",
    "4": u"""\
⬛⬛     ⬛⬛
⬛⬛     ⬛⬛
⬛⬛     ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
        ⬛⬛
        ⬛⬛
        ⬛⬛
        ⬛⬛
""",
    "5": u"""\
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛        
⬛⬛        
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
        ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
""",
    "6": u"""\
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛         
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛    ⬛⬛
⬛⬛    ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
""",
    "7": u"""\
⬛⬛⬛⬛
⬛⬛⬛⬛
    ⬛⬛
    ⬛⬛
    ⬛⬛
    ⬛⬛
    ⬛⬛
    ⬛⬛
    ⬛⬛
""",
    "8": u"""\
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛   ⬛⬛
⬛⬛   ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛   ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
""",
    "9": u"""\
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛     ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
        ⬛⬛
        ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
""",
    "0": u"""\
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛     ⬛⬛
⬛⬛     ⬛⬛
⬛⬛     ⬛⬛
⬛⬛     ⬛⬛
⬛⬛     ⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
""",
    ":": u"""\
             
    ⬛⬛     
    ⬛⬛     
             
             
    ⬛⬛     
    ⬛⬛     
             
             
""", }


def clock():
    while 1:
        try:
            ctime = datetime.now()
            clear()
            translate(":".join(
                [(str(i) if len(str(i)) == 2 else "0" + str(i)) for i in [ctime.hour, ctime.minute, ctime.second]]))
            sleep(0.5)
        except KeyboardInterrupt:
            clear()
            break
clock()