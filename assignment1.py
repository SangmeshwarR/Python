num = int(input("Give number: "))

n = num%2

if n != 0:
    print("Number is odd.")

else:
    print("Number is even.")

n1 = int(input("Give first number: "))
n2 = int(input("Give second number: "))

print("The numbers are:", n1 , "and" , n2)

n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2

print("Swapped numbers are:", n1 , "and" , n2)
