import re

def is_palindrome(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()
    return string == string[::-1]
pala = str(input("donne une phrase :"))
print(is_palindrome(pala))

