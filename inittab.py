for i in range (0,8):
    for j in range(0,8):
        if i%2 == 0 and j%2 == 0:
            print("\tinit(board[{0}][{1}]) := 0".format(i,j))
        elif i%2 == 1 and j%2 == 1:
            print("\tinit(board[{0}][{1}]) := 0".format(i,j))
