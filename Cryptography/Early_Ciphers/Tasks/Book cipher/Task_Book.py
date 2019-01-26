# -*- coding: utf-8 -*-
from collections import OrderedDict

alph = " abcdefghijklmnopqrstuvwxyz"
len_alph =len(alph)
alph_list = list(alph)

dict_alph = {}
i = 0
while i < len(alph_list):
    dict_alph[alph_list[i]] = i
    i += 1
#print(f'dict_alph = {dict_alph}')

f = open('book.txt')
data = f.read()
f.close()

data = data.lower()
new_arr = []
for i in alph_list:
    a = data.count(i)
    new_arr.append(a)

dict_new_arr = {}
i = 0
while i < len(alph_list):
    dict_new_arr[alph_list[i]] = new_arr[i]
    i += 1
print(f'book_dictionary = {dict_new_arr}')

print('===============')
#Шифротекст

f = open('paragraph.txt')
data2 = f.read()
f.close()

data2 = data2.lower()
key = 3
new_mess = ''
for a in data2:
    if a in alph_list:
        new_mess += alph_list[(dict_alph[a] + key) % len_alph]
    else:
        continue           
#print(f'\n: {new_mess}')

my_file = open("scipher.txt", 'w')
my_file.write(new_mess)
my_file.close()

f = open('scipher.txt')
data3 = f.read()
f.close()


new_arr2 = []
for i in alph_list:
    a = data3.count(i)
    new_arr2.append(a)

dict_new_arr2 = {}
i = 0
while i < len(alph_list):
    dict_new_arr2[alph_list[i]] = new_arr2[i]
    i += 1
print(f'cipher_dictionary = {dict_new_arr2}')
print(" ")
print("=============================")
#Процентовка
for a in dict_new_arr:
    dict_new_arr[a] = int(dict_new_arr[a]) / len(data)
print(f'dict_new_arr = {dict_new_arr}')
print(" ")
for a in dict_new_arr2:
    dict_new_arr2[a] = int(dict_new_arr2[a]) / len(data2)
print(f'dict_new_arr2 = {dict_new_arr2}')
print(" ")
#Сортування 
#br = sorted(dict_new_arr2.items(), key=lambda x:x[1])
sorted_dict = OrderedDict(sorted(dict_new_arr.items(), key=lambda x: -x[1]))
sorted_dict2 = OrderedDict(sorted(dict_new_arr2.items(), key=lambda x: -x[1]))

print(sorted_dict) # з книги
print(sorted_dict2) # з шифротексту
    
sorted_arr = list(sorted_dict.keys())
sorted_arr2 = list(sorted_dict2.keys())

print(sorted_arr)
print(sorted_arr2)
#Розшифровка

dict_sorted = {}
i = 0
while i < len(alph_list):
    dict_sorted[sorted_arr2[i]] = i
    i += 1
print(dict_sorted)

new_mess = ''
key = 0
for a in data3:
    if a in sorted_arr:
        new_mess += sorted_arr[(dict_sorted[a] + key)]
    else:
        continue
print(f'\n: {new_mess}')
my_file2 = open("unscipher.txt", 'w')
my_file2.write(new_mess)
my_file2.close()