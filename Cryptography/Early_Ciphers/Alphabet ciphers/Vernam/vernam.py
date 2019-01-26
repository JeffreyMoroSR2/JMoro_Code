# -*- coding: utf-8 -*-
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

def cipher(): 
    while True:
        print("\nВведіть повідомлення для шифрування: (a-z): ", end = "")
        message = input()
        if re.match(validator, message):
            break
        else:
            print("Ви ввели неправильне повідомлення")
        
    
    #Генерація ключа 
    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return random.randint(range_start, range_end)

    
    key = random_with_N_digits(len(message))
    str_key = str(key)
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
        new_mess += copy_alph_list[(iaa + ikk) % len_copy_alph]  if aa != " " else ' '
        a += 1
            
    print(f'\nРезультат: {new_mess}')
    
    #Розшифровка
    uncipher_mess = ''
    a = 0
    while a < mess_len: 
        aa = new_mess[a]
        kk = mess_key[a]
        iaa = dict_alph[aa] if aa in dict_alph else 0
        ikk = dict_alph[kk]
        uncipher_mess += copy_alph_list[(iaa - ikk) % len_copy_alph]  if aa != " " else ' '
        a += 1
    print(f'\nРезультат2: {uncipher_mess}')
    



print("Програма Шифр Вернама")
print("====================")
while True:
    print("\nВи бажаєте зашифрувати (1), вийти(2)?")
    t = input()
    if t == "1":
        cipher()
    elif t == "2":
         break
    else:
         print("\nВи ввели неправильні дані, спробуйте ще раз")