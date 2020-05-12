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


    def movewhite(self):
        newBoards = []
        
        for piece in self.wPieces:
            index = self.wPieces.index(piece)
            row = piece[0]
            print(
                'Piece:', piece,
                '\nindex:', index
            )
            if row < (self.totalRows - 1) / 2:
                newBoards += self.movedown(0, piece, index)
            else:
                newBoards += self.movedown(1, piece, index)
        if newBoards != []:
            return newBoards
        else:
            return None

    def movedown(self, mode, piece, index):
        newBoards = []
        currRow = piece[0]
        currRowLen = len(self.board[currRow])
        currCol = piece[1]
        nextRow = currRow + 1
        jumpRow = nextRow + 1
        nextRowLen = None
        leftCol = None
        rightCol = None
        leftJump = None
        rightJump = None


        if mode == 0:
            nextRowLen = -1
            leftCol = currCol - 1
            rightCol = currCol
            leftJump = -1
            rightJump = 0
        elif mode == 1:
            nextRowLen = 1
            leftCol = currCol
            rightCol = currCol + 1
            leftJump = 0
            rightJump = 1

        if leftCol >= 0:
            if self.board[nextRow][leftCol] == '-':

                board = deepcopy(self)
                
                board.wPieces[index] = (nextRow, leftCol)
                
                board.replacechar(currRow, currCol, '-')
                board.replacechar(nextRow, leftCol, 'w')
                
                newBoards += [board]
            elif self.board[nextRow][leftCol] == 'b':
                jumpCol = leftCol + leftJump
                
                if jumpRow < self.totalRows and self.board[jumpRow][jumpCol] == '-':
                    board = deepcopy(self)
                
                    board.wPieces[index] = (jumpRow, jumpCol)
                    
                    board.replacechar(nextRow, leftCol, '-')
                    board.replacechar(currRow, currCol, '-')
                    board.replacechar(jumpRow, jumpCol, 'w')
            

        if rightCol < currRowLen + nextRowLen and currRow < self.totalRows:
            if self.board[nextRow][rightCol] == '-':
                board = deepcopy(self)

                board.wPieces[index] = (nextRow, currCol)

                board.replacechar(currRow, currCol, '-')
                board.replacechar(nextRow, rightCol, 'w')

                newBoards += [board]
            
            elif self.board[nextRow][rightCol] == 'b':
                jumpCol = rightCol + rightJump
                
                if jumpRow < self.totalRows and self.board[jumpRow][jumpCol] == '-':
                    board = deepcopy(self)
                
                    board.wPieces[index] = (jumpRow, jumpCol)
                    
                    board.replacechar(nextRow, rightCol, '-')

                    board.replacechar(currRow, currCol, '-')
                    board.replacechar(jumpRow, jumpCol, 'w')

                    newBoards += [board]


        return newBoards

    
    def jumpdown(self, wpiece, windex, bpiece, bindex, diff):

        dothing = []



    def moveblack(inBoard):
        newboards = []