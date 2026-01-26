def is_anagram(a, b):
    a = "".join(sorted(a.replace(" ", "").lower()))
    b = "".join(sorted(b.replace(" ", "").lower()))
    return a == b

# test
word1 = input("Enter a word: ").lower()
word2 = input("Enter another word: ").lower()

print(is_anagram(word1, word2))   # True
