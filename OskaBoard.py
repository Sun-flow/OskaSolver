from copy import deepcopy

# Set of classes for throwing errors in board intake functions. 
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
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##



# Object for an Oska board. Contains all relevent board manipulation and move generation functions.
class OskaBoard:



    # Board Constructor. Takes in a board as list of strings and converts it into a board object.
    # 
    # Inputs: list of strings, player colour character
    #  
    # Return: None 
    def __init__(self, inList, playerTurn):
   
        # Assign immediate variables for object
        self.totalRows = len(inList)
        self.maxRowLength = len(inList[0])
        pastCenter = 1

        if playerTurn == 'W' or playerTurn == 'w':
            self.playerTurn = 'w'
        elif playerTurn == 'B' or playerTurn == 'b':
            self.playerTurn = 'b'
        self.board = []

        # Attempt to convert list of strings into a board object.
        # If it fails or the list of strings is not a valid board, throw an error. 
        try: 

            # Ensure that board length is 2n - 3 where n is length of first row
            if self.totalRows == 2 * self.maxRowLength - 3:

                # Intake strings one at a time, each being a single row. If length is not expected length, throw error.
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
        

            #If board was valid structure, check for all pieces 
            self.findPieces()
        
        except InvalidRowLength as inst:
            print('Invalid row length: ', inst.args)
        except InvalidInput as inst:
            print('Invalid input: ', inst.args)

    

    # Function to find pieces and gather them into member variable lists. 
    # If too many pieces for a colour are found or an invalid character is found, throws error.
    # 
    # Inputs: None
    #  
    # Return: None 
    def findPieces(self):
        try:
            self.wPieces = []
            self.bPieces = []
            wCount = 0
            bCount = 0

            # Check each character in each row. If character is 'w' or 'b', add it's coordinates to its corresponding list.
            # If character is '-', ignore it. If character is none of the above, throw and error. 
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

            # If more pieces of a single colour were found than there were spaces in the first row, throw an error.
            if wCount > self.maxRowLength:
                raise TooManyPiece('W', self.wPieces)
            elif bCount > self.maxRowLength:
                raise TooManyPiece('B', self.bPieces)

        except InvalidPiece as inst:
            print('Invalid Piece: ', inst.args)
        except TooManyPiece as inst:
            print('Too many', inst.args[0], 'pieces')
                
    

    # Straightforward board printing function. For each row, print it. Then print player's turn.
    # 
    # Inputs: None
    #  
    # Return: None
    def printBoard(self):
        for i in range(len(self.board)):

            print('Row #', i, ':', self.board[i])

        print('Player turn: ', self.playerTurn)



    # Function for replace characters in a board's character array.
    # 
    # Copies old string, but replaces old character with new character. Reassigns old row with newly created row string.
    #  
    # Inputs: row and column replacement is occuring at, character that is replacing
    #  
    # Return: None 
    def replacechar(self, row, col, char):
        newStr = ''

        for i in range(len(self.board[row])):
            if i == col:
                newStr += char
            else:
                newStr += self.board[row][i]

        self.board[row] = newStr



    def movepiece(self, currRow, currCol, direction):
        
        nextCol = nextRow = jumpRow = jump = oppTurn = index= None

        if self.playerTurn == 'w':
            oppTurn = 'b'
        else:
            oppTurn = 'w'


        if self.playerTurn == 'w':
            index = self.wPieces.index((currRow, currCol))
            nextRow = currRow + 1
            jumpRow = nextRow + 1
            if currRow < (self.totalRows - 1) / 2:
                if direction == 'l' or direction == 'L':
                    nextCol = currCol - 1
                    if jumpRow <= (self.totalRows - 1) / 2:
                        jump = -1
                    else:
                        jump = 0
                else:
                    nextCol = currCol
                    if jumpRow <= (self.totalRows - 1) / 2:
                        jump = 0
                    else: 
                        jump = 1
            else:
                if direction == 'l' or direction == 'L':
                    nextCol = currCol
                    if jumpRow <= (self.totalRows - 1) / 2:
                        jump = -1
                    else:
                        jump = 0
                else:
                    nextCol = currCol + 1
                    if jumpRow <= (self.totalRows - 1) / 2:
                        jump = 0
                    else:
                        jump = 1
        else:
            index = self.bPieces.index(((currRow, currCol)))
            nextRow = currRow - 1
            jumpRow = nextRow - 1
            if currRow > (self.totalRows - 1) / 2:
                if direction == 'l' or direction == 'L':
                    nextCol = currCol - 1
                    if jumpRow >= (self.totalRows - 1) / 2:
                        jump = -1
                    else:
                        jump = 0
                else:
                    nextCol = currCol
                    if jumpRow >= (self.totalRows - 1) / 2:
                        jump = 0
                    else:
                        jump = 1
            else:
                if direction == 'l' or direction == 'L':
                    nextCol = currCol
                    if jumpRow >= (self.totalRows - 1) / 2:
                        jump = -1
                    else:
                        jump = 0
                else:
                    nextCol = currCol + 1
                    if jumpRow >= (self.totalRows - 1) / 2:
                        jump = 0
                    else:
                        jump = 1
    
                
        #Call makemove function, passing necessary modifiers
        return self.makemove(index, oppTurn, currRow, nextRow, jumpRow, currCol, ((nextCol, jump),))


    # Generate children of board
    # 
    # Inputs: None
    #  
    # Return: List of all boards that can be reached in one move 
    def generatechildren(self):

        # Declare list to hold new boards
        newBoards = []
        
        # For whichever player's turn it is, attempt to move each piece in their piece list
        if self.playerTurn == 'w':
            for piece in self.wPieces:
                index = self.wPieces.index(piece)
                newBoards += self.moveprep(piece, index, self.playerTurn, True)

        else:
            for piece in self.bPieces:
                index = self.bPieces.index(piece)
                newBoards += self.moveprep(piece, index, self.playerTurn, True)

        # Return any boards generated
        if newBoards != []:
            return newBoards
        else:
            thisBoard = deepcopy(self)
            if self.playerTurn == 'w':
                thisBoard.playerTurn = 'b'
            else:
                thisBoard.playerTurn = 'w'

            return [thisBoard]



    # Preps relevant data for use by "makemove" function.
    #   
    # makemove is modular, it will perform the correct move regardless of which player's turn it is or where the piece is on the board, 
    # so long as it is given the right inputs. moveprep determines where on the board the piece is, which player's piece it is,
    # where the piece could be moving to, and what the modifiers passed into makemove should be in order for it to make the proper move.
    #  
    # Inputs: piece object (tuple of row, col) to be moved, index of piece to be moved
    #  
    # Return: List of boards that can be reached by moving a specific piece
    def moveprep(self, piece, index, playerTurn, makingMove):

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
        if playerTurn == 'w':
            oppTurn = 'b'
        else:
            oppTurn = 'w'

        #Based on whose turn it is, prepare any of the relevant modifiers that have not been prepared.
        if playerTurn == 'w':
            nextRow = currRow + 1
            jumpRow = nextRow + 1
            if currRow < (self.totalRows - 1) / 2:
                leftCol = currCol - 1
                rightCol = currCol
                if jumpRow <= (self.totalRows - 1) / 2:
                    leftJump = -1
                    rightJump = 0
        else:
            nextRow = currRow - 1
            jumpRow = nextRow - 1
            if currRow > (self.totalRows - 1) / 2:
                leftCol = currCol - 1
                rightCol = currCol
                if jumpRow >= (self.totalRows - 1) / 2:
                    leftJump = -1
                    rightJump = 0
                
        if makingMove:
            #Call makemove function, passing necessary modifiers
            return self.makemove(index, oppTurn, currRow, nextRow, jumpRow, currCol, ((leftCol, leftJump), (rightCol,  rightJump)))
        else:
            return (self.canMove(nextRow, (leftCol, rightCol)), self.canJump(oppTurn, nextRow, jumpRow, currCol, ((leftCol, leftJump), (rightCol,  rightJump))))



    # Carries out the possible moves for a given piece, based on prep it is passed from moveprep
    # 
    # Inputs: piece index, opponent color, row of piece, row piece could move to, row piece could jump to, current column of piece, 
    # possible columps piece could move to as nested tuples <<((leftCol, leftJump), (rightCol, rightJump))>>
    #  
    # Return: List of boards that can be reached by moving a specific piece
    def makemove(self, index, oppTurn, currRow, nextRow, jumpRow, currCol, nextCols):
        
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
                    board.genregmove(index, (currRow, currCol), (nextRow, nextCol[0]))
                    board.playerTurn = oppTurn
                    newBoards += [board]
                    
                # If observed space is not empty, but is occupied by an opponents piece, attempt to jump it.
                elif self.board[nextRow][nextCol[0]] == oppTurn:

                    # Check to see if jump target space is empty. If it is, make jump.
                    jumpCol = nextCol[0] + nextCol[1] 
                    if jumpRow < self.totalRows and jumpRow >= 0 and jumpCol >= 0 and jumpCol < len(self.board[jumpRow]) and self.board[jumpRow][jumpCol] == '-':

                        board = deepcopy(self)    

                        # Call jumping function, passing where the piece is coming from, which piece it is jumping, and where it is landing           
                        board.genjumpmove(index, (currRow, currCol), (nextRow, nextCol[0]), (jumpRow, jumpCol))
                        board.playerTurn = oppTurn
                        newBoards += [board]

        # Return any generated boards
        return newBoards

    

    # Performs a move that is not a jump
    # 
    # Inputs: index of piece moving, space piece is moving from <<fromSpace = (currRow, currCol)>>, 
    # space piece is moving to <<toSpace = (nextRow, nextCol)>>
    #  
    # Return: None  
    def genregmove(self, index, fromSpace, toSpace):

        # Reassign moving piece to new location in piece list
        if self.playerTurn == 'w':
            self.wPieces[index] = (toSpace[0], toSpace[1])
            
        else:
            self.bPieces[index] = (toSpace[0], toSpace[1])
            
        # Update characters on the character list to reflect move
        self.replacechar(fromSpace[0], fromSpace[1], '-')
        self.replacechar(toSpace[0], toSpace[1], self.playerTurn)



    # Perform a jump
    # 
    # Inputs: player name, index of piece jumping, space piece is jumping from <<fromSpace = (currRow, currCol)>>, 
    # space piece is jumping over <<nextSpace = (nextRow, nextCol)>>, space piece is jumping to <<jumpSpace = (jumpRow, jumpCol)>>
    #  
    # Return: None 
    def genjumpmove(self, index, fromSpace, nextSpace, jumpSpace):
        
        # Reassign moving piece to new location in piece list
        # Remove jumped piece from piece list 
        if self.playerTurn == 'w':
            self.bPieces.remove((nextSpace[0], nextSpace[1]))
            self.wPieces[index] = (jumpSpace[0], jumpSpace[1])
        else:
            self.wPieces.remove((nextSpace[0], nextSpace[1]))
            self.bPieces[index] = (jumpSpace[0], jumpSpace[1])

        # Update characters on the character list to reflect move
        self.replacechar(nextSpace[0], nextSpace[1], '-')
        self.replacechar(fromSpace[0], fromSpace[1], '-')
        self.replacechar(jumpSpace[0], jumpSpace[1], self.playerTurn)


    def boardeval(self):

        if self.playerTurn == 'b' and self.gameover():
            return 1000
        elif self.playerTurn == 'w' and self.gameover():
            return -1000

        wNum = len(self.wPieces)
        bNum = len(self.bPieces)

        val = (wNum - bNum)
        #print(val)
        wDist = 0
        for wpiece in self.wPieces:
            wDist += self.totalRows - wpiece[0] - 1

        bDist = 0
        for bpiece in self.bPieces:
            bDist += bpiece[0]

        val += bDist - wDist

        #print(val)
        for piece in self.wPieces:
            index = self.wPieces.index(piece)
            moves = self.moveprep(piece, index, 'w', False)
            #print(moves)
            if moves[0] > 0:
                val += 1
            val += moves[1]

        #print(val)
        for piece in self.bPieces:
            index = self.bPieces.index(piece)
            moves = self.moveprep(piece, index, 'b', False)
            if moves[0] > 0:
                val += -1
            val += -moves[1]

        #print(val)

        #wInGoal = False
        #bInGoal = False
        wGoalCount = 0
        bGoalCount = 0
        for char in self.board[0]:
            if char == 'b':
        #        bInGoal = True
                bGoalCount += 1

        for char in self.board[self.totalRows - 1]:
            if char == 'w':
        #        wInGoal = True
                wGoalCount += 1

        val += wGoalCount - bGoalCount
        

        #eval += self.maxRowLength * wGoalCount
        #eval += self.maxRowLength * bGoalCount * -1

        #if wInGoal == True:
        #    eval += (len(self.wPieces) - wGoalCount) * (-1)
        
        #if bInGoal == True:
        #    eval += (len(self.bPieces) - bGoalCount)    

        return val


    def canMove(self, nextRow, nextCols):
        openMoves = 0
        for col in nextCols:
            #print('nextRow:',nextRow)
            #print('nextCol:',col)


            if nextRow < self.totalRows and nextRow >= 0 and col >= 0 and col < len(self.board[nextRow]) and self.board[nextRow][col] == '-':
                openMoves += 1

        return openMoves


    def canJump(self, oppTurn, nextRow, jumpRow, currCol, nextCols):
        availableJumps = 0
        #print(nextCols)
        for col in nextCols:
            nextCol = col[0]
            jumpCol = nextCol + col[1]

            #print('nextRow:',nextRow)
            #print('jumpRow:',jumpRow)
            #print('nextCol:',nextCol)
            #print('jumpCol:',jumpCol)

            if nextRow < self.totalRows and jumpRow < self.totalRows and nextRow >= 0 and jumpRow >= 0 and nextCol >= 0 and jumpCol >= 0 and nextCol < len(self.board[nextRow]) and jumpCol < len(self.board[jumpRow]) and self.board[nextRow][nextCol] == oppTurn and self.board[jumpRow][jumpCol] == '-':
                availableJumps += 1

        return availableJumps       

        


    def wWin(self):
        if len(self.bPieces) == 0:
            return True
        count = 0
        for char in self.board[self.totalRows - 1]:
            if char == 'w':
                count += 1

        if count != 0 and count == len(self.wPieces):
            return True

    def bWin(self):
        if len(self.wPieces) == 0:
            return True
        count = 0
        for char in self.board[0]:
            if char == 'b':
                count += 1

        if count != 0 and count == len(self.bPieces):
            return True

    def gameover(self):
        if len(self.wPieces) == 0:
            return True
        if len(self.bPieces) == 0:
            return True


        if self.playerTurn == 'w' and self.bWin() == True:
            return True
        elif self.playerTurn == 'b' and self.wWin() == True:
            return True