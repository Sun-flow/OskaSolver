import OskaBoard

# Required move-generation function.
# 
# Inputs: Oska board of any length as list, moving player's turn
# 
# Return: List of boards that can be reached from current board in a single move  
def movegen(inBoard, playerTurn):
    Board = OskaBoard.OskaBoard(inBoard, playerTurn)
    return Board.generatechildren()



# Function for testing other functions. Makes it easy for me to test things without having to type them in over and over. 
# Leaving it here so that I don't have a file with just one function hanging around awkwardly.
def testinput():

    #newBoard = OskaBoard.OskaBoard(['www-','---','-w','---','bbbb'], 'W')
    #newBoard.printBoard()

    #newBoard2 = OskaBoard.OskaBoard(['ww-w-','----','---','-w','--w','----','bbbbb'], 'W')
    #newBoard2.printBoard()

    #newBoard3 = OskaBoard.OskaBoard(['wwwww','----','---','---','----','bbbbb'], 'W')

    #newBoard4 = OskaBoard.OskaBoard(['wwww-w','---w-','----','---','--','---','-b--','-----','b-bbbb'], 'W')
    #newBoard4.printBoard()

    #newBoard5 = OskaBoard.OskaBoard(['wwww','w--','--','---','bbbb'], 'W')
    #newBoard5.printBoard()

    #newBoard6 = OskaBoard.OskaBoard(['wwwq','---','--','---','bbbb'], 'W')
    #newBoard6.printBoard()

    #newChildren = generatechildren(newBoard, 'w')
    #for child in newChildren:
    #    child.printBoard()

    #newChildren2 = generatechildren(newBoard2, 'w')
    #for child in newChildren2:
    #    child.printBoard()

    #newChildren7b = movegen(newBoard7, 'b')
    #for child in newChildren7b:
    #    child.printBoard()

    newChildren7w = movegen(['--ww--','--b--','-w--','-b-','-w','---','----','-----','------'], 'b')
    for child in newChildren7w:
        child.printBoard()
    
