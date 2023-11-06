from queue import Queue

# Define an Item class to represent each item in the knapsack
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

# Define a Node class to represent each node in the branch and bound tree
class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level    # The level of the node in the tree
        self.profit = profit  # The total profit achieved so far
        self.bound = bound    # The maximum profit that can be achieved
        self.weight = weight  # The total weight of the items included so far

# Define a compare function to sort items by their value-to-weight ratio in descending order
def compare(a, b):
    r1 = a.value / a.weight
    r2 = b.value / b.weight
    return r1 > r2

# Calculate the profit bound for a node in the branch and bound tree
def bound(u, n, W, arr):
    if u.weight >= W:  # If the weight exceeds the capacity, profit bound is 0
        return 0

    profitBound = u.profit
    j = u.level + 1
    totWeight = u.weight

    # Consider the remaining items that can fit into the knapsack to calculate the profit bound
    while j < n and totWeight + arr[j].weight <= W:
        totWeight += arr[j].weight
        profitBound += arr[j].value
        j += 1

    # If there are still items left, consider a fraction of the next item's profit based on the remaining space
    if j < n and totWeight < W:
        profitBound += (W - totWeight) * arr[j].value / arr[j].weight

    return profitBound

# Solve the 0/1 Knapsack problem using Branch and Bound
def knapsack_solution(W, arr, n):
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)  # Sort items based on value-to-weight ratio

    q = Queue()
    u = Node(-1, 0, 0, 0)  # Start with a root node
    q.put(u)
    maxProfit = 0

    while not q.empty():
        u = q.get()

        if u.level == -1:
            v = Node(0, 0, 0, 0)  # First node represents the root

        if u.level == n - 1:  # If it's a leaf node, skip
            continue

        # Include the next item in the knapsack and calculate its profit and weight
        v = Node(u.level + 1, u.profit + arr[u.level + 1].value, 0, u.weight + arr[u.level + 1].weight)

        if v.weight <= W and v.profit > maxProfit:  # If this node can give better profit, update maxProfit
            maxProfit = v.profit

        v.bound = bound(v, n, W, arr)  # Calculate the profit bound

        if v.bound > maxProfit:  # If the bound is higher than the current maximum profit, add it to the queue
            q.put(v)

        # Do not include the next item and calculate its profit bound
        v = Node(u.level + 1, u.profit, 0, u.weight)
        v.bound = bound(v, n, W, arr)

        if v.bound > maxProfit:  # If the bound is higher than the current maximum profit, add it to the queue
            q.put(v)

    return maxProfit

# Driver Code
if __name__ == '__main__':
    W = int(input("Enter the capacity of the knapsack: "))  # Accept capacity input from the user
    n = int(input("Enter the number of items: "))  # Accept the number of items from the user

    arr = []
    for i in range(n):
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        value = int(input(f"Enter the value of item {i + 1}: "))
        arr.append(Item(weight, value))

    print('Maximum possible profit =', knapsack_solution(W, arr, n))
    
    
"""
The **0-1 Knapsack Problem** is a classic optimization problem where you have a set of items, each with a weight and a value, and you want to determine the number of each item to include in a knapsack to maximize the total value without exceeding the capacity of the knapsack.

### Branch and Bound Strategy

The **branch and bound algorithm** is a method used for solving optimization problems. It systematically searches the solution space to find the global optimal solution. Here's a high-level overview:

1. **Initial Bounds Calculation:** Calculate the initial bound of the problem. This bound serves as the highest possible value that can be achieved using the knapsack's capacity.

2. **Initial Node Creation:** Create the root node to begin the exploration of the solution space. Each node corresponds to a subproblem, keeping track of its level, profit, bound, and weight.

3. **Explore the Nodes:** The algorithm systematically explores nodes using a priority queue or a similar structure.
   - At each step, it chooses the most promising node and evaluates its children.
   - The bound function is used to calculate the maximum possible profit if items in the knapsack are included up to the weight limit.
   - If the bound of a node is higher than the current maximum profit, it is added to the queue for further exploration.
   - If a node is a leaf or exceeds the weight limit, it is skipped.

4. **Optimal Solution Identification:** The algorithm continues to explore nodes until the queue is empty, finding the node with the maximum profit as the optimal solution.

### 0-1 Knapsack and Branch and Bound

The 0-1 Knapsack problem is well-suited for the branch and bound algorithm because it uses the bound function to evaluate and compare nodes. The bound function allows the algorithm to intelligently explore the solution space without the need to evaluate all possible combinations, thus significantly improving the efficiency in finding the optimal solution.

This approach facilitates the quick discovery of the best solution for a given capacity, even for large instances of the 0-1 Knapsack problem. The branch and bound strategy ensures a more systematic exploration of the solution space, making it particularly effective for this optimization problem.
"""
