summe = 0
for feld in range(64):
    reiskorn = 2 ** feld
    summe = summe + reiskorn
    gewicht = summe * 0.00002
    print("feld {} : {:>30,} Reiskörner und damit insgesamt {:>26,}\
    Reiskörner".format(feld+1, reiskorn, summe))
    
    print("Gewicht der Gesamtmenge = {:>20,.0f} kg".format(gewicht))
    print()
    




