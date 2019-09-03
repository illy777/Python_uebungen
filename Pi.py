import turtle as tu

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
        if color < 247:
            r = 255
        else:
            r= 255 - color
    
    tu.pencolor(r, g, b)
    zahl = int(pi[n])
    r = zahl * 36
    tu.setheading(r)
    tu.forward(1)
    if n % 10_000 == 0:
        tu.update()


tu.done()


