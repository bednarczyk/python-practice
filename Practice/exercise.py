from pprint import pprint

sentence = "This is a common interview question"

# Find the most repeated character in the text

# Dictionary
set = {*sentence}
dictionary = {}

for char in set:
    count = sentence.count(char)
    dictionary[char] = count

pprint(dictionary, width=1)

sorted = sorted(dictionary.items(),
                key=lambda kv:kv[1],
                reverse=True)
print(sorted)

