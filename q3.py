def update_dictionary(dct, key, value):
    if key in dct:
        print(f"Key '{key}' {dct[key]}")
        dct[key] = value
    else:
        dct[key] = value
    return dct

result1 = update_dictionary({}, "name", "Alice")
print(result1)

result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
