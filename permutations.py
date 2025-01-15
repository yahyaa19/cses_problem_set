# A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose difference is 1.
# Given n, construct a beautiful permutation if such a permutation exists.
# Input
# The only input line contains an integer n.
# Output
# Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
# Constraints

# 1 \le n \le 10^6

# Example 1
# Input:
# 5

# Output:
# 4 2 5 3 1
# Example 2
# Input:
# 3

# Output:
# NO SOLUTION

# 1 to N permutations
# 5
# 3 1 5 2 4
# 4 2 5 3 1
# 4 2 5 1 3

# 3 1 4 2


def beautiful_permutation(n):
    if n == 1:
        print(1)
    elif n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        evens = [i for i in range(2, n + 1, 2)]
        odds = [i for i in range(1, n + 1, 2)]
        
        # The * operator in the context of print(*evens, *odds) is used to unpack the lists evens and odds. 
        # This means that each element of the lists will be passed as a separate argument to the print function.
        print(*evens, *odds)

if __name__ == '__main__':
    n = int(input())
    beautiful_permutation(n)


