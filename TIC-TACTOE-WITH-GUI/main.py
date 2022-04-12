import tkinter as tk
import random
from tkinter import messagebox
import time

counter=1
brd=[''for i in range (9)]


def chkwinner(wind2, counter):
    if ((brd[1] == brd[2] == brd[0] == "X") or (brd[3] == brd[4] == brd[5] == "X") or (
            brd[6] == brd[7] == brd[8] == "X")):


        messagebox.showinfo(title='CONGRATULATIONS', message='X is winner', parent=wind2)

        disable_event(wind2)


        quiting(wind2)
        return 1

    elif ((brd[1] == brd[2] == brd[0] == "O") or (brd[3] == brd[4] == brd[5] == "O") or (
            brd[6] == brd[7] == brd[8] == "O")):
       # return 1

        messagebox.showinfo(title='CONGRATULATIONS', message='O is winner', parent=wind2)
        disable_event(wind2)
        quiting(wind2)
        return 1
    elif ((brd[0] == brd[3] == brd[6] == "X") or (brd[1] == brd[4] == brd[7] == "X") or (
            brd[2] == brd[5] == brd[8] == "X")):
       # return 1

        messagebox.showinfo(title='CONGRATULATIONS', message='X is winner', parent=wind2)
        disable_event(wind2)
        quiting(wind2)
        return 1
    elif ((brd[0] == brd[3] == brd[6] == "O") or (brd[1] == brd[4] == brd[7] == "O") or (
            brd[2] == brd[5] == brd[8] == "O")):
       #return 1

       messagebox.showinfo(title='CONGRATULATIONS', message='O is winner', parent=wind2)
       disable_event(wind2)
       quiting(wind2)
       return 1

    elif ((brd[0] == brd[4] == brd[8] == "X") or (brd[2] == brd[4] == brd[6] == "X")):
       #return 1
       messagebox.showinfo(title='CONGRATULATIONS', message='X is winner', parent=wind2)
       disable_event(wind2)
       quiting(wind2)
       return 1

    elif ((brd[0] == brd[4] == brd[8] == "O") or (brd[2] == brd[4] == brd[6] == "O")):

       messagebox.showinfo(title='CONGRATULATIONS', message='O is winner', parent=wind2)
       disable_event(wind2)
       quiting(wind2)
       return 1
    elif (counter == 9):

       messagebox.showinfo(title='MATCH DRAW', message='match draw', parent=wind2)
       disable_event(wind2)
       quiting(wind2)
       return 1


def disable_event(wind2):
   time.sleep(1)

def openwindow():
        global counter
        counter = 1
        wind2 = tk.Toplevel(wind1)
        wind1.state(newstate='iconic')
        wind2.state(newstate='normal')
        wind2.state(newstate='zoomed')
        wind2.configure(bg='#FFCCFF')
        wind1.state(newstate='iconic')
        wind2.overrideredirect(True)
        drawpanel(wind2)

def drawpanel(wind2):
    global counter
    lbl1 = tk.Label(wind2,text="PLAYER1 :  X       PLAYER2 :  O",bd='5', relief='raised',font='200', bg='#FFFF99',fg='black', height=5, width=45)
    lbl1.place(x=480,y=80)
    exit2 = tk.Button(wind2, bg='#FF0000', text="EXIT THIS GAME", font='18', command=lambda: quiting(wind2))
    exit2.place(x=620,y=550)
    btn0 = tk.Button(wind2, text=brd[0], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(0,wind2))
    btn0.place(x=400,y=200)
    btn1 = tk.Button(wind2, text=brd[1], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(1,wind2))
    btn1.place(x=590, y=200)
    btn2 = tk.Button(wind2, text=brd[2], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(2,wind2))
    btn2.place(x=780, y=200)
    btn3 = tk.Button(wind2, text=brd[3], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(3,wind2))
    btn3.place(x=400, y=300)
    btn4 = tk.Button(wind2, text=brd[4], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(4,wind2))
    btn4.place(x=590, y=300)
    btn5 = tk.Button(wind2, text=brd[5], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(5,wind2))
    btn5.place(x=780, y=300)
    btn6 = tk.Button(wind2, text=brd[6], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(6,wind2))
    btn6.place(x=400, y=400)
    btn7 = tk.Button(wind2, text=brd[7], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(7,wind2))
    btn7.place(x=590, y=400)
    btn8 = tk.Button(wind2, text=brd[8], font='18', bg='black', fg='white', height=5, width=20,command=lambda: assignval(8,wind2))
    btn8.place(x=780, y=400)


def quiting(wind2):
    global counter
    global brd
    counter = 1

    brd = ['' for i in range(9)]
    wind2.destroy()
    wind1.state(newstate='zoomed')

def computerassval(wind2):
     global counter
     if(counter<9):
      x=random.randint(0,8)

      if ((brd[x] != "X") and (brd[x] != "O")):

        brd[x] = "O"
        drawpanel(wind2)

        cw=chkwinner(wind2, counter)
        counter = counter + 1

      else:

        computerassval(wind2)

def assignval(i,wind2):
    global counter
    global brd
    if (counter==1):
            brd[i] = "X"

            drawpanel(wind2)

            computerassval(wind2)
            counter = counter + 1

    elif( counter % 2 == 0 and counter<=9):

        computerassval(wind2)
    else:
      if ((brd[i]!="X")and(brd[i] != "O")):

        brd[i]="X"
        drawpanel(wind2)

        cw=chkwinner(wind2, counter)
        counter = counter + 1
        if(cw!=1):

         computerassval(wind2)

      else:
         messagebox.showerror("position occupied select other position","messageoccupied",parent=wind2)



wind1=tk.Tk()
wind1.title("TIC TAC TOE")
wind1.geometry('500x500')
wind1.state(newstate='zoomed')
wind1.configure(bg='#00BFFF')
label1 = tk.Label(wind1, text="START THE GAME ", font=('arial', '38'), borderwidth='4', relief='solid')
label1.place(relx=0.5, rely=0.3, anchor='center', )
yesbtn = tk.Button(wind1, text="YES", font='18', bg='#006400', fg='white', height=5, width=15, command=openwindow)
yesbtn.place(x=520, y=300)
nobtn = tk.Button(wind1, text="NO", font='18', bg='red', fg='white', height=5, width=15, command=wind1.destroy)
nobtn.place(x=720, y=300)
wind1.mainloop()
