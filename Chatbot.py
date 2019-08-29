from random import shuffle #mods verstehen
with open("D:\isaac\Programmierung\Python Übungen\Superlatives.txt") as infile:
    txt = [line.strip() for line in infile] #das muss ich noch verstehen "with as" befehl und "for in"
shuffle(txt)
el2 = txt.pop()
el1 = txt.pop()
for strophe in range(4):
    for n in range(2):   
        for i in range(4):
            print("Spam ",end='')
        print()
    shuffle(txt)    
    print(("{} SPAM, {} SPAM".format(el1, el2)).upper()) #"{}" sind Platzhalter
    print()
 