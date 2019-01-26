text = 'Привет как дилад кк погодадп азазад preved medveodm h 5'
text += ' '
new_text = ''
newer = ''
for a in text:
    if a != " ":
        new_text += a
    else:
        if new_text[0] != new_text[-1]:
            newer += new_text
            newer += ' '

        new_text = ''
print(newer)

