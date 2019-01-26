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
FILE_NAME_MESSAGE = 'modules\Vigener\message.txt'
FILE_NAME_CIPHERTEXT = 'modules\Vigener\cipher_text.txt'
FILE_NAME_KEY = 'modules\Vigener\key.txt'

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
        print("\nВведіть повідомлення для шифрування(1) або Зчитайте з файлу(2): ", end="")
        b = input()
        if b == '1':
            message = input()
            if re.match(validator, message):
                mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
                f = open(mess_file_name, 'w')
                f.write(message)
                f.close()
                break
            else:
                print("Ви ввели неправильне повідомлення")
        elif b == '2':
            mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
            f = open( mess_file_name, 'r')
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
        c = input()
        if c == '1':
            key = input()
            key_fie_name = DIR_NAME + FILE_NAME_KEY
            f = open(key_fie_name, 'w')
            f.write(key)
            f.close()
            break
        elif c == '2':
            key = Generate_Key()
            break
        else:
            continue

    len_key = len(key)
    mess_len = len(message)
    diff = mess_len % len_key
    while diff != 0:
        message = message + " "
        diff = (diff + 1) % len_key
    mess_len = len(message)
    new_len = int(mess_len / len_key)

    new_mess = ''
    b = 0
    while b < new_len:
        a = 0
        while a < len_key:
            aa = message[len_key * b + a]
            kk = key[a]
            iaa = dict_alph[aa] if aa in dict_alph else 0
            ikk = dict_alph[kk]
            new_mess += copy_alph_list[(iaa + ikk) % len_copy_alph] if aa != " " else ' '
            a += 1
        b += 1
    print(f'\nРезультат: {new_mess}')
    cipher_file_name = DIR_NAME + FILE_NAME_CIPHERTEXT
    f = open(cipher_file_name, 'w')
    f.write(new_mess)
    f.close()


def Uncipher():
    while True:
        print("\nВведіть повідомлення для розшифрування(1) або зчитайте з файлу(2): ", end="")
        d = input()
        if d == '1':
            message = input()
            if re.match(validator, message):
                break
            else:
                print("Ви ввели неправильне повідомлення")
        elif d == '2':
            key_fie_name = DIR_NAME + FILE_NAME_KEY
            f = open(key_fie_name, 'r')
            message = f.read()
            if re.match(validator, message):
                print('Текс повідомлення: ', message)
                break
            else:
                print("Ви ввели неправильне повідомлення")
        else:
            continue

    print("\nВведіть ключ (a-z): ", end="")
    key = input()
    len_key = len(key)
    mess_len = len(message)
    diff = mess_len % len_key
    while diff != 0:
        message = message + " "
        diff = (diff + 1) % len_key
    mess_len = len(message)
    new_len = int(mess_len / len_key)


    new_mess = ''
    b = 0
    while b < new_len:
        a = 0
        while a < len_key:
            aa = message[len_key * b + a]
            kk = key[a]
            iaa = dict_alph[aa] if aa in dict_alph else 0
            ikk = dict_alph[kk]
            new_mess += copy_alph_list[((iaa - ikk) + len_copy_alph) % len_copy_alph] if aa != " " else ' '
            a += 1
        b += 1
    print(f'\nРезультат: {new_mess}')
    mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
    f = open(mess_file_name, 'w')
    f.write(new_mess)
    f.close()
