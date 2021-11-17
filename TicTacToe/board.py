
class Square:
    def __init__(self):
        self.filled = False  # returns value of square is empty
        self.xo = " "      # returns value stored in square (X or O)


class Board:
    def __init__(self,n):
        self.win = False   #check to see if someone won
        self.current = 'X'  #current players turn
        self.n = n  # size of board
        self.limit = self.n*self.n #total number of spaces
        self.spaces = [] # spaces in board
        for i in range(n*n): #contructs board
            newspace = Square()
            self.spaces.append(newspace)


    def isFull(self):
        full = False
        for i in self.spaces:
            if i.filled == False:
                full = False
                break
            else:
                full = True
        return full


    def display(self):
        board =""
        for i in range(self.limit):
            board+= " " +self.spaces[i].xo + " "
            if (i+1)%(self.n) != 0:
                board +=  "|"
            elif (i+1)%(self.n) == 0 and (i+1)%(self.limit) != 0:
                board += "\n" +(self.limit +(self.n-1))*"-" + "\n"
        print(board)

    def fillSquare(self, thisSquare):
        currentSquare = self.spaces[thisSquare - 1]
        currentSquare.filled = True
        currentSquare.xo = self.current




    def play(self):
        self.display()
        while self.win == False and self.isFull() == False:
            print("it is " + self.current + "'s turn")
            validInput = False
            goodInput = -1
            while validInput == False:
                thisSquare = input("Which square do u want to fill \n")
                if (thisSquare.isdigit()):
                    goodInput = int(thisSquare)
                    if (self.spaces[goodInput - 1].filled == False):
                        validInput = True
                    else:
                        print('that square is already filled, please choose another')
                else:
                    print('input is not valid, input an integer')
            self.fillSquare(goodInput)
            self.display()
            self.checkwin()
            if self.current == 'X':
                self.current = 'O'
            else:
                self.current = "X"




    def checkwin(self):
        for i in range(0, self.n):
             checkvertical = [] #checks vertical wins
             for j in range(i, self.limit, self.n):
                checkvertical.append(self.spaces[j].xo)
             if (checkvertical.count(self.current) == self.n):
                self.win = True
                print(self.current + " has won the game")
                return
        for i in range(0, self.limit, self.n): #checks horizontal wins
             checkhorizontal = []
             for j in range(i, i+self.n):
                 checkhorizontal.append(self.spaces[j].xo)
             if (checkhorizontal.count(self.current) == self.n):
                 self.win = True
                 print(self.current + " has won the game")
                 return
        z = 0
        checkdiagonal1 = [] #checks first diagonal
        for y in range(0, self.limit, self.n):
            checkdiagonal1.append(self.spaces[z+y].xo)
            z += 1
        if (checkdiagonal1.count(self.current) == self.n):
            self.win = True
            print(self.current + " has won the game")
            return
        w = self.n-1
        checkdiagonal2 = [] #checks second diagonal
        for x in range(0, self.limit, self.n):
            checkdiagonal2.append(self.spaces[w+x].xo)
            w -= 1
        if (checkdiagonal2.count(self.current) == self.n):
            self.win = True
            print(self.current + " has won the game")
            return
        if(self.win == False and self.isFull() == True):
            print("the game is tied,the board will restart ")
            b1 = Board(3)
            b1.play()












b1 = Board(3)
b1.play()




