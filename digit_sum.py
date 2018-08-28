# def digit_sum(number):
#     numbers = str(number)
#     total = 0
#     for number in numbers:
#         total += int(number)
#     print(total)
    
# digit_sum(123)
""" Calculating factorial of a number"""
def factorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        factorial = 1
        for number in range(1, x+1):
            factorial *= number
        return factorial

