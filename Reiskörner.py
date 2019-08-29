import matplotlib.pyplot as plt
summe = 0
Plotreiskorn = []
Plotgesamt =[]
PlotGewicht = []

for feld in range(64):
    reiskorn = 2 ** feld
    Plotreiskorn.append(reiskorn)
    summe += reiskorn
    Plotgesamt.append(summe)
    print(f"Feld {feld+1} : {reiskorn:>30,} Reiskörner und damit insgesamt {summe:>26,}\
    Reiskörner")
    gewicht = summe * 0.00002
    PlotGewicht.append(gewicht)
    print(f"Gewicht der Gesamtmenge = {gewicht:>20,.0f} kg ")
    print()
    
plt.plot(Plotreiskorn)
plt.plot(Plotgesamt)
plt.plot(PlotGewicht)

plt.show()




