number = int(input("Write number: "))
if number % 2 == 0:
    print("True")
else:
    print("False")

letters = 'a, e, i, o, u, y'
num = 0
string = input("Write something: ")
for letter in string:
    if letter in letters:
        num += 1
print(num)

number1 = int(input("Write number: "))
factorial = number1
if number1 >= 0:
    for i in range(1, number1):
        factorial = factorial * i
    print(factorial)
else:
    print("Error")


