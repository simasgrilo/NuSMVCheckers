for lin in range (0,8):
    for col in range(0,8):
        if lin%2 == 0 and col%2 == 0:
            print("\tnext(board[{0}][{1}]) := case".format(lin,col))
            print("\t\t\t\t\t\t\tlin = {0} & col = {1} & canMove: 0;".format(lin,col))
            print("\t\t\t\t\t\t\tcanMove & whoIs = 1 & {0} = linUp & ({1} = diagEsq | {1} = diagDir): 1;".format(lin,col))
            print("\t\t\t\t\t\t\tcanMove & whoIs = 2 & {0} = linDw & ({1} = diagEsq | {1} = diagDir): 3;".format(lin,col))
            print("\t\t\t\t\t\t\tTRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t esac;")
        elif lin%2 == 1 and col%2 == 1:
            print("\tnext(board[{0}][{1}]) := case".format(lin,col))
            print("\t\t\t\t\t\t\tlin = {0} & col = {1} & canMove: 0;".format(lin,col))
            print("\t\t\t\t\t\t\tcanMove & whoIs = 1 & {0} = linUp & ({1} = diagEsq | {1} = diagDir): 1;".format(lin,col))
            print("\t\t\t\t\t\t\tcanMove & whoIs = 2 & {0} = linDw & ({1} = diagEsq | {1} = diagDir): 3;".format(lin,col))
            print("\t\t\t\t\t\t\tTRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t esac;")
