import re
import random
validator = "^[ a-z]{,}$"

alph = " abcdefghijklmnopqrstuvwxyz"
alph = list(alph)
len_alph = len(alph)
alph_list = list(alph)
dict_alph = {}
i = 0
while i < len(alph):
    dict_alph[alph[i]]=i
    i += 1

DIR_NAME = ''
FILE_NAME_MESSAGE = 'modules\Substituting\message.txt'
FILE_NAME_CIPHERTEXT = 'modules\Substituting\cipher_text.txt'
FILE_NAME_KEY = 'modules\Substituting\key.txt'

def Generate_Key():
    print("Введіть максимальне значення довжини ключа: ")
    key = input()
    key = int(key)
    key = random.randint(1, key)
    print("Ключ = ", key)
    cipher_file_name = DIR_NAME + FILE_NAME_CIPHERTEXT
    f = open(cipher_file_name, 'w')
    f.write(str(key))
    f.close()
    return key

def Cipher():
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

    while True:
        print("\nВведіть довжину ключа(1) або згенеруйте автоматично(2): ", end="")
        c = input()
        if c == '1':
            key = int(input())
            break
        elif c == '2':
            key = Generate_Key()
            break
        else:
            continue
    i = 1
    key_mess = []
    while i <= key:
        key_mess.append(i)
        if i == key:
            random.shuffle(key_mess)
        i += 1
    print(f'key = {key_mess}')

    new_key_mess = []
    i = 1
    while i <= key:
        index = key_mess.index(i)
        new_key_mess.append(index+1)
        i += 1
    print(f'key_ob = {new_key_mess}')

#***********************
    mess_len = len(message)
    diff = mess_len % key
    while diff != 0:
        message = message + " "
        diff = (diff + 1) % key
    mess_len = len(message)
    new_len = int(mess_len / key)

    new_mess = ''
    b = 0
    while b < new_len:
        mes = message[key*b:key*b+key:1]
        a=0
        while a < key:
            new_mess = new_mess + mes[key_mess[a]-1]
            a += 1
        b += 1

    print(f'\nРезультат: {new_mess}, \nДовжина ключа: {key}, \nКлюч: {key_mess}')
    cipher_file_name = DIR_NAME + FILE_NAME_CIPHERTEXT
    f = open(cipher_file_name, 'w')
    f.write(new_mess)
    f.close()




#Розшифровка
    new_len_mess = ''
    b = 0
    while b < new_len:
        mes = new_mess[key*b:key*b+key:1]
        a=0
        while a < key:
            new_len_mess = new_len_mess + mes[new_key_mess[a]-1]
            a += 1
        b += 1

    print(f'\nРезультат2: {new_len_mess}, \nДовжина ключа: {key}, \nКлюч2: {key_mess}')
    mess_file_name = DIR_NAME + FILE_NAME_MESSAGE
    f = open(mess_file_name, 'w')
    f.write(new_len_mess)
    f.close()

def Uncipher():
    pass