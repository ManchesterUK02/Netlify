import timeit

# Non-recursive Fibonacci function
def fibonacci(n):
    """Non recursive fibonacci function"""
    # Calculate the Fibonacci sequence iteratively
    prevnum = 0
    currnum = 1
    for i in range(1,n):
        preprevnum = prevnum
        prevnum = currnum
        currnum = preprevnum + prevnum
    return currnum

# Recursive Fibonacci function
def fibonacci_recursive(n):
    """Recursive fibonacci function"""
    # Calculate the Fibonacci sequence recursively
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Taking input from the user
N = int(input("Enter the value of N for Fibonacci sequence: "))
RUNS = 1000  # Number of runs for timeit


# Calculate and measure time for non-recursive Fibonacci
print("Non Recursive: \n"  "The nth term of Fibonacci number is:", fibonacci(N))
non_recursive_time = timeit.timeit(lambda: fibonacci(N), number=RUNS)
print(f"Time taken: {non_recursive_time} seconds\n" "Time Complexity: O(n)\n" "Space Complexity: O(1)\n")

# Time measurement for recursive Fibonacci
print("Recursive: \n"  "The nth term of Fibonacci number is:", fibonacci(N))
recursive_time = timeit.timeit(lambda: fibonacci_recursive(N), number=RUNS)
print(f"Time taken: {recursive_time} seconds\n" "Time Complexity: O(2^n)\n" "Space Complexity: O(n)\n")

"""
Theory:

### Recursive Approach for Fibonacci Numbers

The recursive approach uses a function that calls itself to find the Fibonacci sequence. The method works on the premise that the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers. The base cases of this sequence are typically considered as F(0) = 0 and F(1) = 1.

However, this method faces issues due to redundant calculations. As the sequence grows, it recalculates the same Fibonacci numbers multiple times. This redundancy results in inefficient time complexity, making it less practical for larger values of n.

### Non-Recursive Approach for Fibonacci Numbers

The non-recursive approach employs iteration rather than recursion. It involves a loop that systematically calculates the Fibonacci numbers by storing and updating the previous two numbers in the sequence.

By avoiding the recursion, this method computes Fibonacci numbers without repeating calculations. It optimizes the process by storing and reusing previous values to compute subsequent ones, making it much more efficient in terms of time complexity for larger n values.

### Time and Space Complexity Analysis

#### Recursive Approach:
- **Time Complexity:** The time complexity of the recursive approach is roughly O(2^n) due to the duplicated computations involved in recursive calls.
- **Space Complexity:** It incurs a space complexity of O(n) due to the recursive call stack, which grows linearly with the input.

#### Non-Recursive Approach:
- **Time Complexity:** The non-recursive approach has a time complexity of O(n) as it directly iterates through the sequence to compute Fibonacci numbers without recalculations.
- **Space Complexity:** It has a space complexity of O(1) since it doesn't require any additional space proportional to the input.

The non-recursive approach is significantly more efficient for computing Fibonacci numbers, particularly for larger n values, as it doesn't incur the repeated calculations and offers better time complexity. The recursive approach is often inefficient due to its recursive nature and higher time complexity.

"""