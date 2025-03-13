def check_divisibility(num, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be 0")
    return num % divisor == 0

result1 = check_divisibility(10, 2)
print("is 10 divisible by 2: ", result1)

result2 = check_divisibility(7, 3)
print("is 7 divisible by 3: ", result2)