# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.


# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron's birth month

#  Two children 
def birthday(s, d, m):
    # Write your code here
    numberDiveded = 0
    numberIteration = len(s)-(m-1)
    if(numberIteration == 0):
        numberIteration = 1
    for k in range(0, numberIteration):
        newArray = s[k:k+m]
        sumArray = sum(newArray)
        if sumArray == d:
            numberDiveded += 1
    return numberDiveded

s = '2 5 1 3 4 4 3 5 1 1 2 1 4 1 3 3 4 2 1'
caracteres = '18 7'
array = list(map(int, s.split()))
caracteresList = list(map(int, caracteres.split()))

print(birthday(array, caracteresList[0], caracteresList[1]))
