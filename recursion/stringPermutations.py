def permutations(string):
    return return_permutations(string, 0)

def return_permutations(string, index):
    output = list()

    if index >= len(string):
        return [""]
    small_output = return_permutations(string, index + 1)
   
    current_char = string[index]
    for substring in small_output:
        for index in range(len(small_output[0]) + 1):
            new_substring = substring[0: index] + current_char + substring[index:]
            output.append(new_substring)
    return output


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)
