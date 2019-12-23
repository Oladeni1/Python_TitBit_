
str = "RahulShettyAcademy.com"

str2 = "Global Management"

str3 = "Global"

print(str[5])  # S

print(str[0:5])  # Rahul

print(str + str2)  # Concatenation of 2 strings in python (merge)

print(str3 in str2)  # Check if str3 is present in str2 -> return True

var = str.split(".")  # Split "RahulShettyAcademy.com" & print the index 1 of the split
print(var)
print(var[1])

var2 = str2.split(" ")  # Split "Global Management" & print the index 0 of the split
print(var2)
print(var2[0])

# Closing space in a string value
str4 = " Selenium "
var4 = str4.rstrip()  # Right strip
print(var4)

var5 = str4.lstrip()  # Left strip
print(var5)

var6 = str4.strip()  # Strip gaps from both sides of the string
print(var6)
