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

    def class OskaPiece:
    def __init__(self, char, row, col):
        self.piece = char
        self.row = row
        self.col = col

    def __init__(self, inList, playerTurn):
        self.totalRows = len(inList)
        self.maxRowLength = len(inList[0])
        pastCenter = 1
        self.playerTurn = playerTurn
        self.board = []

        #TODO: Check to make sure there are not too many pieces on the board (> self.maxRowLength). Could keep a counter for W and B, increment when it is found. Or do a check after board import.
        try: 
            if self.totalRows == 2 * self.maxRowLength - 3:

                rowNum = 0
                for row in inList:
                    if rowNum <= (self.totalRows - 1) / 2:
                        if len(inList[rowNum]) == self.maxRowLength - rowNum:
                            self.board += [row]
                        else:
                            raise InvalidRowLength(1, rowNum, inList[rowNum])
                    else:
                        if len(inList[rowNum]) == 2 + pastCenter:
                            pastCenter += 1
                            self.board += [row]
                        else:
                            raise InvalidRowLength(3, rowNum, inList[rowNum])

                    rowNum += 1

            else:
                raise InvalidInput(inList)
        
            self.board.findPieces()
        
        except InvalidRowLength as inst:
            print('Invalid row length: ', inst.args)
        except InvalidInput as inst:
            print('Invalid input: ', inst.args)

        

    

    def findPieces(self):
        try:
            self.wPieces = []
            self.bPieces = []
            for row in range(len(self.board)):
                for col in range(len(row)):
                    char = self.board[row][col]
                    if char == 'W' or char == 'w':
                        self.wPieces += OskaPiece(char, row, col)
                    elif char == 'B' or char == 'b':
                        self.bPieces += OskaPiece(char, row, col)
                    elif char != '-':
                        raise InvalidPiece(char, row, col)

            if len(self.wPieces) > self.maxRowLength:
                raise TooManyPiece('W', self.wPieces)
            elif len(self.bPieces) > self.maxRowLength:
                raise TooManyPiece('B', self.bPieces)

        except InvalidPiece as inst:
            print('Invalid Piece: ', inst.args)
        except TooManyPiece as inst:
            print('Too many ', inst.args[0], 'pieces')
                
        



    def printBoard(self):
        for i in range(len(self.board)):
            print('Row #', i, ': ', self.board[i])

        print('Player turn: ', self.playerTurn)