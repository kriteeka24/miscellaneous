text = input("Enter a sentence: ").lower().split()

duplicates = set()
seen = set()

for word in text:
    if word in seen:
        duplicates.add(word)
    else:
        seen.add(word)

if duplicates:
    print("Duplicate words found:", ", ".join(duplicates))
else:
    print("No duplicate words found")
