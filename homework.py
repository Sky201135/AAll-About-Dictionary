test_dict = {
    "a": [1, 2, 3, 4],
    "b": [2, 3, 4],
    "c": [4, 5, 6],
    "d": [1, 4]
}

val = 4

freq = sum(sublist.count(val) for sublist in test_dict.values())
print(f"The value {val} appears {freq} times.")