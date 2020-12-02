from queue import Queue



class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def convert_arr_to_binary_tree(arr):
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]

def diameter_of_binary_tree_func(root):
    if root is None:
        return 0, 0

    left_height, left diameter = diameter_of_binary_tree_func(root.left)
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)

    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

return current_height, current_diameter