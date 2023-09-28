
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def combinations(n,k):
    return ((n)/k*(k))

k = factorial(10)
n = factorial(5)
print(combinations(n,k))
""" 
def pascalTriangle(num):
    # Iterating through rows
    for n in range(0, num):

        # iterating through each value of the row
        for k in range(0, n + 1):
            print(factFormula(n, k),
                  " ", end="")
        print()


#function to find factorial
def findFact(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i*findFact(i-1)

# function for the Combination formula
def factFormula(n, k):
    return int(findFact(n)/(findFact(n-k)*findFact(k)))


# Driver code
num = int(input("Enter the number of rows: "))
pascalTriangle(num)
"""