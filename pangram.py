text = input("Enter a sentence: ").lower()

alphabet = set("abcdefghijklmnopqrstuvwxyz")

if alphabet.issubset(set(text)):
    print("It is a pangram.")
else:
    print("Not a pangram.")
