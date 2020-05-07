class Error(Exception):
    pass

class InvalidRowLength(Error):
    pass

class InvalidInput(Error):
    pass



class Oska:

    def __init__(self, inList):
        totalRows = len(inList)
        maxRowLength = len(inList[0])

        print

        self.board = []

        #TODO: Check to make sure there are not too many pieces on the board (> maxRowLength). Could keep a counter for W and B, increment when it is found. Or do a check after board import.
        try: 
            if totalRows == 2 * maxRowLength - 3:

                rowNum = 0
                for row in inList:
                    print('Row #', rowNum, ': ', row)
                    if rowNum <= (totalRows - 1) / 2:
                        if len(inList[rowNum]) == maxRowLength - rowNum:
                            self.board += row
                        else:
                            raise InvalidRowLength(1, rowNum, inList[rowNum])
                    elif rowNum == (((totalRows - 1) / 2)):
                        if len(inList[rowNum]) == 2:
                            self.board += row
                        else:
                            raise InvalidRowLength(2, rowNum, inList[rowNum])
                    elif rowNum >= (totalRows + 1) / 2:
                        if len(inList[rowNum]) == totalRows - (totalRows - rowNum):
                            self.board += row
                        else:
                            raise InvalidRowLength(3, rowNum, inList[rowNum])

                    rowNum += 1

            else:
                raise InvalidInput(inList)

        except InvalidRowLength as inst:
            print('Invalid row length: ', inst.args)
        except InvalidInput as inst:
            print('Invalid input: ', inst.args)


    def printBoard(self):
        for row in self.board:
            print(row)
        


def testinput():

    newBoard = Oska(['wwww','---','--','---','bbbb'])

    newBoard.printBoard()