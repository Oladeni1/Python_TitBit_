
be = 4
while be > 1:
    print(be)
    be = be -1
print("**********I am out of the greater than while loop*************")

be = 4
while be > 1:
    if be != 3:
        print(be)
    be = be - 1
print("**********I am out of the not equal to while loop*************")

be = 4
while be > 1:
    if be == 3:
        break
    print(be)
    be = be - 1
print("**********I am out of the equal to break  while loop*************")


be = 10
while be > 1:
    if be == 9:
        be = be - 1
        continue
    if be == 3:
        break
    print(be)
    be = be - 1
print("**********I am out of the continue/ break  while loop, 9 will be excluded*************")