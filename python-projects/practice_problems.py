# My solution
print("Twinkle, twinkle, little star,")
print("	How I wonder what you are! ")
print("		Up above the world so high,   		")
print("		Like a diamond in the sky. ")
print("Twinkle, twinkle, little star, ")
print("	How I wonder what you are\n")

# Their solution
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# Find out what version of python I am using
import sys
print("\nPython Version")
print(sys.version)
print("Version Info")
print(sys.version_info,'\n\n')

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# print(factorial(5))


# The following code shows how you would obtain the first, middle and last element of an array with python
str1 = 'James'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2) # This will round up so that will always give us the exact middle number
# Get middle character and add it to result
#res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)