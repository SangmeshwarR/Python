num = int(input("Give number: "))

if num == 0:
    print("1")

elif num != 1:
    for i in range(1, num):
        num *= i
    num -= 1
    
num += 1

print(num)