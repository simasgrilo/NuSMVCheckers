for position in range(0,31):
    print("case position = {0}:".format(position))
    print("\tcase whois = 1:")
    if (position == 3 or position == 11 or position == 19 or position == 27 or position == 4 or position == 12  or position == 20):
        print("\t\tmove(board,{0},{1});".format(position,position+4))
    elif (position/4)%2 == 0:
    	print("\t\tmove(board,{0},{1});".format(position,position+4))
    	print("\t\tmove(board,{0},{1});".format(position,position+5))