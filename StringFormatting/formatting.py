# Example with %
fname = "John"
lname = "Jones"
age = 35
print("My name is %s %s and I am %d years old" % (fname, lname, age))
                  





# Example with f strings
myList = [1,2,3]
print(f"I have {len(myList)} items in my list. \nThey are {myList}")

# Example with .format, format numbers into string
print("The {0} of 50 is {1:b}".format("binary", 50))

# Not formatting, but this "prints" a sound
print('\a')
print('\a')
print('\a')

number = 10
line = "|"
number2 = 20
print("This can be useful to make tables")
print("{:<9}{:^9}{:>9}".format(number, line, number2))
print("{:<9}{:^9}{:>9}".format(number2, line, number))