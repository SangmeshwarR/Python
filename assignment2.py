num = int(input("Give number: "))
fact = 1
if num < 2:
    print("1")

else:
    for i in range(1, num+1):
        fact *= i
    
print(f"The factorial of {num} is {fact}")