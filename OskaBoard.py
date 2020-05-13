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
                
    
    # Straightforward board printing function. For each row, print it. Then print player's turn.
    def printBoard(self):
        for i in range(len(self.board)):

            print('Row #', i, ':', self.board[i])

        print('Player turn: ', self.playerTurn)



    # Function for replace characters in a board's character array.
    # 
    # Copies old string, but replaces old character with new character. Reassigns old row with newly created row string.
    #  
    # Inputs: row and column replacement is occuring at, character that is replacing 
    def replacechar(self, row, col, char):
        newStr = ''

        for i in range(len(self.board[row])):
            if i == col:
                newStr += char
            else:
                newStr += self.board[row][i]

        self.board[row] = newStr



    # Generate children of board
    # 
    # Inputs: player turn 
    def generatechildren(self, turn):

        # Declare list to hold new boards
        newBoards = []
        
        # For whichever player's turn it is, attempt to move each piece in their piece list
        if turn == 'w':
            for piece in self.wPieces:
                index = self.wPieces.index(piece)
                newBoards += self.moveprep(piece, index, turn)

        else:
            for piece in self.bPieces:
                index = self.bPieces.index(piece)
                newBoards += self.moveprep(piece, index, turn)

        # Return any boards generated
        if newBoards != []:
            return newBoards
        else:
            return None



    # Preps relevant data for use by "makemove" function.
    #   
    # makemove is modular, it will perform the correct move regardless of which player's turn it is or where the piece is on the board, 
    # so long as it is given the right inputs. moveprep determines where on the board the piece is, which player's piece it is,
    # where the piece could be moving to, and what the modifiers passed into makemove should be in order for it to make the proper move.
    #  
    # Inputs: piece object (tuple of row, col) to be moved, index of piece to be moved, player turn
    def moveprep(self, piece, index, turn):

        #Gather data from piece object into named variables
        currRow = piece[0]
        currCol = piece[1]
        
        #Declare pointers which will need to pull values out of future conditional statements
        oppTurn = nextRow = jumpRow = None
        
        #Prep default values for modifiers
        leftCol = currCol
        rightCol = currCol + 1
        leftJump = 0
        rightJump = 1

        #Set a variable to hold the name of the opponent
        if turn == 'w':
            oppTurn = 'b'
        else:
            oppTurn = 'w'

        #Based on whose turn it is, prepare any of the relevant modifiers that have not been prepared.
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
            nextRow = currRow - 1
            jumpRow = nextRow - 1
            if currRow >= (self.totalRows + 1) / 2:
                leftCol = currCol - 1
                rightCol = currCol
                if jumpRow > (self.totalRows - 1) / 2:
                    leftJump = -1
                    rightJump = 0
                
        #Call makemove function, passing necessary modifiers
        return self.makemove(index, turn, oppTurn, currRow, nextRow, jumpRow, currCol, ((leftCol, leftJump), (rightCol,  rightJump)))



    # Carries out the possible moves for a given piece, based on prep it is passed from moveprep
    # 
    # Inputs: piece index, player name, opponent name, row of piece, row piece could move to, row piece could jump to, current column of piece, 
    # possible columps piece could move to as nested tuples ((leftCol, leftJump), (rightCol, rightJump))
    def makemove(self, index, turn, oppTurn, currRow, nextRow, jumpRow, currCol, nextCols):
        
        # Declare empty list to hold boards
        newBoards = []

        # Attempt a move in each direction, left and right
        for nextCol in nextCols:

            # Ensure that both currRow and nextRow are within bounds of the board
            if currRow < self.totalRows and currRow >= 0 and nextRow < self.totalRows and nextRow >= 0 and nextCol[0] >= 0 and nextCol[0] < len(self.board[nextRow]):

                # If observed space is empty, move piece there
                if self.board[nextRow][nextCol[0]] == '-':

                    board = deepcopy(self)

                    # Call move function, passing where the piece is coming from and where it is moving to
                    board.genregmove(turn, index, (currRow, currCol), (nextRow, nextCol[0]))
                    newBoards += [board]
                    
                # If observed space is not empty, but is occupied by an opponents piece, attempt to jump it.
                elif self.board[nextRow][nextCol[0]] == oppTurn:

                    # Check to see if jump target space is empty. If it is, make jump.
                    jumpCol = nextCol[0] + nextCol[1] 
                    if jumpRow < self.totalRows and jumpRow >= 0 and self.board[jumpRow][jumpCol] == '-':

                        board = deepcopy(self)    

                        # Call jumping function, passing where the piece is coming from, which piece it is jumping, and where it is landing           
                        board.genjumpmove(turn, index, (currRow, currCol), (nextRow, nextCol[0]), (jumpRow, jumpCol))
                        newBoards += [board]

        # Return any generated boards
        return newBoards

    

    # Performs a move that is not a jump
    # 
    # Inputs: player name, index of piece moving, space piece is moving from <<fromSpace = (currRow, currCol)>>, 
    # space piece is moving to <<toSpace = (nextRow, nextCol)>> 
    def genregmove(self, turn, index, fromSpace, toSpace):

        # Reassign moving piece to new location in piece list
        if turn == 'w':
            self.bPieces[index] = (toSpace[0], toSpace[1])
            
        else:
            self.wPieces[index] = (toSpace[0], toSpace[1])
            
        # Update characters on the character list to reflect move
        self.replacechar(fromSpace[0], fromSpace[1], '-')
        self.replacechar(toSpace[0], toSpace[1], turn)



    # Perform a jump
    # 
    # Inputs: player name, index of piece jumping, space piece is jumping from <<fromSpace = (currRow, currCol)>>, 
    # space piece is jumping over <<nextSpace = (nextRow, nextCol)>>, space piece is jumping to <<jumpSpace = (jumpRow, jumpCol)>>
    def genjumpmove(self, turn, index, fromSpace, nextSpace, jumpSpace):
        
        # Reassign moving piece to new location in piece list
        # Remove jumped piece from piece list 
        if turn == 'w':
            self.bPieces.remove((nextSpace[0], nextSpace[1]))
            self.wPieces[index] = (jumpSpace[0], jumpSpace[1])
        else:
            self.wPieces.remove((nextSpace[0], nextSpace[1]))
            self.bPieces[index] = (jumpSpace[0], jumpSpace[1])

        # Update characters on the character list to reflect move
        self.replacechar(nextSpace[0], nextSpace[1], '-')
        self.replacechar(fromSpace[0], fromSpace[1], '-')
        self.replacechar(jumpSpace[0], jumpSpace[1], turn)
        



