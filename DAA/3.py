class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt_, val_, ind_):
        # Initialize an ItemValue object with weight, value, and index
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        # Calculate cost as value divided by weight
        self.cost = val_ / wt_

    def __lt__(self, other):
        # Comparator function to compare costs of two items
        return self.cost < other.cost


def fractionalKnapSack():
    # Take input from the user for items' weights and values
    wt = list(map(int, input("Enter the weights of the items: ").split()))
    val = list(map(int, input("Enter the values of the items: ").split()))

    # Take input from the user for the capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Create a list of ItemValue objects
    iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]
    # Sort the list of ItemValue objects based on cost in descending order
    iVal.sort(key=lambda x: x.cost, reverse=True)

    totalValue = 0
    # Loop through each item to find the maximum value in the knapsack
    for i in iVal:
        curWt = i.wt
        curVal = i.val
        if capacity - curWt >= 0:
            # If the item fits entirely in the knapsack, add its value to the total value
            capacity -= curWt
            totalValue += curVal
        else:
            # If the item doesn't fit, add the fraction that can fit to the total value
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = int(capacity - (curWt * fraction))
            break  # Break the loop as the knapsack is full

    return totalValue


if __name__ == "__main__":
    # Execute the fractional knapsack algorithm and display the maximum value in the knapsack
    maxValue = fractionalKnapSack()
    print("Maximum value in Knapsack =", maxValue)

    
"""
The Fractional Knapsack problem is a type of optimization problem where the goal is to select items from a set, each with a weight and an associated value, to fit into a knapsack with a specified capacity. The objective is to maximize the total value of the items included in the knapsack without exceeding its weight capacity.

A greedy approach to solving the Fractional Knapsack problem involves selecting items by considering the ratio of value to weight. The algorithm iterates through the items, selecting the one with the highest value-to-weight ratio first. It adds as much of that item as possible to the knapsack until the capacity is full.

The steps involved in the greedy approach are as follows:

1. **Compute value-to-weight ratios:** Calculate the value-to-weight ratio for each item.

2. **Sort items:** Sort the items based on their value-to-weight ratio in non-increasing order.

3. **Fill the knapsack:** Starting from the item with the highest ratio, add as much of that item as possible to the knapsack. If the whole item cannot fit, take a fraction of it, maximizing the value until the knapsack is full.

4. **Calculate total value:** Sum up the values of the items included in the knapsack.

This greedy strategy is based on the idea that selecting items with the highest value-to-weight ratio at each step will result in the optimal solution for fractional knapsack problems. It might not always provide the most optimal solution for all knapsack problems, unlike the 0/1 Knapsack problem, but it is efficient and effective for fractional cases.

The implementation involves iterating through the items, sorting them based on their value-to-weight ratio, and choosing the best items to maximize the overall value within the knapsack's weight capacity.
"""