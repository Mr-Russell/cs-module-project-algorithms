'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # single = None
    # for a in arr:
    #     count = 0
    #     for b in arr:
    #         if a == b:
    #             count += 1
    #             if count > 1:
    #                 break
    #     if count < 2:
    #         single = a

    # return single


    for n in arr:
        if arr.count(n) < 2:
            return n

    # return single   


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")