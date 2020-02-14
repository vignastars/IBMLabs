string=input("enter a string : ")
string = string.casefold() 
rev_string = reversed(string) 
print()
if list(string) == list(rev_string):
    print("the given string is a palindrome")
else:
    print("the given string is not a palindrome")