#Convert char to integer
given_string = "123YUM2"
only_integers = ""
characters = ""
for each_digit in given_string:
    value = ord(each_digit)
    if value >= 47 and value <= 58:
        only_integers = only_integers + each_digit
    else:
        characters = characters + each_digit
print(int(only_integers))
print(characters)

    