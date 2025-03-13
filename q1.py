def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, ))):
        return -1
    x, y = y, x
    print(f"Swapped values: x = {x}, y = {y}")
    return

result1 = swap(9, 17)