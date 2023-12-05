name = input()
volume = int(input())
weight = int(input())
sugar = int(input())

energy = (volume * weight) / 100
sugars = (volume * sugar) / 100

print(f"{volume}ml {name}:\n"
      f"{energy:.2f}kcal, {sugars:.2f}g sugars")