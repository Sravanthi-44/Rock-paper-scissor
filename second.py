
from tkinter import *
root=Tk()
import random
root.title("ROCK PAPAER SCISSER")
root.geometry("460x500")
rps= ["_Rock_.","_Paper_","Scissors"]
def play(event):
    computer=random.choice(rps)
    player=event.widget.cget("text")
    player1=Label(frame4,text=player,relief=SUNKEN,bg="green",borderwidth=5,font=("Arial",20))
    player1.grid(row=0,column=1)
    computer1=Label(frame4,text=computer,relief=SUNKEN,bg="green",borderwidth=5,font=("Arial",20))
    computer1.grid(row=0,column=2)
    if computer==player:
        winner=Label(frame5,text="Its Draw",relief=RAISED,borderwidth=5,font=("Arial",20))
        winner.pack()
    elif computer=="_Rock_."and player=="Scissors":
        winner=Label(frame5,text="Computer Win",relief=RAISED,borderwidth=5,font=("Arial",20))
        winner.pack()
    elif computer=="Scissors"and player=="_Rock_.":
        winner=Label(frame5,text="Player Win",relief=RAISED,borderwidth=5,font=("Arial",20))
        winner.pack()
    elif computer=="_Paper_"and player=="Scissors":
        winner=Label(frame5,text="Player win",relief=RAISED,borderwidth=5,font=("Arial",20))
        winner.pack()
    elif computer=="Scissors"and player=="_Paper_":
        winner=Label(frame5,text="Computer Win",relief=RAISED,borderwidth=5,font=("Arial",20))
        winner.pack()
    elif computer=="_Rock_."and player=="_Paper_":
        winner=Label(frame5,text="Player Win",relief=RAISED,borderwidth=5,font=("Arial",20))
        winner.pack()
    elif computer=="_Paper_"and player=="_Rock_.":
        winner=Label(frame5,text="Computer Win",relief=RAISED,borderwidth=5,font=("Arial",20))
        winner.pack()
frame1=Frame(root ,bg="lightblue")
frame1.pack(fill=X)
titleLabel=Label(frame1,text="ROCK PAPAER SCISSER",font=("Arial",20),bg="Yellow")
titleLabel.pack()
frame2=Frame(root ,bg="lightgreen")
frame2.pack(fill=X)
player1=Label(frame2,text="__Player__",relief=SUNKEN,bg="green",borderwidth=5,font=("Arial",20))
player1.grid(row=0,column=1)
computer1=Label(frame2,text="Computer",relief=SUNKEN,bg="green",borderwidth=5,font=("Arial",20))
computer1.grid(row=0,column=2)
frame4=Frame(root ,bg="lightgreen")
frame4.pack(fill=X)
player1=Label(frame4,text="_________",relief=SUNKEN,bg="green",borderwidth=5,font=("Arial",20))
player1.grid(row=0,column=1)
computer=Label(frame4,text="________",relief=SUNKEN,bg="green",borderwidth=5,font=("Arial",20))
computer.grid(row=0,column=2)
frame3=Frame(root ,bg="lightblue")
frame3.pack(fill=X)
rock=Button(frame3,text="_Rock_.",relief=RAISED,bg="orange",borderwidth=5,font=("Arial",20))
rock.pack()
rock.bind("<Button-1>",play)
rock=Button(frame3,text="_Paper_",relief=RAISED,bg="orange",borderwidth=5,font=("Arial",20))
rock.pack()
rock.bind("<Button-1>",play)
rock=Button(frame3,text="Scissor",relief=RAISED,bg="orange",borderwidth=5,font=("Arial",20))
rock.pack()
rock.bind("<Button-1>",play)
frame5=Frame(root ,bg="lightgreen")
frame5.pack(fill=X)
winner=Label(frame5,text="__Winner__",relief=RAISED,borderwidth=5,font=("Arial",20))
winner.pack()
root.mainloop()
