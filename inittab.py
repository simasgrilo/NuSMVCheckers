for i in range (-1,4):
    for j in range(-1,4):
        if i< 0 or j < 0:
            print("\tinit(board[{0}][{1}]) := 5;".format(i, j))
        elif i%2 == 0 and j%2 == 0:
            print("\tinit(board[{0}][{1}]) := 0;".format(i,j))
        elif i%2 == 1 and j%2 == 1:
            print("\tinit(board[{0}][{1}]) := 0;".format(i,j))
        else:
            print("\tinit(board[{0}][{1}]) := 5;".format(i,j))
