
# Data types in python: Numeric(int, long, float, complex), String, List, Tuple, Dictionary.

# Numeric(int, long, float, complex), String:
b, c, d, e, f, j = 10, 12, "Manchester", "United Kingdom", 4.5, 300+3j
print(b, c, d, j)
print("{} {}".format("String is", e))
print(type(b))
print(type(d))
print(type(f))
print(type(j))

# List data types in python:
Values = [1, 3, 4, "Leeds", 7, "London", 15, 13, "University"]
print(Values[0], Values[2], Values[3], Values[-1])
# OR print this way
print(Values[0])
print(Values[2])
print(Values[3])
print(Values[-1])  # print last on list
print(Values[4:6])  # print index 4 to 5

# Inserting value(s) in btw list (insert):
Values.insert(3, "Halifax")
print(Values)

# Adding value at the end of the list (append):
Values.append("Doctorate Degree")
print(Values)

# Updating values in the list
Values[3] = "LEEDS"

# Deleting value from the List
del Values[4]  # Will delete "Leeds"
print(Values)

# Tuple: Immutable (Locked) data that can not be edited.
h = (6, 2, 8, 9, 4)
print(h)
q = ("Ola", 76, "Year of birth", 31, "Sunday")
print(q)
print(q[4])

# Dictionary:
w ={1: "Boris", 2: "Johnson,", "Post": "Brexit Prime Minister"}
print(w[1], w[2], w["Post"])

# Adding new values to Dictionary:
dict1 = {}
dict1["Lastname"] = "Therasa"
dict1["Firstname"] = "May"
dict1["Sex"] = "Female"
dict1["Position"] = "Former Prime Minister"
print(dict1)

dict2 = {}
dict2["Surname"] = "Jeromy"
dict2["Forename"] = "Corbyn"
dict2["Gender"] = "Male"
dict2["Post"] = "Labour Leader"
print(dict2)



