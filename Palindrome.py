# n deines value of inputs
n = int(input())
# list of palindromes
palindromes = []

# for loop to get inputs
for i in range(n):
    # get input
    value = input().lower()
    # reverse value
    reverse = value[::-1].lower()
    # check if value is palindrome
    if value == reverse:
        # add to list
        palindromes.append(value)
        
# print list
print(palindromes)


