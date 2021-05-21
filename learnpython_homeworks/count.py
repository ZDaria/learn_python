from collections import Counter

phones = ["iPhone", "Samsung", "LG", "LG"]

count = Counter(phones)

print(count)
print(count["LG"])
print(count["Test"])

text = "Vincent Malloy is seven years old " \
       "He's polite and always does as he's told " \
       "For a boy his age, he's considerate and nice " \
       "But he want's to be just like Vincent Price"
count = Counter(text.lower().replace(" ", ""))
print(count)
