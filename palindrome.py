text = input("Enter a word or phrase: ").lower().replace(" ", "")

if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("Not a palindrome.")
