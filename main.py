import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from connect_four import game

print(f'\n2 Human players: 1')
print(f'Player against AI: 2')
connect_four = game.Game()

try:
    print(f'\nPlease Enter 1 or 2: ', end='')
    input1 = int(input())
    if input1 == 1:
        print('-----------------------------------')
        print(f'Play text version: 1')
        print(f'Play GUI version: 2')

        try:
            print(f'\nPlease Enter 1 or 2: ', end='')
            input2 = int(input())

        except:
            print(f'')
        
        if input2 == 1:
            connect_four.play_text()

        elif input2 == 2:
            connect_four.play_gui()
        
        else:
            print(f'\nWrong input! Please Enter 1 or 2.')

    elif input1 == 2:
        connect_four.play_mcts()

    else:
        print(f'Wrong input! Please Enter 1 or 2.')

except KeyboardInterrupt:
    sys.exit()

except:
    print('end')
    # print(f'Wrong input! Please Enter 1 or 2.')

