# Data Structures

This document serves as my personal review of data structures used in programming. 
I expect this document to begin with only the most fundamental concepts: stacks, queues, graphs, 
linked lists, arrays, hash maps, etc. As I learn more though, I expect this document to become quite lengthy. This 
document will not serve as an in-depth review of everything, but rather will hold only the most vital content
to remember. It's my intention to link longer explanations of individual concepts to separate documents, 
particularly those which are more complex or have more to remember. 


# Fundamentals
We'll begin with the most basic of structures, a simple list. 

# Lists
# Stacks
**LIFO**: Last In First Out
- The stack is a last-in, first-out data structure

The <u>means of access</u> defines a stack, not the implementation itself
- It must be LIFO
- You can use pointers, arrays, etc. (doesn't matter)

**Push**: Add an object to the top of the stack

**Pop**: Remove the object on the top of the stack

**Underflow**: Attempting to pop an element from an empty stack





## Assembly
**Stack Pointer**: Points to the address on the *top* of the stack
- R6 is *always* the stack pointer 

**Push**:
- `ADD R6, R6, #-1 ; decrement stack ptr`
- `STR R0, R6, #0 ;store data R0`

**Pop**:
- `LDR R0, R6, #0 ; load data from TOS`
- `ADD R6, R6, #1 ; increment stack ptr`

**Stack Underflow**: We must check that the stack is not empty: the pointer does not point to the bottom of the stack
- If R6 points to bottom of the stack --> stack is empty
- `MEM[bottom-of-stack]` is <u>not</u> an object on the stack
- Need to know the limits of the stack (defined in program)

**Stack Overflow**: We must check that the stack still has space: the pointer does not "exceed" the max memory address value
- I quote "exceed" because we the max memory address is actually the smallest value in memory (by our implementation)
- If R6 points to the max stack value --> stack is full


## Python

# Queues

# Hashing
## Addressing and Hash Functions
## Probing
## Double Hashing

# Heaps
## Heap
## Priority Queues

# Linked Lists

**Linked List**: a set of nodes that are linked
- Types: Singly, Doubly, Circular, etc.

**Node**: a unit of data
- Consists of <u>at least</u> 2 words (or memory location)
- <u>Word 1</u> *(Mem Location 1)*: Some data stored by the node
- <u>Word 2</u> *(Mem Location 2)*: Pointer to the next node
- *Nodes may have many implementations, the one above is an example of a single implementation*

**Head**: points to the first element in the linked list
- Python: `head` variable
    - `head.next = first_node`
- Assembly: designated memory location for the head (memory location contains address of first node)

**Tail**: indicates the last element in the linked list. Tail node points to the *sentinel*, a value indicating the end of the linked list. 

## Singly Linked
Node
- Consists of at least 2 words (or memory location)
- <u>Word 1</u> *(Mem Location 1)*: Some data stored by the node
- <u>Word 2</u> *(Mem Location 2)*: Pointer to the next node
- *Nodes may have many implementations, the one above is an example of a single implementation*

## Doubly Linked
Node
- Consists of at least 3 words (or memory location)
- <u>Word 1</u> *(Mem Location 1)*: Some data stored by the node
- <u>Word 2</u> *(Mem Location 2)*: Pointer to the next node
- <u>Word 3</u> *(Mem Location 3)*: Pointer to the previous node
- *Nodes may have many implementations, the one above is an example of a single implementation*

## Assembly
**Head Pointer**: points to the address of the head node
- A designated memory location (say `x4000`) points to the location of the *head node*
- If the head pointer has the sentinel (`x0000`, the null pointer), then the linked list is empty

**Head Node**: first node in the linked list

**Sentinel**: `x0000` 
- Your `sentinel` can be any designated number
- `x0000` is often the most common choice

**Tail Node**: pointer to the next node = `x0000`


# Trees
## Tree Traversals
## Binary Search Trees
## Tries

# Graphs
## Graph Representations
## Breadth First Search
## Depth First Search
## Topological Sort
## Prim's Algorithm
## Kruskal's Algorithm

\end{document}