for lin in range (0,8):
    for col in range(0,8):
        if lin%2 == 0 and col%2 == 0:
            print("\tnext(board[{0}][{1}]) := case".format(lin,col))
            print("\t\t\t\t\t\t\tlin = {0} & col = {1} & (canMove | canJump): 0;".format(lin,col))
            print("\t\t\t\t\t\t\tcanJump & {0} = linUp & ({1} = diagDir | {1} = diagEsq): 0;".format(lin,col))
            print("\t\t\t\t\t\t\tcanJump & {0} = lin2Up & ({1} = diagDir | {1} = diagEsq):case".format(lin,col))
            print("\t\t\t\t\t\t\t\t whoIs = 1: 1;")
            print("\t\t\t\t\t\t\t\t whoIs = 2: 3;")
            print("\t\t\t\t\t\t\t\t TRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t\t\tesac;")
            print("\t\t\t\t\t\t\t!canJump & canMove & whoIs = 1 & {0} = linUp:case".format(lin))
            print("\t\t\t\t\t\t\t\t {0} = diagDir & movNum = 1: 1;".format(col))
            print("\t\t\t\t\t\t\t\t {0} = diagDir & movNum = 2: 1;".format(col))
            print("\t\t\t\t\t\t\t\t TRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t\t\tesac;")
            print("\t\t\t\t\t\t\t!canJump & canMove & whoIs = 2 & {0} = linDw:case".format(lin))
            print("\t\t\t\t\t\t\t\t {0} = diagDir & movNum = 1: 3;".format(col))
            print("\t\t\t\t\t\t\t\t {0} = diagDir & movNum = 2: 3;".format(col))
            print("\t\t\t\t\t\t\t\t TRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t\t\tesac;")
            print("\t\t\t\t\t\t\tTRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t esac;")
        elif lin%2 == 1 and col%2 == 1:
            print("\tnext(board[{0}][{1}]) := case".format(lin,col))
            print("\t\t\t\t\t\t\tlin = {0} & col = {1} & canMove: 0;".format(lin,col))
            print("\t\t\t\t\t\t\tcanJump & {0} = linUp & ({1} = diagDir | {1} = diagEsq): 0;".format(lin,col))
            print("\t\t\t\t\t\t\tcanJump & {0} = lin2Up & ({1} = diagDir | {1} = diagEsq):case".format(lin,col))
            print("\t\t\t\t\t\t\t\t whoIs = 1: 1;")
            print("\t\t\t\t\t\t\t\t whoIs = 2: 3;")
            print("\t\t\t\t\t\t\t\t TRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t\t\tesac;")
            print("\t\t\t\t\t\t\t\t {0} = diagDir & movNum = 1: 1;".format(col))
            print("\t\t\t\t\t\t\t\t {0} = diagDir & movNum = 2: 1;".format(col))
            print("\t\t\t\t\t\t\t\t TRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t\t\tesac;")
            print("\t\t\t\t\t\t\t\t {0} = diagDir & movNum = 1: 3;".format(col))
            print("\t\t\t\t\t\t\t\t {0} = diagDir & movNum = 2: 3;".format(col))
            print("\t\t\t\t\t\t\t\t TRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t\t\tesac;")
            print("\t\t\t\t\t\t\tTRUE: board[{0}][{1}];".format(lin,col))
            print("\t\t\t\t\t\t esac;")
