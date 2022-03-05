from collections import Counter

print("Enter the name of the string ")
str = input()

a = Counter(str)

print("Count of characters in", str , "is :\n ", a)
