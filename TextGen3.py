for lin in range (0,5):
    for col in range(0,5):
        if lin%2 == 0 and col%2 == 0:
            print("\tnext(board[{0}][{1}]) := case".format(lin,col))
            print("\t\t\t\t\t\t\tlin = {0} & col = {1} & (canMove): 0;".format(lin,col))
            print("\t\t\t\t\t\t\tcanMove & whoIs = 1 & {0} = linUp & (({0} = diagDir & movN = 1)|({0} = diagEsq & movN = 2)):1".format(lin))
            print("\t\t\t\t\t\t\tcanMove & whoIs = 2 & {0} = linDw & (({0} = diagDir & movN = 1)|({0} = diagEsq & movN = 2)):3".format(lin))
            print("\t\t\t\t\t\t\tTRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t esac;")
        elif lin%2 == 1 and col%2 == 1:
            print("\tnext(board[{0}][{1}]) := case".format(lin,col))
            print("\t\t\t\t\t\t\tlin = {0} & col = {1} & (canMove): 0;".format(lin,col))
            print("\t\t\t\t\t\t\tcanMove & whoIs = 1 & {0} = linUp & (({0} = diagDir & movN = 1)|({0} = diagEsq & movN = 2)):1".format(lin))
            print("\t\t\t\t\t\t\tcanMove & whoIs = 2 & {0} = linDw & (({0} = diagDir & movN = 1)|({0} = diagEsq & movN = 2)):3".format(lin))
            print("\t\t\t\t\t\t\tTRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t esac;")
        else:
            print("\tnext(board[{0}][{1}]) := board[{0}][{1}];".format(lin,col))
