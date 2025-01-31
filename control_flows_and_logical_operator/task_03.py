a = True
b = False
c = True
print(a and b) 
# a and b → True AND False → False
# False because "and" requires both values to be True

print(a or b) 
# a or b → True OR False → True
# True because "or" returns True if at least one value is True

print(not b) 
# not b → NOT False → True
# True because "not" inverts False to True

print((a and c) or b) 
# (a and c) or b → (True AND True) OR False → True OR False → True
# True because "a and c" = True, and "True or False" = True

print(a and (b or c)) 
# a and (b or c) → True AND (False OR True) → True AND True → True
# True because "b or c" = True (since c=True), and "True and True" = True
