# -*- coding: utf-8 -*-

import re, random
validator = "^[ a-z]{,}$"

alph = " abcdefghijklmnopqrstuvwxyz"
alph = list(alph)
copy_alph = "abcdefghijklmnopqrstuvwxyz"
len_copy_alph =len(copy_alph)
copy_alph_list = list(copy_alph)
random_alph = list(copy_alph) # алфавіт, який змінюється рандомно
random.shuffle(random_alph) # <- алфавіт змінюється рандомно
random_alph_list = list(random_alph)
print(random_alph)
print("===============================================")
dict_alph = {}
i = 0
while i < len(copy_alph):
    dict_alph[copy_alph[i]]=i
    i += 1
    
dict_rand = {}
a = 0
while a < len(random_alph):
    dict_rand[random_alph[a]]=a
    a += 1

while True:
    print("\nВведіть повідомлення для шифрування: (a-z): ", end = "")
    message = input()
    if re.match(validator, message):
        break
    else:
        print("Ви ввели неправильне повідомлення")

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


#Part 2
while True:
    print("\nВведіть ключ (a-z): ", end = "")
    key = input()
    if len(key) == 1 and  re.match(validator, key):
        break
    else:
        print("Ви ввели неправильний ключ")
        
key = dict_alph[key]
new_mess2 = ''
for a in message:
    new_mess2 += copy_alph_list[(dict_rand[a] - key) % len_copy_alph] if a != " " else ' '
 
new_mess2 = list(new_mess2)              
print(f'\nРезультат п2: {new_mess2}')

'''
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
    new_mess += new_mess2[t]
    i += 1
    
print(f'\nРезультат п3: {new_mess}') 
  '''  
    
    
    