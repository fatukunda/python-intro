def digit_sum(number):
    numbers = str(number)
    total = 0
    for number in numbers:
        total += int(number)
    print(total)
    
digit_sum(123)

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

"""Reversing a given string"""
def reverse(text):
    reversed = []
    text_length = len(text)
    while text_length > 0:
        last_char = text[text_length-1]
        reversed.append(last_char)
        text_length -= 1
    return (''.join(reversed))

"""Removing vowels from a given text"""
def anti_vowel(text):
    vowels = ['a', 'e', 'i','o','u', 'A', 'E', 'I', 'O', 'U' ]
    new_word = []
    for char in text:
        if char not in vowels:
             new_word.append(char)
    return ''.join(new_word)
