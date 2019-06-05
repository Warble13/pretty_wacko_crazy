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
    plant_direction1=randint(1,3)
    if plant_direction1==1:
        print('You grow for many years. As a plant. ')
    elif plant_direction1==2:
        print('A caterpillar eats you to become a butterlfy. ')
    elif plant_direction1==3:
        print('You die from lack of sunlight. ')

def wings_story():
    wings_answer=input('Would you like to fly? ')
    if wings_answer== 'yes' or wings_answer=='Yes':
        wings_direction1=randint(1,3)
        if wings_direction1==1:
            print('You are struck by a meteor shower. ')
        elif wings_direction1==2:
            print('You fly into a volcano. Dummy. ')
        elif wings_direction1==3:
            print('You are stuck by three bolts of lightning. It was raining. ')
    if wings_answer=='no' or wings_answer=='No':
        print('You sit on the ground. ')


intro()
initial_choice()
