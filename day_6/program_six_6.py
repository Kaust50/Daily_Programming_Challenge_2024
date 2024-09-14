def find_zero_sum_subarrays(arr):
    prefix_sum_map = {}
    prefix_sum = 0
    result = []
    
    prefix_sum_map[0] = [-1]
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum in prefix_sum_map:
            for start_index in prefix_sum_map[prefix_sum]:
                result.append((start_index + 1, i))
                
        if prefix_sum in prefix_sum_map:
            prefix_sum_map[prefix_sum].append(i)
        else:
            prefix_sum_map[prefix_sum] = [i]
    
    return result

# Test cases
print(find_zero_sum_subarrays([1, 2, -3, 3, -1, 2]))        
print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))      
print(find_zero_sum_subarrays([1, 2, 3, 4]))               
print(find_zero_sum_subarrays([0, 0, 0]))                  
print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))
