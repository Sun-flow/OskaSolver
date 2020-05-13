from copy import deepcopy

class Error(Exception):
    pass

class InvalidRowLength(Error):
    pass

class InvalidInput(Error):
    pass

class InvalidPiece(Error):
    pass

class TooManyPiece(Error):
    pass


class OskaBoard:

    def __init__(self, inList, playerTurn):
   
        self.totalRows = len(inList)
        self.maxRowLength = len(inList[0])
        pastCenter = 1
        self.playerTurn = playerTurn
        self.board = []

        try: 
            if self.totalRows == 2 * self.maxRowLength - 3:

                rowNum = 0
                for row in inList:
                    if rowNum <= (self.totalRows - 1) / 2:
                        if len(inList[rowNum]) == self.maxRowLength - rowNum:
                            self.board += [row]
                        else:
                            raise InvalidRowLength('First Half', rowNum, inList[rowNum])
                    else:
                        if len(inList[rowNum]) == 2 + pastCenter:
                            pastCenter += 1
                            self.board += [row]
                        else:
                            raise InvalidRowLength('Second Half', rowNum, inList[rowNum])

                    rowNum += 1

            else:
                raise InvalidInput(inList)
        
            self.findPieces()
        
        except InvalidRowLength as inst:
            print('Invalid row length: ', inst.args)
        except InvalidInput as inst:
            print('Invalid input: ', inst.args)

    

    def findPieces(self):
        try:
            self.wPieces = []
            self.bPieces = []
            wCount = 0
            bCount = 0
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    char = self.board[row][col]
                    if char == 'W' or char == 'w':
                        self.wPieces += [(row, col)]
                        wCount += 1
                    elif char == 'B' or char == 'b':
                        self.bPieces += [(row, col)]
                        bCount += 1
                    elif char != '-':
                        raise InvalidPiece(char, (row, col))

            if wCount > self.maxRowLength:
                raise TooManyPiece('W', self.wPieces)
            elif bCount > self.maxRowLength:
                raise TooManyPiece('B', self.bPieces)

        except InvalidPiece as inst:
            print('Invalid Piece: ', inst.args)
        except TooManyPiece as inst:
            print('Too many', inst.args[0], 'pieces')
                
    

    def printBoard(self):
        for i in range(len(self.board)):
            print('Row #', i, ': ', self.board[i])

        print('Player turn: ', self.playerTurn)


    def replacechar(self, row, col, char):
        newStr = ''

        for i in range(len(self.board[row])):
            if i == col:
                newStr += char
            else:
                newStr += self.board[row][i]

        self.board[row] = newStr


    def generatechildren(self, turn):
        newBoards = []
        
        if turn == 'w':
            for piece in self.wPieces:
                index = self.wPieces.index(piece)
                newBoards += self.move(piece, index, turn)

        else:
            for piece in self.bPieces:
                index = self.bPieces.index(piece)
                newBoards += self.move(piece, index, turn)

            
        if newBoards != []:
            return newBoards
        else:
            return None

    def move(self, piece, index, turn):
        newBoards = []
        currRow = piece[0]
        currCol = piece[1]
        
        leftCol = None
        rightCol = None
        leftJump = 0
        rightJump = 1

        playerPieces = turn
        oppPieces = None
        if turn == 'w':
            oppPieces = 'b'
        else:
            oppPieces = 'w'
        

        nextRow = None
        jumpRow = None
        if turn == 'w':
            nextRow = currRow + 1
            jumpRow = nextRow + 1
            if currRow <= (self.totalRows - 1) / 2:
                leftCol = currCol - 1
                rightCol = currCol
                if jumpRow < (self.totalRows + 1) / 2:
                    leftJump = -1
                    rightJump = 0
            else:
                leftCol = currCol
                rightCol = currCol + 1

        else:
            nextRow = currRow - 1
            jumpRow = nextRow - 1

            if currRow >= (self.totalRows + 1) / 2:
                leftCol = currCol - 1
                rightCol = currCol
                if jumpRow > (self.totalRows - 1) / 2:
                    leftJump = -1
                    rightJump = 0
            else:
                leftCol = currCol
                rightCol = currCol + 1

        
            

        if leftCol >= 0:
            if self.board[nextRow][leftCol] == '-':

                board = deepcopy(self)
                
                if turn == 'w':
                    board.wPieces[index] = (nextRow, leftCol)
                else:
                    board.bPieces[index] = (nextRow, leftCol)
                
                board.replacechar(currRow, currCol, '-')
                board.replacechar(nextRow, leftCol, turn)
                
                newBoards += [board]

            elif self.board[nextRow][leftCol] == oppPieces:
                jumpCol = leftCol + leftJump
                
                if jumpRow < self.totalRows and self.board[jumpRow][jumpCol] == '-':
                    board = deepcopy(self)

                    if turn == 'w':
                        board.bPieces.remove((nextRow, leftCol))
                        board.wPieces[index] = (jumpRow, jumpCol)
                    else:
                        board.wPieces.remove((nextRow, leftCol))
                        board.bPieces[index] = (jumpRow, jumpCol)
                    
                    board.replacechar(nextRow, leftCol, '-')
                    board.replacechar(currRow, currCol, '-')
                    board.replacechar(jumpRow, jumpCol, turn)

                    newBoards += [board]
            

        if rightCol < len(self.board[nextRow]) and currRow < self.totalRows and currRow >= 0 and nextRow >= 0 and nextRow < self.totalRows:
            if nextRow < self.totalRows and self.board[nextRow][rightCol] == '-':
                board = deepcopy(self)

                if turn == 'w':
                    board.wPieces[index] = (nextRow, rightCol)
                else:
                    board.bPieces[index] = (nextRow, rightCol)


                board.replacechar(currRow, currCol, '-')
                board.replacechar(nextRow, rightCol, turn)

                newBoards += [board]
            
            elif self.board[nextRow][rightCol] == oppPieces:
                jumpCol = rightCol + rightJump
                
                if jumpRow < self.totalRows and jumpRow >= 0 and self.board[jumpRow][jumpCol] == '-':
                    board = deepcopy(self)               

                    board.replacechar(nextRow, rightCol, '-')

                    if turn == 'w':
                        board.bPieces.remove((nextRow, rightCol))
                    else:
                        board.wPieces.remove((nextRow, rightCol))

                    board.replacechar(currRow, currCol, '-')
                    board.replacechar(jumpRow, jumpCol, turn)

                    newBoards += [board]


        return newBoards

    
    def jumpdown(self, wpiece, windex, bpiece, bindex, diff):
        dothing = []
        



