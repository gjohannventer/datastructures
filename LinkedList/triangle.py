def nth_row_pascal(n):
    if n == 0:
        return [1]

    current_row = [1]

    for i in range(1, n + 1): # i is the row number
        # Set the 'current_row' from previous iteration as the `previous_row`
        print("i: {}".format(i))
        previous_row = current_row
        current_row = [1] # start

        for j in range(1, i): # first iteration will never happen
            print("previous_row: {}".format(previous_row))
            print("j: {}".format(j))
            next_number = previous_row[j] + previous_row[j - 1]
            print("next_number: {}".format(next_number))
            current_row.append(next_number)
            print("current_row in for loop: {}".format(current_row))

        current_row.append(1) # finish
        print("current_row: {}".format(current_row))
    return current_row

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)
