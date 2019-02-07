import sys
for turn in range(1,6):
    for play in range(1,3):
        for symbol in range(0,3):
            if symbol == 0:
                out = 'r'
            elif symbol == 1:
                out = 'p'
            elif symbol == 2:
                out = 's'
            sys.stdout.write('\'P' + str(play) + '.' + str(turn) + out + "', ")
