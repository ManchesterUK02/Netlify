class Node:
    def __init__(self, freq_, symbol_, left_=None, right_=None):
        self.freq = freq_
        self.symbol = symbol_
        self.left = left_
        self.right = right_
        self.huff = ""

def print_nodes(node, val=""):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

def huffman_encoding(word):
    # Calculate the frequency of characters in the given word
    freq = {}
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    chars = list(freq.keys())
    frequencies = list(freq.values())

    nodes = [Node(frequencies[x], chars[x]) for x in range(len(chars))]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]
        left.huff = 0
        right.huff = 1
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    print("Huffman Encoding:")
    print_nodes(nodes[0])

if __name__ == "__main__":
    word = input("Enter a word: ")
    huffman_encoding(word)

"""
Characters: [a, b, c, d, e, f]
Frequency: [5, 9, 12, 13, 16, 45]

Step 1: Frequency Analysis
a: 5
b: 9
c: 12
d: 13
e: 16
f: 45

Step 2: Priority Queue
(a, 5) (b, 9) (c, 12) (d, 13) (e, 16) (f, 45)

Step 3: Building the Huffman Tree
1. Take the two nodes with the lowest frequencies: (a, 5) and (b, 9)
   Create a new node with frequency 14 and set the two nodes as its children.
   New Node: (null, 14)

2. Updated Priority Queue:
(c, 12) (d, 13) (e, 16) (f, 45) (null, 14)

3. Take the two nodes with the lowest frequencies: (c, 12) and (d, 13)
   Create a new node with frequency 25 and set the two nodes as its children.
   New Node: (null, 25)

4. Updated Priority Queue:
(e, 16) (f, 45) (null, 14) (null, 25)

5. Take the two nodes with the lowest frequencies: (e, 16) and (null, 14)
   Create a new node with frequency 30 and set the two nodes as its children.
   New Node: (null, 30)

6. Updated Priority Queue:
(f, 45) (null, 25) (null, 30)

7. Take the two nodes with the lowest frequencies: (null, 25) and (null, 30)
   Create a new node with frequency 55 and set the two nodes as its children.
   New Node: (null, 55)

8. Updated Priority Queue:
(f, 45) (null, 55)

9. Take the two nodes with the lowest frequencies: (f, 45) and (null, 55)
   Create a new node with frequency 100 and set the two nodes as its children.
   New Node: (null, 100)

10. Updated Priority Queue:
(null, 100)

Step 4: Huffman Tree
         (null, 100)
         /          \
        (null, 55)    f
       /           \
    (null, 25)     (null, 30)
     /       \
 (null, 14)  e
             /   \
          (a, 5) (b, 9)

Step 5: Assigning Codes
f: 1
e: 001
a: 0000
b: 0001
c: 010
d: 011

Step 6: Encoding
Input: cbedaf
Encoded Output: 0100001011001

Step 7: Decoding
Encoded Input: 0100001011001
Decoded Output: cbedaf


### Theory of Huffman Encoding

**Huffman Encoding** is a data compression technique used to reduce the size of files by assigning shorter binary codes to more frequent characters and longer codes to less frequent characters. This encoding is accomplished through a greedy algorithm, which means it makes the best choice at each step to achieve the overall optimum solution.

#### Greedy Strategy in Huffman Encoding

1. **Character Frequency Calculation:** Initially, the algorithm scans the input text to compute the frequency of each character.

2. **Priority Queue:** It then creates a priority queue or min-heap data structure to hold all the characters and their frequencies. The characters are sorted based on their frequencies in an ascending order.

3. **Building the Huffman Tree:** The Huffman tree is constructed using a greedy approach:
    - The two nodes with the lowest frequencies are taken from the priority queue.
    - These nodes are combined to create a new internal node, with the sum of their frequencies as the new frequency value.
    - The new node is added back to the priority queue.
    - This process continues until a single root node is formed, creating a binary tree structure with characters and their encoded paths.

4. **Assigning Binary Codes:** The Huffman tree is then traversed to assign binary codes to each character. In this step, characters appearing more frequently receive shorter binary codes, and vice versa.

5. **Encoding the Text:** The actual text is encoded using the generated Huffman codes for each character.

6. **Compression:** The text is compressed by replacing the characters with their corresponding Huffman codes.

### Greedy Strategy

The greedy nature of Huffman encoding ensures that, at every step, it makes the locally optimal choice. Although it doesn't guarantee a globally optimal solution, it generally produces very efficient compression for various types of input data. The strategy of choosing the lowest frequencies first to build the Huffman tree efficiently reduces the overall size of the encoded data.

This encoding technique serves as a vital component in various compression algorithms, such as ZIP files, as it significantly reduces the file size by utilizing fewer bits to represent more frequent characters.

"""
