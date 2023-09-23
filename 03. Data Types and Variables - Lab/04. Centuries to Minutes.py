#Read User Input
century = int(input())

#Logic

years = century * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

#Print Output

print(f"{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")