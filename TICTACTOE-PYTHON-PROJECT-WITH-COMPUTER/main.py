
# PYTHON PROJECT
# TIC TAC TOE
# BASIC PROJECT TO BUILD MY BASIC PROGRAMMING EFFICIENCY
# THIS PROJECT IS TWO PLAYER GAME ONE PLAYER AS COMPUTER AND OTHER PLAYER AS USER
# THIS PROJECT HAS BEEN BUILD WITH BASIC PROGRAMMING STRUCTURES AND FUNCTIONS







#Importing library
import random


#Declaring brd as Global
brd =[[" "] * 3 for i in range(3)]

#function to set the board with empty values
def brdempty():
    for i in range(3):
        for j in range(3):
            brd[i][j]= " "

#function to check if the board is full or not
def brd_full():
    for i in range (0,3):
        for j in range(0,3):
           if(brd[i][j]== " "):
               return 1



#function assigning values on board for user entry
def assval(x, y):
    brd[x][y] = "X"
    printbrd()
    BF = brd_full()
    if BF == 1:
        IW = ISWINNER()
        if (IW == 0):
            print("\n!!!!YOU ARE THE WINNER!!!!!!\n")
            print("\nyou can play another game:::!!!")
            brdempty()
            chkstart()
        if (IW == 1):
            print("\nOH !!!COMPUTER IS THE WINNER\n ")
            print("\nyou can play another game:::!!!\n")
            brdempty()
            chkstart()
    else:
        IW = ISWINNER()
        if (IW == 0):
            print("\n!!!!YOU ARE THE WINNER!!!!!!\n")
            print("\nyou can play another game:::!!!\n")
            brdempty()
            chkstart()
        elif (IW == 1):
            print("\nOH!!!COMPUTER IS THE WINNER\n\n ")
            print("\nyou can play another game:::!!!\n")
            brdempty()
            chkstart()
        else:
            print("BOARD IS NOW FILLED COMPLETELY")
            print("******MATCH DRAW******")
            chkstart()


#function assigning values on board for Computer entry
def compassval(x, y):
    print("COMPUTER ENTERED ITS POSITION")
    print("--------------------------------")
    brd[x][y] = "Y"
    printbrd()
    BF = brd_full()
    if BF == 1:
        IW = ISWINNER()
        if (IW == 0):
            print("\n!!!!YOU ARE THE WINNER!!!!!!\n")
            print("\nyou can play another game:::!!!")
            brdempty()
            chkstart()
        if (IW == 1):
            print("\nOH !!!COMPUTER IS THE WINNER\n ")
            print("\nyou can play another game:::!!!\n")
            brdempty()
            chkstart()
    else:
        IW = ISWINNER()
        if (IW == 0):
            print("\n!!!!YOU ARE THE WINNER!!!!!!\n")
            print("\nyou can play another game:::!!!\n")
            brdempty()
            chkstart()
        elif (IW == 1):
            print("\nOH!!!COMPUTER IS THE WINNER\n\n ")
            print("\nyou can play another game:::!!!\n")
            brdempty()
            chkstart()
        else:
         print("BOARD IS NOW FILLED COMPLETELY")
         print("******MATCH DRAW******")
         chkstart()

#Function to check winner conditions on board

def ISWINNER():
    for i in range (3):
     if( (brd[i][0]==brd[i][1]==brd[i][2]=="X") or (brd[0][i]==brd[1][i]==brd[2][i]=="X") or(brd[0][2] == brd[1][1] == brd[2][0] == "X")or(brd[0][0]==brd[1][1]==brd[2][2]=="X")):
          return 0
     elif((brd[i][0]==brd[i][1]==brd[i][2]=="Y" ) or (brd[0][i]==brd[1][i]==brd[2][i]=="Y") or (brd[0][0]==brd[1][1]==brd[2][2]=="Y")or (brd[0][2] == brd[1][1] == brd[2][0] == "Y")):
          return 1

#Function to print the Board

def printbrd():
    print("\n""--""--""---")
    print("|" + brd[0][0] + "|" + brd[0][1] + "|" + brd[0][2]+"|" )
    print("|" + brd[1][0] + "|" + brd[1][1] + "|" + brd[1][2]+"|" )
    print("|" + brd[2][0] + "|" + brd[2][1] + "|" + brd[2][2]+"|" )
    print("--""--""---""\n")


#Function getting random position to computer

def getcomppos1():

    a =random.randint(0,2)
    b =random.randint(0,2)
    PO=isposoccup(a,b)
    if PO==1:
        getcomppos1()
    elif PO==0:
        compassval(a,b)
        getusrpos1()


#Getting user position from user
def getusrpos1():
     print("NEXTENTRY : Now your turn")
     print("-------------------------")
     pos1 = input("Enter your position as in row :")
     pos2 = input("Enter your position as in column :")
     if(pos1.isnumeric() and pos2.isnumeric()):
         x= int(pos1)-1
         y = int(pos2)-1
         if ((x <= 2) and (y <= 2) and (x >= 0) and (y >= 0)):

             IO = isposoccup(x, y)
             if (IO == 0):
                 assval(x, y)
                 getcomppos1()
             else:
                 print("\nPosition occupied please enter a valid input\n")
                 getusrpos1()
         else:
             print("\nPlease enter proper values to column between 1 and 3\n")
             getusrpos1()
     else:
      print("\nPlease enter a valid input:")
      getusrpos1()


#function to check if the particular position is filled or empty
def isposoccup(x,y):
    if (brd[x][y]=="X" or brd[x][y]=="Y"):
        return 1
    else:
        return 0


#function to start the game
def chkstart():
     print("\nTIC TAC TOE ")
     print("-------------\n")
     name_1 = input("Do you want to start the game y/n:")
     if name_1.lower() == 'y':
         print("\nHELLO! WELCOME TO THE GAME")
         printbrd()
         firstusrpos1()
     elif name_1.lower() == 'n':
         print("\nThank you!!\nBye............")
         exit()
     else:
         print("\nPlease give proper input")
         chkstart()


#Function to get very first user input
def firstusrpos1():
    print("YOU WILL BE : X  COMPUTER WILL BE :  Y")
    print("---------------------------------------\n")
    pos1 = input("Please enter your position as in row :")
    pos2 = input("Please enter your position as in column :")
    if (pos1.isnumeric() and pos2.isnumeric()):
        x = int(pos1)
        x = x-1
        y = int(pos2)
        y = y-1
        if ((x <= 2) and (y <= 2) and (x >= 0) and (y >= 0)):
            IO = isposoccup(x,y)
            if (IO == 0):
                     assval(x,y)
                     getcomppos1()
            else:
               print("\n The position is occupied\nPlease enter a valid input\n")
               getusrpos1()
        else:
             print("\nPlease enter proper values to column between 1 and 3")
             getusrpos1()
    else:
        print("\nPlease enter a valid input\n")
        getusrpos1()

#main function
def main():
  print("\nWELCOME!!!!")
  chkstart()

if __name__== "__main__":
    main()






