comps = ["Resistors","Capacitors"]
new_comps = [None] * (len(comps)+1)
for i in range(len(comps)):
    new_comps[i] = comps[i]
    print(comps[i], "is", i)

n = int(input("Which component would you like "))
print(comps[n])
new_comps[len(comps)] = "LED"
print(new_comps)