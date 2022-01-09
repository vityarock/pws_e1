import random
quest_list = ['skillfactory',
              'testing',
              'blackbox',
              'pytest',
              'unittest',
              'coverage']


def start():
    target = random.choice(quest_list)
    global foo
    foo = ['_' for i in target]
    counter = 0
    print(counter, 'counter')
    print(foo)
    game(target, counter)
    replay = input('Играть( y ) / Выход( anykey )')
    if replay == 'y':
        print('Продолжаем играть')
        start()
    else:
        print('Спасибо за игру')


def game(target, counter):
    for letter in range(len(target) + 4):
        if foo.count('_') == 0:
            message = 'Вы угадали все буквы в этом слове!'
            finish(message)
            break
        if counter == 4:
            message = 'Вы допустили 4 ошибки'
            finish(message)
            break
        answer = input_validation()
        flag = letter_check(target, answer)
        if flag is False:
            counter += 1
            print('Нет такой буквы в этом слове или буква уже открыта')
        print(foo, 'Ошибок', counter)


def input_validation():
    while True:
        answer = input('Введите загаданную букву: ')
        if len(answer) < 2 and answer.isalpha():
            print('Вы ввели букву ' + answer)
            return answer
        else:
            print('Пожалуйста введите 1 букву')


def letter_check(target, answer):
    flag = False
    for index, value in enumerate(target):
        if foo[index] != '_':
            continue
        if answer == value:
            print('Открываем ' + str(index + 1) + '-Ю букву')
            foo[index] = answer
            flag = True
    return flag


def finish(message):
    print(message)


if __name__ == '__main__':
    start()
