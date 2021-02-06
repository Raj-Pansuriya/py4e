"""
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.
"""

largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    try:
        inum=int(snum)
    except:
        if(snum == "done"):
            break
        else:
            print("Invalid input")
    if(largest==None):
        largest=inum
    elif(inum>largest):
        largest=inum
    if(smallest==None):
        smallest=inum
    elif(inum<smallest):
        smallest=inum
    

print("Maximum is",largest)
print("Minimum is",smallest)