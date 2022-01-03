import extract

pick, symbol, cost, day_change, multiple, mcap = extract.cmcScreen()

a = [pick, symbol, cost, day_change, multiple, mcap]

iter = range(len(pick))

b = []

for i in iter:

    b += [pick[i], symbol[i], cost[i], day_change[i], multiple[i], mcap[i]]

print(b[:n*6])

with open("output.txt", "w") as output:
    output.write(str(b))
