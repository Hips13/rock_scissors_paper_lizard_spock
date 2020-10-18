import random

file = open('rating.txt', 'w')
file.close()

user_input = '0 0'
score = 0
list_f = []

name = input('Enter your name: ')
print('Hello,', name)


def start():
    file_list()
    new_name()
    menu()


def menu():
    global user_input
    global list_f
    try:
        user_input = input('')
    except EOFError:
        print("EOFError")
    if user_input == '':
        print("Okay, let's start")
        game()
    elif ',' in user_input:
        print("Okay, let's start")
        game_advansed()
    elif user_input == '!rating':
        rating_read()
        menu()
    elif user_input == '!exit':
        print('Bye!')
        pass
    else:
        print('Invalid input')


def file_list():
    global list_f
    file = open('rating.txt', 'r')
    list_f = file.readlines()
    file.close()
    for i in range(len(list_f)):
        if '\n' in list_f[i]:
            list_f[i] = list_f[i].replace('\n', '')


def new_name():
    global name
    global score
    global list_f
    line_temp = []
    file = open('rating.txt', 'r')
    for line in file:
        a, b = line.split(' ')
        line_temp.append(a)
        line_temp.append(b)
    file.close()
    if name not in line_temp:
        file = open('rating.txt', 'w')
        list_f.append(f'{name} {score}')
        file.write('\n'.join(list_f))
        file.close()


def rating_read():
    global list_f
    file = open('rating.txt', 'r')
    for line in file:
        if name in line:
            line_temp = line.split(' ')
            print('Your rating:', line_temp[1], end='')
    file.close()


def write():
    global list_f
    global score
    global name
    file_list()
    for i in range(len(list_f)):
        if name in list_f[i]:
            file = open('rating.txt', 'w')
            list_temp = list_f[i].split(' ')
            list_temp[1] = str(int(list_temp[1]) + score)
            list_f[i] = ' '.join(list_temp)
            file.write('\n'.join(list_f))
            file.close()


def game():
    global score
    variant = ['rock', 'scissors', 'paper']
    while True:
        pc = random.choice(variant)
        user_input = input('')
        if user_input == '!rating':
            rating_read()
        elif user_input == '!exit':
            break
        elif user_input in variant:
            if user_input == pc:
                score += 50
                write()
                print(f'There is a draw ({pc})')
                score = 0
            elif (user_input == variant[0]) and (pc == variant[2]):
                print(f'Sorry, but the computer chose {pc}')
            elif (user_input == variant[1]) and (pc == variant[0]):
                print(f'Sorry, but the computer chose {pc}')
            elif (user_input == variant[2]) and (pc == variant[1]):
                print(f'Sorry, but the computer chose {pc}')
            else:
                score += 100
                write()
                print(f'Well done. The computer chose {pc} and failed')
                score = 0
        else:
            print('Invalid input')


def game_advansed():
    global user_input
    global score
    words = user_input.split(',')
    words_base = [i for i in words]
    words_step = int((len(words) - 1) / 2)
    words *= 3
    while True:
        user_input = input()
        pc = random.choice(words_base)
        if user_input == '!rating':
            rating_read()
        elif user_input == '!exit':
            break
        elif user_input in words_base:
            usr_pos = words.index(user_input, len(words_base))
            if pc == user_input:
                score += 50
                write()
                print(f'There is a draw ({pc})')
                score = 0
            elif pc in words[usr_pos - words_step:usr_pos]:
                print(f"Sorry, but the computer chose {pc}")
            elif pc in words[usr_pos:usr_pos + words_step+1]:
                score += 100
                write()
                print(f'Well done. The computer chose {pc} and failed')
                score = 0
        else:
            print('Invalid input')


start()
