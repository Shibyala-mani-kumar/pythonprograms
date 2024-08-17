numbers_given = input("Enter Numbers: ")
numbers_list = []
number = ""
for each_num in numbers_given:
    if each_num != " ":
        number = number + each_num
    else:
        if each_num == " ":
            numbers_list = numbers_list + [number]
            number = ""
if number != " ":
    numbers_list = numbers_list + [number]
print(numbers_list)