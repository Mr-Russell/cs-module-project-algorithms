'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # zeroes = []
    # for i in range(len(arr)):
    #     if arr[i] == 0:
    #         arr.append(0)
    #         zeroes.insert(0, i)
    # for n in zeroes:
    #     arr.pop(n)
    # return arr

    new_arr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            new_arr.append(0)
        else:
            new_arr.insert(0, arr[i])
    return new_arr


    

print(moving_zeroes([0, 0, 0, 0, 3, 2, 1]))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")