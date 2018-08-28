# def digit_sum(number):
#     numbers = str(number)
#     total = 0
#     for number in numbers:
#         total += int(number)
#     print(total)
    
# digit_sum(123)

""" Calculating factorial of a number"""
# def factorial(x):
#     if x == 1:
#         return 1
#     elif x == 0:
#         return 0
#     else:
#         factorial = 1
#         for number in range(1, x+1):
#             factorial *= number
#         return factorial


""" Testing if a given number is a prime number"""
def is_prime(x):
    if x<2:
        return False
    else:
         for n in range(2, x-1 ):
            if x % n == 0:
                return False
            else:
                return True

