def cal_factorial(num: int):
    if num == 0 or num == 1:
        return 1
    return num * cal_factorial(num - 1)

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {cal_factorial(number)}")