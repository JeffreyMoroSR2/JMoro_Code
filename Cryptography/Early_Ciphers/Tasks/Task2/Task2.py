# -*- coding: utf-8 -*-

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


while True:
        print("\nВведіть повідомлення для шифрування: (a-z): ", end = "")
        message = input()
        if re.match(validator, message):
            break
        else:
            print("Ви ввели неправильне повідомлення")


key = 'abcde'
len_key = len(key)
mess_len = len(message)
diff = mess_len % len_key
while diff != 0:
    message = message + " "
    diff = (diff + 1) % len_key
mess_len = len(message)
new_len = int(mess_len / len_key)

new_mess = ''
final_mess = list('')
b = 0
while b < new_len:
    a = 0
    new_mess = ''
    while a < len_key:
        aa = message[len_key * b + a]  
        iaa = dict_alph[aa] if aa in dict_alph else 0
        new_mess += alph_list[iaa]       
        a+=1
    new_mess = list(new_mess)
    random.shuffle(new_mess)
    final_mess.append(new_mess)
    b += 1

print(f'\nРезультат: {final_mess}')