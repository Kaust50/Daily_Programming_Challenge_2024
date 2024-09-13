def find_leaders(arr):
    n = len(arr)
    if n == 0:
        return []

    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)

    leaders.reverse()
    return leaders

# Test cases
print(find_leaders([16, 17, 4, 3, 5, 2]))  # Output: [17, 5, 2]
print(find_leaders([1, 2, 3, 4, 0]))       # Output: [4, 0]
print(find_leaders([7, 10, 4, 10, 6, 5, 2])) # Output: [10, 6, 5, 2]
print(find_leaders([5]))                   # Output: [5]
print(find_leaders([100, 50, 20, 10]))     # Output: [100, 50, 20, 10]
print(find_leaders(list(range(1, 1000001)))) # Output: [1000000]