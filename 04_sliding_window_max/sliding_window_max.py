'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_list = []
    for i in range(len(nums) - (k - 1)):
        arr = nums[i:(i+k)]
        max_val = nums[i]
        for n in arr:
            if n > max_val:
                max_val = n
        max_list.append(max_val)

    return max_list

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
