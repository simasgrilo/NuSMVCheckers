for position in range(0,32):
    print("\t\tcase position = {0}:".format(position))
    col = position%4
    lin = position/4
    print("\t\t\tcase whois = 1:")
    if (position == 3 or position == 11 or position == 19 or position == 27 or position == 4 or position == 12  or position == 20):
    elif (col%2) == 0 and lin < 7:
    elif (col%2) == 1 and lin < 7:
    else: print("\t\t\t\t;")
    print("\t\t\tcase whois = 2:")
    if (position == 11 or position == 19 or position == 27 or position == 4 or position == 12  or position == 20 or position == 28):
    elif (col%2) == 0 and lin >= 1:
    elif (col%2) == 1 and lin >= 1:
    else: print("\t\t\t\t;")
    print("\t\t\tcase TRUE:;\n\t\t\tesac;")
print("\t\tcase TRUE:;\n\t\tesac;")

