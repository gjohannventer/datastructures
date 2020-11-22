def add_one(arr):
    borrow = 1 #initial value

    for i in range(len(arr), 0, -1):
        digit = borrow + arr[i - 1]

        borrow = digit//10

        if borrow == 0:
            arr[i - 1] = digit
            break
        else:
            arr[i - 1] = digit % 10

    # Prepend the final "borrow" to the original array
    arr = [borrow] + arr
    position = 0
    while arr[position] == 0:
        position += 1

    return arr[position:]