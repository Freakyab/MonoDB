res = "Aryan"
decode = " "
encode = " "
for character in res:
    x = ord(character)
    encode += chr(x+5)
# for character in res:
    y = ord(character)
    decode += chr(y-5)
print(decode)
..