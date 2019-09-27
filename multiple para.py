#define the function
def format_name(name_input, age_input):
    print("My name is", name_input +", I am", age_input, "years old.")

name1 = input("What is your name?: ")
age1 = input("What is your age?: ")

#Call the function
format_name(name1, age1)