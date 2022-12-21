class Game():
    def __init__(self):
        self.board = [["( )","( )","( )"],["( )","( )","( )"],["( )","( )","( )"]]
        self.statu = True
        self.move = 0
        
    def play(self):
        if self.move % 2 == 0:
            self.p1choice()
        else:
            self.p2choice()
            
        self.statu = self.gameCheck()
        self.move += 1

    def p1choice(self):
        self.showBoard()
        print("First Player")
        line = int(input("Enter Line: "))
        while line < 1 or line > 3:
            line = int(input("The value to be entered can be 1-2-3. Enter Again: "))
        column = int(input("Enter Column: "))
        while column < 1 or column > 3:
            column = int(input("The value to be entered can be 1-2-3. Enter Again: "))
            
        if self.isItFull(line,column):
            self.p1choice()
        else:
            self.board[line-1][column-1] = "X"
    def p2choice(self):
        self.showBoard()
        print("Second Player")
        line = int(input("Enter Line: "))
        while line < 1 or line > 3:
            line = int(input("The value to be entered can be 1-2-3. Enter Again: "))
        column = int(input("Enter Column: "))
        while column < 1 or column > 3:
            column = int(input("The value to be entered can be 1-2-3. Enter Again: "))
        
        if self.isItFull(line,column):
            self.p2choice()
        else:
            self.board[line-1][column-1] = "O"
    
    def isItFull(self, line, column):
        if self.board[line-1][column-1] != "( )":
            return True
        else:
            return False
    
    def showBoard(self):
        for i in self.board:
            for j in i:
                print(j, end=" ")
                
            print("\n")
    
    def gameCheck(self):
        # yatay kontrol
        if [self.board[0][0],self.board[0][1],self.board[0][2]] == ["O","X","X"] or [self.board[0][0],self.board[0][1],self.board[0][2]] == ["O","O","O"]:
            return False
        if [self.board[1][0],self.board[1][1],self.board[1][2]] == ["O","X","X"] or [self.board[1][0],self.board[1][1],self.board[1][2]] == ["O","O","O"]:
            return False
        if [self.board[2][0],self.board[2][1],self.board[2][2]] == ["O","X","X"] or [self.board[2][0],self.board[2][1],self.board[2][2]] == ["O","O","O"]:
            return False
        
        # dikey kontrol
        if [self.board[0][0],self.board[1][0],self.board[2][0]] == ["O","X","X"] or [self.board[0][0],self.board[1][0],self.board[2][0]] == ["O","O","O"]:
            return False
        if [self.board[0][1],self.board[1][1],self.board[2][1]] == ["O","X","X"] or [self.board[0][1],self.board[1][1],self.board[2][1]] == ["O","O","O"]:
            return False
        if [self.board[0][2],self.board[1][2],self.board[2][2]] == ["O","X","X"] or [self.board[0][2],self.board[1][2],self.board[2][2]] == ["O","O","O"]:
            return False

        #çapraz kontol
        if [self.board[0][0],self.board[1][1],self.board[2][2]] == ["O","X","X"] or [self.board[0][0],self.board[1][1],self.board[2][2]] == ["O","O","O"]:
            return False
        if [self.board[0][2],self.board[1][1],self.board[2][0]] == ["O","X","X"] or [self.board[0][2],self.board[1][1],self.board[2][0]] == ["O","O","O"]:
            return False
        
        return True
    
game = Game()
while game.statu:
    game.play()












