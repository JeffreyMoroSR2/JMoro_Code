# -*- coding: utf-8 -*-

alph = " abcdefghijklmnopqrstuvwxyz"
alph = list(alph)
copy_alph = "abcdefghijklmnopqrstuvwxyz"

def cipher(): 
    while True:
        print("Введіть повідомлення для шифрування: (a-z)")
        message = input()
        flag = False
        lan = 0
        mess = list(message)
        zero = 0
        for i in mess:
            if i in alph: 
                lan +=  1
                if lan == len(mess):
                    flag = True
                    break
            else:
                print("Ваше повідомлення має некоректні символи")
                break
            
        if flag == True:
            break
        
    while True:
        print("Введіть ключ (a-z):")
        key = input()
        if key in alph and key != " ":
            break
        else:
            print("Ви ввели неправильний ключ")
    new_mess = []
    #ind = len(alph)
    ind1 =len(copy_alph)
    index = 0
    for i in copy_alph:
        if key == i:
            key = alph.index(i) - 1

    for a in mess:
        if a in alph:
            if a != " ":
                index = (alph.index(a) + key) % ind1
                if index == 0:
                    index = 26
                    new_mess.append(index)
                else:
                    new_mess.append(index)
            else:
                new_mess.append(zero)
            
    for x in new_mess:
        print(alph[x], end = "")
    input()

def uncipher():
    while True:
        print("Введіть повідомлення для розшифрування: (a-z)")
        message = input()
        flag = False
        lan = 0
        mess = list(message)
        zero = 0
        for i in mess:
            if i in alph: 
                lan +=  1
                if lan == len(mess):
                    flag = True
                    break
            else:
                print("Ваше повідомлення має некоректні символи")
                break
            
            if flag == True:
                break
        while True:
            print("Введіть ключ (a-z):")
            key = input()
            if key in alph and key != " ":
                break
            else:
                print("Ви ввели неправильний ключ")
                
        new_mess = []
        
        ind1 =len(copy_alph)
        index = 0
        for i in copy_alph:
            if key == i:
                key = alph.index(i) - 1
        
        for i in alph:
           if key == i:
                alph.index(i)
        for a in mess:
            if a in alph:
                if a != " ":
                    index = (alph.index(a) - key + ind1) % ind1
                    if index == 0:
                        index = 26
                        new_mess.append(index)
                    else:
                        new_mess.append(index)
                else:
                    new_mess.append(zero)
                    
    
        for x in new_mess:
            print(alph[x], end = "")
        input()
        break

print("Програма Шифр Цезаря")
print("====================")
while True:
    print("Ви бажаєте зашифрувати чи розшифрувати?(1/2)")
    t = input()
    if t == "1":
        cipher()
        break
    elif t == "2":
         uncipher()
         break
    else:
         print("Ви ввели неправильні дані, спробуйте ще раз")


'''
 if (alph.index(a) + key) >= ind:
                #ind -= index
                index = (alph.index(a) + key) - ind
                new_mess.append(index)
                #ind = 0
            else:
                new_mess.append(alph.index(a) + key)
                #ind = 0
'''