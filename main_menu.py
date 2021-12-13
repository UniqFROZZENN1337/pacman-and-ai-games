import tkinter as tki
import os
from tkinter import *


BLACK = (0, 0, 0)


def StartPacman():
    os.system(r'python StructFiles/game.py')


def StartSnakeAI():
    os.system(r'python StructFiles/SnakeAI/snake.py')


def StartFlappyBirdAI():
    os.system(r'python StructFiles/FlappyBirdAI/main.py')


app = tki.Tk()
app.title("Plasm-Leaf Games")
app.geometry('616x500')
lbl = Label(app, text="Plasm-Leaf Games", font=("Arial Bold", 50),)
pacman = tki.Button(app,text="Start Pacman",command=StartPacman, width=60, height=5,bg='blue', fg='yellow')
snake = tki.Button(app,text="Start SnakeAI",command=StartSnakeAI, width=60, height=5, bg='#6bb8c9', fg='yellow')
flappybird = tki.Button(app,text="Start FlappyBirdAI",command=StartFlappyBirdAI, width=60, height=5, bg='green', fg='yellow')

lbl.pack()
pacman.pack()
snake.pack()
flappybird.pack()

app.mainloop()
