"""
Name: John Patrick Agravante
Section: BSCS Block B
Exam/Project Title: Think It. Code It. Prove It.
Algorithm: Recursive Showcase
"""

"""
Dataset: digits of birth year, month, day of friends and family
In any combination: 2 6 5 3 0 8 7 1 9
"""

#Recursion Implementations

# This function calculates factorial using recursion.
# It keeps calling itself until it reaches 0, which is the stopping point.
# Then it multiplies the numbers as it returns back.
def factorial(n, level=0):
    print("\t" * level + f"factorial({n})")
    
    if n == 0:
        print("\t" * level + "→ base case → returns 1")
        return 1
    else:
        result = n * factorial(n - 1, level+1)
        print("\t" * level + f"returns {n}×{result//n} = {result}")
        return result
        

# This function generates Fibonacci numbers using recursion.
# Each number is the sum of the two previous numbers.
# It splits into smaller calls, which is why it becomes slow for large inputs.
"""
OLD CODE:
def fibonacci(n, level=0):
    print("\t" * level + f"fibonacci({n})")
    
    if n <= 1:
        print("\t" * level + "→ base case → returns 1")
        return 1
    else:
        left = fibonacci(n - 1, level+1)
        right = fibonacci(n - 2, level+1)
        result = left + right
        print("\t" * level + f"returns {left} + {right} = {result}")
        return result
"""

#Fibonacci with Memoization
def fibonacci(n, memo=None, level=0):
    # Initialize memo dictionary for storing computed values (memoization)
    if memo is None:
        memo = {}

    # If value is already computed, return it immediately
    if n in memo:
        return memo[n]

    print("\t" * level + f"fibonacci({n})")

    if n <= 1:
        print("\t" * level + "→ base case → returns 1")
        return 1

    else:
        left = fibonacci(n - 1, memo, level + 1)
        right = fibonacci(n - 2, memo, level + 1)

        # Store computed result to avoid recomputation later
        memo[n] = left + right

        # Show how the result is built from smaller values
        print("\t" * level + f"returns {left} + {right} = {memo[n]}")
        return memo[n]


# This function counts total handshakes in a group of people.
# Each person shakes hands with everyone before them.
# It adds up all possible combinations using recursion.
def handshakeRecursion(n, level=0):
    print("\t" * level + f"handshakeRecursion({n})")
    
    if n <= 1:
        print("\t" * level + "→ base case → returns 0")
        return 0
    else:
        result = handshakeRecursion(n-1, level+1) + (n-1)
        print("\t" * level + f"returns f({n-1}) + {n-1} = {result}")
        return result

# This function counts the number of digits in a number.
# It removes the last digit each time using floor division (// 10).
# It repeats until only one digit is left.
def digitCounter(n, level=0):
    print("\t" * level + f"digitCounter({n})")
    
    if n < 10:
        print("\t" * level + "→ base case → returns 1")
        return 1
    else:
        result = 1 + digitCounter(n // 10, level+1)
        print("\t" * level + f"returns 1 + digits({n//10}) = {result}")
        return result


# This part explains how each recursion problem works.
# It shows the base case, recursive formula, and time complexity based on the users choice.
def show_analysis(choice):
    if choice == 1:
        print("\nBase Case: n = 0 → return 1")
        print("Recursive Case: n! = n × (n-1)!")
        print("Big O: O(n)")

    elif choice == 2:
        print("\nBase Case: n <= 1 → return n")
        print("Recursive Case: fib(n) = fib(n-1) + fib(n-2)")
        print("Big O: O(2ⁿ)")

    elif choice == 3:
        print("\nBase Case: n <= 1 → return 0")
        print("Recursive Case: f(n) = f(n-1) + (n-1)")
        print("Big O: O(n)")

    elif choice == 4:
        print("\nBase Case: n < 10 → return 1")
        print("Recursive Case: digits(n) = 1 + digits(n//10)")
        print("Big O: O(d) where d = number of digits")        
        
#Interface
menu = """
- - - - - Recursive Problem Showcase - - - - -
   Pick a Recursion Problem:
    [1]. Factorial
    [2]. Fibonacci 
    [3]. Handshake Recursion 
    [4]. Digit Counter
    [5]. Exit
"""          
choice = 0

#Main loop
while choice != 5:
    print(menu)
    try:
          choice = int(input("Enter Choice: "))
    except ValueError:
          print("Not a Number")

    if choice == 1:
        try:
            num = int(input("Enter a Number: "))
            if num < 0:
                print("ERROR: Factorial undefined for negative numbers")
            else:    
                print(f"\n\nAnswer: {factorial(num)}" )
                show_analysis(1)
        except ValueError:
            print("Not a Number")
            
    elif choice == 2:
        while True:
            try:
                num = int(input("Enter a Number: "))
                if num < 0:
                    print("ERROR: Fibonacci position cannot be negative.")
                    break   
                
                if num > 30:
                    print("WARNING: O(2ⁿ) — this may take very long.")
                    answer = input("Proceed? (y/n): ").strip().lower()
                    if answer != "y":
                        print("Calculation cancelled.")
                        break  
                
                print(f"\nAnswer: {fibonacci(num)}")
                show_analysis(2)
                break  
                
            except ValueError:
                print("Not a Number. Please try again.")
    
    elif choice == 3:
        try:
            num = int(input("Enter a Number: "))
            print(f"\nAnswer: {handshakeRecursion(num)}")
            show_analysis(3)
        except ValueError:
            print("Not a Number")
    
    elif choice == 4:
        try:
            num = int(input("Enter a Number: "))
            print(f"Answer: {digitCounter(num)}")
            show_analysis(4)
        except ValueError:
            print("Not a Number")

    elif choice >= 6:
            print("Invalid Options")
             
print("\nThank You for using this Program!")