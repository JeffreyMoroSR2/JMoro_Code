# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:22:54 2018

@author: JMoro
"""

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
        
    
    print("\nВведіть ключ (a-z): ", end = "")
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
            new_mess += copy_alph_list[(iaa + ikk) % len_copy_alph] if aa != " " else ' ' 
            a += 1
        b += 1
    print(f'\nРезультат: {new_mess}')

def uncipher():
     while True:
        print("\nВведіть повідомлення для розшифрування: (a-z): ", end = "")
        message = input()
        if re.match(validator, message):
            break
        else:
            print("Ви ввели неправильне повідомлення")
        
    
     print("\nВведіть ключ (a-z): ", end = "")
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
'''
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
 '''   
print("Програма Шифр Віженера")
print("====================")
while True:
    print("\nВи бажаєте зашифрувати (1), розшифрувати(2), підібрати ключ(3), вийти(4)?")
    t = input()
    if t == "1":
        cipher()        
    elif t == "2":
         uncipher()
    #elif t == "3":
         #uncipher_without_key()
    elif t == "4":
         break
    else:
         print("\nВи ввели неправильні дані, спробуйте ще раз")