import turtle as tu
import math

lines = 1_000000


with open("1miopi.txt", "r") as f:
    pi = f.read()
    
print(pi[0:10])
print(pi[-10:])
tu.mode("logo")
tu.tracer(False)
tu.screensize(5000,5000,"black")
#tu.pencolor("red")
tu.colormode(255)

for n in range(lines): #schritt der wiederholung =n
    color= int(n/(lines/255))
    b=color
    if color < 20: 
        g = 0
    else:
        g = 255-color 
    if 235 < g < 200:
        r = 0  
    else:
        if color < 240:
            r = 255
        else:
            for x in range(15):
                a = (math.log(x+2)/2.08) 
                r = int(255 * 1/a/4)
    
    tu.pencolor(r, g, b)


    zahl = int(pi[n])
    rot = zahl * 36
    tu.setheading(rot)
    tu.forward(1)
    if n % 100_000 == 0:
        tu.update()


tu.done()


