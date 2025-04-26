num = input("Enter a number: ")
sum =0
for i in range(0, len(num)):
    sum =sum+int(num[i])
print(f"The sum of digits in {num} is {sum}")