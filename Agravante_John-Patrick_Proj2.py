"""
Name: John Patrick Agravante
Section: BSCS Block B
Exam/Project Title: Think It. Code It. Prove It.
Algorithm: Personal Analyzer
"""
"""
Datasets: Prices of my Parcels from shopee
367 167 166 327 49 39 65 59 379 148 43 299 264 38 68
"""

# -------- SEARCH IMPLEMENTATIONS --------

# Sequential Search
# This checks each value one by one from the start until it finds the target
def sequentialSearch(arr, target):
    print("\n--- SEQUENTIAL SEARCH ---")
    steps = 0  # counts how many checks we did

    for i in range(len(arr)):
        steps += 1  # increase step every time we check a value
        print(f"Checking index {i}: {arr[i]}", end=" ")

        if arr[i] == target:
            print("→ FOUND!")
            return steps  # stop immediately if found
        else:
            print("→ no match")

    print("Target not found")
    return steps  # return total steps even if not found


# Binary Search
# This only works properly on sorted data, so we sort first
# Then we repeatedly divide the search space in half
def binarySearch(arr, target):
    print("\n--- BINARY SEARCH ---")
    
    sorted_arr = arr.copy()  # copy first so original list is not changed
    sorted_arr.sort()        # sort the list
    print(f"Sorted: {sorted_arr}")

    lower = 0
    upper = len(sorted_arr) - 1
    steps = 0  # count how many times we loop

    while lower <= upper:
        steps += 1
        mid = (lower + upper) // 2  # get the middle index

        print(
            f"L={lower}, R={upper}, Mid={mid}, Value={sorted_arr[mid]}",
            end=" "
        )

        if sorted_arr[mid] == target:
            print("→ FOUND!")
            return steps
        elif sorted_arr[mid] < target:
            print("→ go right")
            lower = mid + 1  # ignore left half
        else:
            print("→ go left")
            upper = mid - 1  # ignore right half

    print("Target not found")
    return steps


# Recursive Search
# This works like sequential search but uses function calls instead of loops
def recursiveSearch(arr, target, i=0):
    
    # Only print title once at the start
    if i == 0:
        print("\n--- RECURSIVE SEARCH ---")

    print(f"recursiveSearch(index={i})")

    # Base case: if index goes beyond list, stop
    if i >= len(arr):
        print("→ base case → not found")
        return 0

    print(f"Checking value: {arr[i]}")

    # If found, return 1 step
    if arr[i] == target:
        print("FOUND!")
        return 1
    else:
        # If not found, call the function again for next index
        steps = 1 + recursiveSearch(arr, target, i + 1)
        print(f"returns step count = {steps}")
        return steps


# This just explains the idea and time complexity after running each algorithm
def show_analysis(choice):
    if choice == 1:
        print("\nBase Idea: Check each element one by one")
        print("Big O: O(n)")

    elif choice == 2:
        print("\nBase Idea: Divide the list in half each step")
        print("Big O: O(log n)")

    elif choice == 3:
        print("\nBase Idea: Same as sequential but uses recursion")
        print("Big O: O(n)")


# -------- USER INTERFACE --------

menu = """
- - - - - Algorithm Analyzer - - - - -
   Pick an Option:
    [1]. Run All Searches
    [2]. Exit
"""

choice = 0

# Loop keeps running until user chooses exit
while choice != 2:
    if choice >= 3:
        print("Invalid Options")

    print(menu)

    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Not a Number")

    if choice == 1:
        try:
            # Get list of numbers from user
            raw_input = input("Enter Numbers: ")
            arr = list(map(int, raw_input.split()))

            # Get target value to search
            target = int(input("Enter Target: ")) 

            # Run all search algorithms and print results
            print(f"\n\nAnswer (Sequential): Steps = {sequentialSearch(arr, target)}")
            show_analysis(1)

            print(f"\nAnswer (Binary): Steps = {binarySearch(arr, target)}")
            show_analysis(2)

            print(f"\nAnswer (Recursive): Steps = {recursiveSearch(arr, target)}")
            show_analysis(3)

        except ValueError:
            print("Not a Number")

# End message
print("\nThank You for using this Program!")