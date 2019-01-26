import re
validator = "^[ a-z]{,}$"

alph = " abcdefghijklmnopqrstuvwxyz"
alph = list(alph)
len_alph =len(alph)

dict_alph = {}
i = 0
while i < len(copy_alph):
    dict_alph[copy_alph[i]]=i
    i += 1


def uncipher_with_key_len():
    while True:
        print("\nВведіть повідомлення для розшифрування: (a-z): ", end = "")
        message = input()
        if re.match(validator, message):
            break
        else:
            print("Ви ввели неправильне повідомлення")


