from random import randint


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
        wings_story()
    elif apple_choice=='yellow' or apple_choice==' the yellow one' or apple_choice=='the yellow apple':
        print('You burst into flames. ')
    else:
        print('Nothing happens. Choose again. ')
        initial_choice()

def plant_story():
    print('You grow for many years. As a plant. ')

def wings_story():
    wings_answer=input('Would you like to fly? ')
    if wings_answer== 'yes' or wings_answer=='Yes':
        wings_direction=randint(1,3)
        if wings_direction==1:
            print('You are struck by a meteor shower. ')
        elif wings_direction==2:
            print('You fly into a volcano. ')
        elif wings_direction==3:
            print('You are stuck by three bolts of lightning. It was raining. ')


intro()
initial_choice()
