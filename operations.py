# assign input command to a variable for user to write a value in terminal
var = input("Please enter a value: ")

# to convert a value to a string
print(str(var))

# to convert a string to upper with the uppercase method
print(var.upper())

# use of len in-built function to print the number of characters in var which is 3
print(len(var))

# .isdecimal method to see if there are decimals in base numbers between 0 and 9
# boolean value returns false in terminal because var is a string variable
# boolean value returns true in terminal if value inputted has integers
print(var.isdecimal())




