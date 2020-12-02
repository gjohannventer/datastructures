def subsets(arr):
    return returned_subsets(arr, 0)

def returned_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = returned_subsets(arr, index + 1)
    
    output = list()

    for element in small_output:
        output.append(element)

    # add current elements to existing subsets and add them to the output
    print('small_output')
    print(small_output)
    for element in small_output:
        current = list()
        print(index)
        print(element)
        print(arr[index])
        current.append(arr[index])
        current.extend(element)
        output.append(current)

    print('output')
    print(output)
    return output


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = subsets(arr)
        
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail") 

arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)