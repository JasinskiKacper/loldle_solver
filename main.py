from modes import classic
import os
mode = ['Classic', 'Quote', 'Ability', 'Emoji', 'Splash']

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



if __name__ == '__main__':

    clear_terminal()
    
    print(f'=== Modes ===\n1.{mode[0]}\n2.{mode[1]}\n3.{mode[2]}\n4.{mode[3]}\n5.{mode[4]}\n0.Exit')

    choice = int(input('\nEnter mode: '))

    clear_terminal()

    if choice == 0:
        print('See you next time!')
    elif choice == 1:
        game = classic.Classic()
        game.start()