import re
import random
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
FILE_NAME_MESSAGE = 'modules\Vernam\message.txt'
FILE_NAME_CIPHERTEXT = 'modules\Vernam\cipher_text.txt'
FILE_NAME_KEY = 'modules\Vernam\key.txt'

def Generate_Key():
    def random_with_N_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return random.randint(range_start, range_end)

    key = random_with_N_digits(1000)
    str_key = str(key)
    key_fie_name = DIR_NAME + FILE_NAME_KEY
    f = open(key_fie_name, 'w')
    f.write(str_key)
    f.close()
    print('Новий ключ згенеровано :', key)
    return key

def Cipher():
    message = ''
    str_key = ''
    while True:
        print("\nВведіть повідомлення для шифрування(1) або зчитайте з файлу(2): ", end = "")
        b = input()
        if b == '1':
            message = input()
            if re.match(validator, message):
                mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
                f = open(mess_file_name, 'w')
                f.write(message)
                f.close()
            else:
                print("Ви ввели неправильне повідомлення")
                continue
        elif b == '2':
            mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
            f = open(mess_file_name, 'r')
            message = f.read()
            if re.match(validator, message):
                print('Текст повідомлення: ', message)
            else:
                print("Ви ввели неправильне повідомлення")
                continue
        else:
            continue

        key_fie_name = DIR_NAME + FILE_NAME_KEY
        f = open(key_fie_name, 'r')
        key_read = f.read()
        key = key_read[:len(message):]
        str_key = str(key)
        if len(str_key) < len(message):
            print('Згенеруйте новий ключ або введть нове повідомлення: len(str_key) < len(message)')
            continue
        else:
            break

    list_key = list(str_key)
    len_key = len(str_key)
    mess_len = len(message)
    diff = mess_len % len_key
    while diff != 0:
        message = message + " "
        diff = (diff + 1) % len_key
    mess_len = len(message)

    new_mess = ''
    mess_key = ''
    x = 0
    v = 0


    while x < mess_len:
        v = int(list_key[x])
        mess_key += copy_alph_list[v]
        x += 1
    print(f'\nКлюч: {mess_key}')

    a = 0
    while a < mess_len:
        aa = message[a]
        kk = mess_key[a]
        iaa = dict_alph[aa] if aa in dict_alph else 0
        ikk = dict_alph[kk]
        new_mess += copy_alph_list[(iaa + ikk) % len_copy_alph] if aa != " " else ' '
        a += 1

    print(f'\nРезультат: {new_mess}')
    cipher_file_name = DIR_NAME + FILE_NAME_CIPHERTEXT
    f = open(cipher_file_name, 'w')
    f.write(new_mess)
    f.close()

def Uncipher():
    message = ''
    str_key = ''
    while True:
        print("\nВведіть повідомлення для розшифрування(1) або зчитайте з файлу(2): ", end="")
        b = input()
        if b == '1':
            message = input()
            if re.match(validator, message):
                mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
                f = open(mess_file_name, 'w')
                f.write(message)
                f.close()
            else:
                print("Ви ввели неправильне повідомлення")
                continue
        elif b == '2':
            cipher_file_name = DIR_NAME + FILE_NAME_CIPHERTEXT
            f = open(cipher_file_name, 'r')
            message = f.read()
            if re.match(validator, message):
                print('Текст повідомлення: ', message)
            else:
                print("Ви ввели неправильне повідомлення")
                continue
        else:
            continue

        key_fie_name = DIR_NAME + FILE_NAME_KEY
        f = open(key_fie_name, 'r')
        key_read = f.read()
        key = key_read[:len(message):]
        str_key = str(key)
        if len(str_key) < len(message):
            print('Згенеруйте новий ключ або введть нове повідомлення: len(str_key) < len(message)')
            continue
        else:
            break

    list_key = list(str_key)
    len_key = len(str_key)
    mess_len = len(message)
    diff = mess_len % len_key
    while diff != 0:
        message = message + " "
        diff = (diff + 1) % len_key
    mess_len = len(message)

    new_mess = ''
    mess_key = ''
    x = 0
    v = 0

    while x < mess_len:
        v = int(list_key[x])
        mess_key += copy_alph_list[v]
        x += 1
    print(f'\nКлюч: {mess_key}')

    cipher_file_name = DIR_NAME + FILE_NAME_CIPHERTEXT
    f = open(cipher_file_name, 'r')
    new_mess = f.read()
    uncipher_mess = ''
    a = 0
    while a < mess_len:
        aa = new_mess[a]
        kk = mess_key[a]
        iaa = dict_alph[aa] if aa in dict_alph else 0
        ikk = dict_alph[kk]
        uncipher_mess += copy_alph_list[(iaa - ikk) % len_copy_alph] if aa != " " else ' '
        a += 1
    print(f'\nРезультат2: {new_mess}')
    mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
    f = open(mess_file_name, 'w')
    f.write(uncipher_mess)
    f.close()