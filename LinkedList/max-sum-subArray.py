def max_sum_subarray(arr):
    current_sum = arr[0] # current sum denotes the sum of a subarray
    max_sum = arr[0]     # max_sum denotes the maximm value of 'current_sum' ever

    # loop from value at index position 1 till the end of the array
    for element in arr[1:]:
        current_sum = max(current_sum + element, element)
        max_sum = max(current_sum, max_sum)

    return max_sum