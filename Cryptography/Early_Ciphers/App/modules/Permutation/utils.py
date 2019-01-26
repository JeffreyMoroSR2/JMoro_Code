import re, random

validator = "^[ a-z]{,}$"

alph = " abcdefghijklmnopqrstuvwxyz"
alph = list(alph)
copy_alph = "abcdefghijklmnopqrstuvwxyz"
len_copy_alph = len(copy_alph)
copy_alph_list = list(copy_alph)
random_alph = list(copy_alph)  # алфавіт, який змінюється рандомно
random.shuffle(random_alph)  # <- алфавіт змінюється рандомно
random_alph_list = list(random_alph)
dict_alph = {}
i = 0
while i < len(copy_alph):
    dict_alph[copy_alph[i]] = i
    i += 1

dict_rand = {}
a = 0
while a < len(random_alph):
    dict_rand[random_alph[a]] = a
    a += 1

DIR_NAME = ''
FILE_NAME_MESSAGE = 'modules\Permutation\message.txt'
FILE_NAME_CIPHERTEXT = 'modules\Permutation\cipher_text.txt'
FILE_NAME_KEY = 'modules\Permutation\key.txt'


def Generate_Key():
    key = random.choice(copy_alph)
    key_fie_name = DIR_NAME + FILE_NAME_KEY
    f = open(key_fie_name, 'w')
    f.write(key)
    f.close()
    print('Новий ключ згенеровано :', key)
    return key

def Cipher():
    while True:
        print("\nВведіть повідомлення для шифрування(1) або зчитайте з файлу(2): ", end="")
        b = input()
        if b == '1':
            message = input()
            if re.match(validator, message):
                break
            else:
                print("Ви ввели неправильне повідомлення")
        elif b == '2':
            mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
            f = open(mess_file_name, 'r')
            message = f.read()
            if re.match(validator, message):
                print('Текс повідомлення: ', message)
                break
            else:
                print("Ви ввели неправильне повідомлення")
        else:
            continue

    v = ''
    t = 0
    i = 0
    mess_num = []
    new_mess = []
    while i < len(message):
        v = message[i]
        iaa = dict_alph[v]
        mess_num.append(iaa)
        t = int(mess_num[i])
        new_mess += random_alph[t]
        i += 1

    print(f'\nРезультат п1: {new_mess}')

# Part 2
    while True:
        print("\nВведіть ключ(1) або згенеруйте(2): ", end="")
        c = input()
        if c == '1':
            key = input()
            if len(key) == 1 and re.match(validator, key):
                mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
                f = open(mess_file_name, 'w')
                f.write(message)
                f.close()
                break
            else:
                print("Ви ввели неправильний ключ")
        elif c == '2':
            key = Generate_Key()
            key_fie_name = DIR_NAME + FILE_NAME_KEY
            f = open(key_fie_name, 'w')
            f.write(key)
            f.close()
            break
        else:
            continue

    key = dict_alph[key]
    new_mess2 = ''
    for a in message:
        new_mess2 += copy_alph_list[(dict_rand[a] - key) % len_copy_alph] if a != " " else ' '

    new_mess2 = list(new_mess2)
    print(f'\nРезультат п2: {new_mess2}')

def Uncipher():
    pass

