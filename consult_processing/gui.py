from tkinter import *
import pandas as pd
from general_query import GeneralQuery
import os
import json

root = Tk()
root.geometry("500x800") #You want the size of the app to be 500x500
root.resizable(0, 0) #Don't allow resizing in the x or y direction

def getGames():
    frame.config({'borderwidth':2})

    query = GeneralQuery(eGame.get().lower(), eDesc.get().lower(), eOS.get().lower(), eRam.get().lower(), eStorage.get().lower(), ePrice.get().lower())
    result = query.processQuery()

    #Display games informations
    for game in result:
        gamePath = os.path.abspath('../inverted_index/db/' + str(game[0]))

        jsonGame = None    
        with open(gamePath, 'r', encoding="unicode_escape") as fp:
            jsonGame = json.loads(fp.read()[0:-1])
        
        r = StringVar()
        r.set(str("\nName: " + jsonGame["game"] + "\nPrice: " + jsonGame["price"] + "\nos: " + jsonGame["os"] + "\nram: " + jsonGame["ram"] + "\nstorage: " + jsonGame["storage"]))
        lResult = Label(frame, font=("Helvetica", 9),textvariable=r)
        lResult.pack()

lHead = Label(root, font=("Helvetica", 24), text="Engenho de Busca - Jogos\n")
lHead.pack()

lGame = Label(root, text="\nNome do Jogo")
lGame.pack()
eGame = Entry(root)
eGame.pack()
eGame.focus_set()

lDesc = Label(root, text="\nDescription")
lDesc.pack()
eDesc = Entry(root)
eDesc.pack()
eDesc.focus_set()

lOS = Label(root, text="\nOperational System")
lOS.pack()
eOS = Entry(root)
eOS.pack()
eOS.focus_set()

lRam = Label(root, text="\nRAM")
lRam.pack()
eRam = Entry(root)
eRam.pack()
eRam.focus_set()

lStorage = Label(root, text="\nStorage")
lStorage.pack()
eStorage = Entry(root)
eStorage.pack()
eStorage.focus_set()

lPrice = Label(root, text="\nPrice")
lPrice.pack()
ePrice = Entry(root)
ePrice.pack()
ePrice.focus_set()

bGeral = Button(root, text="Pesquisar", command=getGames)
bGeral.pack()

lspace = Label(root, text="\nResultados:")
lspace.pack()

frame = Frame(width=300, height=100, borderwidth=0, relief=GROOVE)
frame.pack()

mainloop()