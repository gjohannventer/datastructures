def deep_reverse(arr):
    if len(arr) < 1:
        return arr

    reversed_items = []
    for item in arr[::-1]:
        if type(item) is list:
            item = deep_reverse(item)

        # append the item to the final list
        reversed_items.append(item)

    return reversed_items