from random import shuffle #mods verstehen
with open("C:\Users\heike\Desktop\VS-Repository\Python_uebungen\Superlatives.txt", "r") as infile:
    txt = [line.strip() for line in infile] #das muss ich noch verstehen "with as" befehl und "for in"
shuffle(txt)

for strophe in range(4):
    for n in range(2):   
        for i in range(4):
            print("Spam ",end='')
        print()
    shuffle(txt)    
    el1 = txt.pop()
    el2 = txt.pop()
    print(("{} SPAM, {} SPAM".format(el1, el2)).upper()) #"{}" sind Platzhalter
    print()


 