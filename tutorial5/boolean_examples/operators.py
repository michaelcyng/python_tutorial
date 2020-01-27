# Not operator
a = True
print("a = {0}".format(a))
print("not a = {0}".format(not a))
print()

# And operator
a = True
b = True
print('True and True = {0}'.format(a and b))  # True
a = True
b = False
print('True and False = {0}'.format(a and b))  # False
a = False
b = True
print('False and True = {0}'.format(a and b))  # False
a = False
b = False
print('False and False = {0}'.format(a and b))  # False
print()

# Or operator
a = True
b = True
print('True or True = {0}'.format(a or b))  # True
a = True
b = False
print('True or False = {0}'.format(a or b))  # True
a = False
b = True
print('False or True = {0}'.format(a or b))  # True
a = False
b = False
print('False or False = {0}'.format(a or b))  # False
print()
