count1  = 0
count2 = 0
while True:
    number = int(input("Give a number: "))
    if number != 1 and number != -1:
        if number % 2 == 0 and number != 2:
            count1 += 1
        else:
            count2 += 1
    if number == -1:
        break

print("Prime numbers: ", count1)
print("Composite numbers: ", count2)
