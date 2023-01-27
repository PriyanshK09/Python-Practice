# input a list items seperated by space
lst = input("Enter the list items : ").split()

dictionary = {}
div2 = 0
div3 = 0
div5 = 0
# checking if the elements in list are divisible by 2,3 and 5 and storing multiples in dicionary
for i in lst:
    if int(i)%2==0:
        div2+=1
    if int(i)%3==0:
        div3+=1
    if int(i)%5==0:
        div5+=1

dictionary["2"] = div2
dictionary["3"] = div3
dictionary["5"] = div5

# printing the dictionary
print(dictionary)