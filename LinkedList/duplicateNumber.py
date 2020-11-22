def duplicate_number(arr):
    current_sum = 0
    expected_sum = 0
    # Traverse original array in the forward direction
    for num in arr:
        current_sum += num

    for i in range(len(arr) - 1): # the last value is non exlusive meaning it does not include the last index
        expected_sum += i

    # The difference between the
    return current_sum - expected_sum

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)