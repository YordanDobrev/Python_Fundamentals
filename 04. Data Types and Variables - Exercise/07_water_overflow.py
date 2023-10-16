#Read User Input
flows = int(input())

#Logic

total_flows = 0

for i in range(flows):
    current_flow = int(input())
    if total_flows + current_flow > 255:
        print("Insufficient capacity!")
        continue
    else:
        total_flows += current_flow

#Print Output

print(total_flows)