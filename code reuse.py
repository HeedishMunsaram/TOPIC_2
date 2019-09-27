def add_numbers():
    num1 = input("Enter a number: ")
    num2 = input("Enter a second number: ")
    num3 = int(num1) + int(num2)
    return num3

print("Welcome to the Magic!")
num4 = add_numbers()
num5 = add_numbers()
print(num4 + num5)