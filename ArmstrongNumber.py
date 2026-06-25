num = int(input("Enter The Number:"))

num_str = str(num)
num = len(num_str)

total_sum = sum(int(digit) ** num for digit in num_str)

if total_sum == int(num_str):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")







