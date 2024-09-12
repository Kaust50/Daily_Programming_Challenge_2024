import math

def next_gap(gap):
    if gap <= 1:
        return 0
    return math.ceil(gap / 2)

def merge(arr1, arr2, m, n):
    gap = next_gap(m + n)

    while gap > 0:
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        j = max(0, gap - m)
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        if j < n:
            j = 0
            while j + gap < n:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        gap = next_gap(gap)

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merge(arr1, arr2, len(arr1), len(arr2))
print("Test case 1 - arr1:", arr1, "arr2:", arr2)

arr1 = [10, 12, 14]
arr2 = [1, 3, 5]
merge(arr1, arr2, len(arr1), len(arr2))
print("Test case 2 - arr1:", arr1, "arr2:", arr2)

arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
merge(arr1, arr2, len(arr1), len(arr2))
print("Test case 3 - arr1:", arr1, "arr2:", arr2)

arr1 = [1]
arr2 = [2]
merge(arr1, arr2, len(arr1), len(arr2))
print("Test case 4 - arr1:", arr1, "arr2:", arr2)

arr1 = list(range(1, 50001))
arr2 = list(range(50001, 100001))
merge(arr1, arr2, len(arr1), len(arr2))
print("Test case 5 - arr1:", arr1[:5], "...", arr1[-5:], "arr2:", arr2[:5], "...", arr2[-5:])
