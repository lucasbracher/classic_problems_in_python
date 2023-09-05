# Two ways of swapping values between variables without a third variable

# First one, using arithmetic:
def swap_numbers(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a, b

# Second one, using xor operator:
def swap_numbers_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

