class Error(Exception):
    pass

class InvalidRowLength(Error):
    pass

class InvalidInput(Error)



class Oska:

    def __init__(self, inList):
        totalRows = len(inList)
        maxRowLength = len(inList[0])

        self.board = []

        #TODO: Check to make sure there are not too many pieces on the board (> maxRowLength). Could keep a counter for W and B, increment when it is found. Or do a check after board import.
        try: 
            if totalRows == 2 * maxRowLength - 3:

                rowNum = 0
                for row in inList:
                    if rowNum <= (totalRows - 1) / 2:
                        if len(inList[rowNum]) == maxRowLength - rowNum:
                            self.board[rowNum] = inList[rowNum]
                        else:
                            raise InvalidRowLength(rowNum, inList[rowNum])
                    elif rowNum == (((totalRows - 1) / 2) + 1):
                        if len(inList[rowNum]) == 2:
                            self.board[rowNum] = inList[rowNum]
                        else:
                            raise InvalidRowLength(rowNum, inList[rowNum])
                    elif rowNum >= (totalRows + 1) / 2:
                        if len(inList[rowNum]) == 2 + (rowNum - (totalRows / 2)):
                            self.board[rowNum] = inList[rowNum]
                        else:
                            raise InvalidRowLength(rowNum, inList[rowNum])

                    self.board[rowNum] = row
                    row += 1

            else:
                raise InvalidInput(inList)

        except InvalidRowLength as inst:
            print('Invalid row length: ', inst.args)
        except InvalidInput as inst:
            print('Invalid input: ', inst.args)
        
        