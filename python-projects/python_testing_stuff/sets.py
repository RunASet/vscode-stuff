x=set()
s = {4,32,2} # this known as a set literal
s2 = {6,7,34}

empty_set = {}

print('The following are examples:','\n')

print(type({})) # This is the library of the empty set

print(3 in s,'\n')  # returns the boolean value false because there is no 3 in the set

print(s.union(s2),'\n') #  Print the union of the two sets

print(s.difference(s2),'\n')    # Print the difference between the two sets.