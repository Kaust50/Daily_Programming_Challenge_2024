def sort_array(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

def is_valid_input(input_list):
    for item in input_list:
        try:
            num = int(item)
            if num < 0 or num > 2:
                return False
        except ValueError:
            return False
    return True

def main():
    while True:
        input_line = input("Enter the elements of the array (0, 1, or 2) in one line, separated by space: ")
        input_list = input_line.split()

        if is_valid_input(input_list):
            arr = list(map(int, input_list))
            sort_array(arr)
            print("Sorted array: ")
            print(" ".join(map(str, arr)))
            break
        else:
            print("Invalid input. Please enter only numbers 0, 1, or 2.")

if __name__ == "__main__":
    main()
