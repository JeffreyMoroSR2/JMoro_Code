# -*- coding: utf-8 -*-

import re, random
validator = "^[ a-z]{,}$"

alph = " abcdefghijklmnopqrstuvwxyz"
len_alph =len(alph)
alph_list = list(alph)
random_alph = list(alph) # алфавіт, який змінюється рандомно
random.shuffle(random_alph) # <- алфавіт змінюється рандомно
print(random_alph)
print("\n===============================================")
dict_alph = {}
i = 0
while i < len(alph_list):
    dict_alph[alph_list[i]]=i
    i += 1
    
while True:
    print("\nВведіть повідомлення для шифрування: (a-z): ", end = "")
    message = input()
    if re.match(validator, message):
        break
    else:
        print("Ви ввели неправильне повідомлення")

i = 0
new_mess = ''
while i < len(message):
    new_mess += random_alph[dict_alph[message[i]]]
    i += 1
     
print(f'\nРезультат п1: {new_mess}')


#Part 2
while True:
    print("\nВведіть ключ (a-z): ", end = "")
    key = input()
    if len(key) == 1 and  re.match(validator, key):
        break
    else:
        print("Ви ввели неправильний ключ")
        
key_index = dict_alph[key]
random_alph_copy = []
i = 0
while i < len(random_alph):
    index_new = (i + key_index) % len(random_alph)
    random_alph_copy.append(random_alph[index_new])
    i += 1
print(f'\n\n{random_alph_copy}')

i = 0
new_mess = ''
while i < len(message):
    new_mess += random_alph_copy[dict_alph[message[i]]]
    i += 1
 
print(f'\nРезультат п2: {new_mess}')
    