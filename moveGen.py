for lin in range (0,8):
    for col in range (0,8):
        if lin%2 == 0 and col%2 == 0:
            print("\tmove{0}{1}: process move(board,whoIs,pecas1,pecas2,{0},{1});".format(lin,col))
        elif lin%2 == 1 and col%2 == 1:
            print("\tmove{0}{1}: process move(board,whoIs,pecas1,pecas2,{0},{1});".format(lin,col))
