
def swap_nodes(head, position_one, position_two):
    # if both indices are the same
    if position_one == position_two:
        return head

    one_previous = None
    one_current = None

    two_previous = None
    two_current = None

    current_index = 0
    current_node = head
    new_head = None

    while current_node is not None:
        if current_index == position_one:
            one_current = current_node

        elif current_index == position_two:
            two_current = current_node
            break

        if one_current is None:
            one_previous = current_node

        two_previous = current_node

        current_node = current_node.next
        current_index += 1

    # Loop ends

    # Swapping logic
    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp
    if one_previous is None:
        new_head = two_current
    else:
        one_previous.next = two_current
        new_head = head

    return new_head
            

def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]
    
    left_node = None
    right_node = None
    
    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)