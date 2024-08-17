given_number = int(input("Enter a Number: "))
convert_to_string = str(given_number)
length = len(convert_to_string)
sum = 0
for i in convert_to_string:
    value = int(i) ** length 
    sum = sum + value
if sum == given_number:
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")
