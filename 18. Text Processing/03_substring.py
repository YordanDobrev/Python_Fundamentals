word_to_search = input()
text = input()

while word_to_search in text:
    text = text.replace(word_to_search,"")

print(text)