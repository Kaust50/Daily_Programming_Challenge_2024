def find_missing_number(arr, n):
    xor_full = 0
    for i in range(1, n + 1):
        xor_full ^= i
    
    xor_arr = 0
    for num in arr:
        xor_arr ^= num
    
    missing_number = xor_full ^ xor_arr
    
    return missing_number

# Test cases
test_cases = [
    ([1, 2, 4, 5], 5),
    ([2, 3, 4, 5], 5),
    ([1, 2, 3, 4], 5),
    ([1], 2),
    (list(range(1, 1000000)), 1000000)
]

for arr, n in test_cases:
    print(f"Array: {arr[:10]}...  n={n} => Missing Number: {find_missing_number(arr, n)}")
