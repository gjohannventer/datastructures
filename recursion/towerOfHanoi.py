def tower_of_Hanoi_solution(num_disks, source, auxiliary, destination):

    # Base case
    if num_disks == 0:
        return

    # Termination condition
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return

    # Just think of one iteration, rest the Recursion will take care!

    # Step 1: Move num_disks - 1 from source to auxiliary
    tower_of_Hanoi_solution(num_disks - 1, source, destination, auxiliary)

    # Step 2: Now you are only left with the only largest disk at source
    # Move the only leftover disk frim source to destination

    print("{} {}".format(source, destination))

    # Step 3: move 'num_disks - 1' from auxiliary to destination
    tower_of_Hanoi_solution(num_disks - 1, auxiliary, source, destination)

def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_solution(num_disks, 'S', 'A', 'D')