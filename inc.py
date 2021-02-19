#groupe BI TD4, groupe 2
#Elsa Fernandez-Antolin




#import des modules

import tkinter as tk


#constantes

HAUTEUR = 400
LARGEUR = 600
COTE = 35
#fonctions
def quadrillage():
    """Dessine un quadrillage dans le canevas avec des carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill="black")
        y += COTE
    i = 0
    while i * COTE <= LARGEUR:
        x = i * COTE
        canvas.create_line((x, 0), (x, HAUTEUR), fill="black")
        i += 1

#programe principal

racine = tk.Tk()
racine.title("INCENDIE")

#création widget
canvas = tk.Canvas(racine, width =LARGEUR , height= HAUTEUR)

#placement widget
canvas.grid(row = 0)

quadrillage()

racine.mainloop()
