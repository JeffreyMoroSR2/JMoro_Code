# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:22:57 2018

@author: JMoro
"""
alph = " abcdefghijklmnopqrstuvwxyz"
len_alph =len(alph)
alph_list = list(alph)

dict_alph = {}
i = 0
while i < len(alph_list):
    dict_alph[alph_list[i]] = 0
    i += 1
print(f'dict_alph = {dict_alph}')

knuga = 'fkefwenfffpww;efs,wefnwew'
print(knuga[0])
i = 0
while i < len(knuga):
    if knuga[i] not in dict_alph:
        i += 1
        continue
    dict_alph[knuga[i]] += 1
    i += 1
print(f'dict_alph = {dict_alph}')
    
for a in dict_alph:
    dict_alph[a] = int(dict_alph[a]) / len(knuga)
print(f'dict_alph = {dict_alph}')