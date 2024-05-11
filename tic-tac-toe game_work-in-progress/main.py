#variables
playing_field = ["#", "#", "#",
                 "#","#","#",
                 "#","#","#"] # 0 = empty, 1 = X, 2 = O
who_won = None # X, O, None


#functions
def print_field():
    print(playing_field[0], playing_field[1], playing_field[2])
    print(playing_field[3], playing_field[4], playing_field[5])
    print(playing_field[6], playing_field[7], playing_field[8])  

#main
print_field()