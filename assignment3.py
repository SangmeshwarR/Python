count1, count2  = 0
isPrime = 1
while True:
    number = int(input("Give a number(-1 to stop): "))
    if number == -1:
        break

    elif number < 2:
        continue

    for i in range(2, number):
        if number % i == 0:
            isPrime = 0
            break
        else:
            isPrime = 1

    if isPrime:
        count1 += 1
    else:
        count2 += 1

print("Prime numbers: ", count1)
print("Composite numbers: ", count2)