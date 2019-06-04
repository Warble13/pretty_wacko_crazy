def intro():
    print('Welcome!')
    print('----')

def initial_choice():
    print('On the table before you, there is a green apple, a red apple and a yellow apple. ')
    apple_choice = input('Which of the three apple will you eat? ').lower()
    if apple_choice=='green' or apple_choice=='the green one' or apple_choice== 'the green apple':
        print('You become a plant. ')
        plant_story()
    elif apple_choice=='red' or apple_choice=='the red one' or apple_choice=='the red apple':
        print('You grow large wings. ')
    elif apple_choice=='yellow' or apple_choice==' the yellow one' or apple_choice=='the yellow apple':
        print('You burst into flames. ')
    else:
        print('Nothing happens. Choose again. ')
        initial_choice()

def plant_story():
    print('You grow for many years. As a plant. ')

intro()
initial_choice()
