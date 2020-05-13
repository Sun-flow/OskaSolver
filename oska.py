import OskaBoard




def generatechildren(inBoard, playerTurn):
    return inBoard.generatechildren(playerTurn)


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

    newBoard7 = OskaBoard.OskaBoard(['--w--','-b--','---','--','---','-ww-','-bb--'], 'b')
    newBoard7.printBoard()

    newChildren7 = generatechildren(newBoard7, 'b')
    for child in newChildren7:
        child.printBoard()
