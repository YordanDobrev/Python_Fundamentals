# Read User Input
num1 = int(input())
num2 = int(input())

# Logic
num2, num1 = num1, num2

# Print Output
print(f"Before:\n"
      f"a = {num2}\n"
      f"b = {num1}\n"
      f"After:\n"
      f"a = {num1}\n"
      f"b = {num2}\n")
