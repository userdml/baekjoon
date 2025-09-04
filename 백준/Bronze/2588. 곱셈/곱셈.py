num1 = int(input())
num2 = int(input())

# num1 : 472
# num2 : 385

print(f"{num1 * (num2 % 10)}")
print(f"{num1 * (num2 % 100 // 10)}")
print(f"{num1 * (num2 // 100)}")
print(f"{num1 * num2}")