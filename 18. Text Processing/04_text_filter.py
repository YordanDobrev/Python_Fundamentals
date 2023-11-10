words_to_replace = input().split(", ")
text = input()

for words in words_to_replace:
    while words in text:
        text = text.replace(words, "*" * len(words))

print(text)