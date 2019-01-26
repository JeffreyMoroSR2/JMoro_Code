# -*- coding: utf-8 -*-
import re
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
        
    while True:
        print("\nВведіть ключ (a-z): ", end = "")
        key = input()
        if len(key) == 1 and  re.match(validator, key):
            break
        else:
            print("Ви ввели неправильний ключ")
    
    key = dict_alph[key]
    new_mess = ''
    for a in message:
        new_mess += copy_alph_list[(dict_alph[a] + key) % len_copy_alph] if a != " " else ' '
               
    print(f'\nРезультат: {new_mess}')


def uncipher():
     while True:
        print("\nВведіть повідомлення для розшифрування: (a-z): ", end = "")
        message = input()
        if re.match(validator, message):
            break
        else:
            print("Ви ввели неправильне повідомлення")
        
     while True:
        print("\nВведіть ключ (a-z): ", end = "")
        key = input()
        if len(key) == 1 and  re.match(validator, key):
            break
        else:
            print("Ви ввели неправильний ключ")
            
     key = dict_alph[key]
     new_mess = ''
     for a in message:
         new_mess += copy_alph_list[(dict_alph[a] - key + len_copy_alph) % len_copy_alph] if a != " " else ' '
               
     print(f'\nРезультат: {new_mess}')

def uncipher_without_key():
    while True:
        print("\nВведіть повідомлення для розшифрування: (a-z): ", end = "")
        message = input()
        if re.match(validator, message):
            break
        else:
            print("Ви ввели неправильне повідомлення")
    new_mess = '' 
    i = 0       
    while i <= 25:
        for a in message:
            new_mess += copy_alph_list[(dict_alph[a] - i + len_copy_alph) % len_copy_alph] if a != " " else ' '
        print(f'\nРезультат при ключі {i}: {new_mess}')
        new_mess = ''
        i += 1
    #print(f'\nРезультат: {new_mess}')
    
print("Програма Шифр Цезаря")
print("====================")
while True:
    print("\nВи бажаєте зашифрувати (1), розшифрувати(2), підібрати ключ(3), вийти(4)?")
    t = input()
    if t == "1":
        cipher()        
    elif t == "2":
         uncipher()
    elif t == "3":
         uncipher_without_key()
    elif t == "4":
         break
    else:
         print("\nВи ввели неправильні дані, спробуйте ще раз")