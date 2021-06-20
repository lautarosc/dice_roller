import random

# The ASCII dices and the rights of the design are of Valkyrie from https://www.asciiart.eu/miscellaneous/dice

def main():
    print('\t   Dice roller!')
# The r before the ''' ''' is for RAW PRINT, super useful for printing ASCII art!
    print(r'''                         
      ____
     /\' .\    _____
    /: \___\  / .  /\
    \' / . / /____/..\
     \/___/  \'  '\  /
              \'__'\/
              
1) Roll dice! (this option by default is from 1 to 5)
2) Choose how many sides you want
3) Quit program''')

    user_choice = int(input('Choose an option: '))

    while user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4:
        user_choice = int(input('Enter a valid option: '))

    if user_choice == 1:
        option_1()
    elif user_choice == 2:
        print()
        option_2()
    elif user_choice == 3:
        option_3()
    elif user_choice == 4:
        option_4()


def option_1():
    rand1 = random.randint(1, 5)
    print('**********')
    print(rand1)
    ask = input('Roll again? (y/n): ')

    if ask.lower() != 'y' and ask.lower() != 'n':
        while ask != 'y' and ask != 'n':
            ask = input('Please enter Y or N: ')

    while ask.lower() == 'y':
        print(random.randint(1, 5))
        ask = input('Roll again? (y/n): ')
    if ask.lower() == 'n':
        print('Done!')
        print('**********')
        main()


def option_2():
    number_of_sides = int(input('Enter number of sides: '))

    rand1 = random.randint(1, number_of_sides)
    print(rand1)
    ask = input('Roll again? (y/n): ')

    if ask.lower() != 'y' and ask.lower() != 'n':
        while ask != 'y' and ask != 'n':
            ask = input('Please enter Y or N: ')

    while ask.lower() == 'y':
        print(random.randint(1, number_of_sides))
        ask = input('Roll again? (y/n): ')
    if ask.lower() == 'n':
        print('Done!')
        print('**********')
        print()
        main()


def option_3():
    print()
    print('**********')
    print('Thank you for using 6ER\'s Dice Roller!')
    print('See you soon!')
    print('**********')
    quit()


def option_4():
    print()
    print(r'''You have chosen the secret option!
Congratulations on finding this secret. My regards. 
Unfortunately, I don't actually have anything on me to reward you with...
So here's an ASCII banana as a price: 

 _
//\
V  \
 \  \_
  \,'.`-.
   |\ `. `.       
   ( \  `. `-.                        _,.-:\
    \ \   `.  `-._             __..--' ,-';/
     \ `.   `-.   `-..___..---'   _.--' ,'/
      `. `.    `-._        __..--'    ,' /
        `. `-_     ``--..''       _.-' ,'
          `-_ `-.___        __,--'   ,'
             `-.__  `----"""    __.-'
                  `--..____..--'

1) Go back to menu
2) Quit program''')

    ask = int(input('Enter an option: '))

    while ask != 1 and ask != 2:
        ask = int(input('1 or 2: '))

    if ask == 1:
        main()
    elif ask == 2:
        quit()

    # ASCII banana's rights are of https://www.asciiart.eu/food-and-drinks/bananas

main()
