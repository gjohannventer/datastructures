class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skip_i_delete_j(head, i, j):
    # Edge case - Skip 0 nodes (means delete all nodes)
    if i == 0:
        return None

    # Edge case - Delete 0 Nodes
    if j == 0:
        return head


    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # references
    current = head
    previous = None

    while current:

        # skip (i - 1) nodes
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        # delete j nodes
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node

        # Connect the previous.next to the current
        previous.next = current

    # Loop ends
    return head

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
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)