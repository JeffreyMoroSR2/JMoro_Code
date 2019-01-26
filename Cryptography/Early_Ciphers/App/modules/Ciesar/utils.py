import re, random
validator = "^[ a-z]{,}$"

alph = " abcdefghijklmnopqrstuvwxyz"
alph = list(alph)
copy_alph = "abcdefghijklmnopqrstuvwxyz"
len_copy_alph =len(copy_alph)
copy_alph_list = list(copy_alph)
dict_alph = {}
i = 0
while i < len(copy_alph):
    dict_alph[copy_alph[i]]=i
    i += 1

DIR_NAME = ''
FILE_NAME_MESSAGE = 'modules\Ciesar\message.txt'
FILE_NAME_CIPHERTEXT = 'modules\Ciesar\cipher_text.txt'
FILE_NAME_KEY = 'modules\Ciesar\key.txt'

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
        print("\nВведіть повідомлення для шифрування(1) або Зчитайте з файлу(2): (a-z): ", end="")
        c = input()
        if c == '1':
            message = input()
            if re.match(validator, message):
                mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
                f = open(mess_file_name, 'w')
                f.write(message)
                f.close()
                break
            else:
                print("Ви ввели неправильне повідомлення")
        elif c == '2':
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

    while True:
        print("\nВведіть ключ (a-z) (1) або згенеруйте автоматично(2): ", end="")
        b = input()
        if b == '1':
            print('\nВведіть ключ')
            key = input()
            if len(key) == 1 and re.match(validator, key):
                key_fie_name = DIR_NAME + FILE_NAME_KEY
                f = open(key_fie_name, 'w')
                f.write(key)
                f.close()
                break
            else:
                print("Ви ввели неправильний ключ")
        elif b == '2':
            key = Generate_Key()
            break
        else:
            continue

    key = dict_alph[key]
    new_mess = ''
    for a in message:
        new_mess += copy_alph_list[(dict_alph[a] + key) % len_copy_alph] if a != " " else ' '

    print(f'\nРезультат: {new_mess}')
    cipher_file_name = DIR_NAME + FILE_NAME_CIPHERTEXT
    f = open(cipher_file_name, 'w')
    f.write(new_mess)
    f.close()

def Uncipher():
    while True:
        print("\nВведіть повідомлення для розшифрування(1) або Зчитайте з файлу(2): (a-z): ", end="")
        c = input()
        if c == '1':
            message = input()
            if re.match(validator, message):
                mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
                f = open(mess_file_name, 'w')
                f.write(message)
                f.close()
                break
            else:
                print("Ви ввели неправильне повідомлення")
        elif c == '2':
            cipher_file_name = DIR_NAME + FILE_NAME_CIPHERTEXT
            f = open(cipher_file_name, 'r')
            message = f.read()
            if re.match(validator, message):
                print('Текст повідомлення: ', message)
                break
            else:
                print("Ви ввели неправильне повідомлення")
        else:
            continue

    while True:
        print("\nВведіть ключ (a-z) (1) або зчитати з файлу(2): ", end="")
        b = input()
        if b == '1':
            print('\nВведіть ключ')
            key = input()
            if len(key) == 1 and re.match(validator, key):
                key_fie_name = DIR_NAME + FILE_NAME_KEY
                f = open(key_fie_name, 'w')
                f.write(key)
                f.close()
                break
            else:
                print("Ви ввели неправильний ключ")
        elif b == '2':
            key_fie_name = DIR_NAME + FILE_NAME_KEY
            f = open(key_fie_name, 'r')
            key = f.read()
            if len(key) == 1 and re.match(validator, key):
                print('Ключ: ', key)
                break
            else:
                print("Невірний ключ")
        else:
            continue

    key = dict_alph[key]
    new_mess = ''
    for a in message:
        new_mess += copy_alph_list[(dict_alph[a] - key + len_copy_alph) % len_copy_alph] if a != " " else ' '

    print(f'\nРезультат: {new_mess}')
    mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
    f = open(mess_file_name, 'w')
    f.write(new_mess)
    f.close()