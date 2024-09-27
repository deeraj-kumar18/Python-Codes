'''
What is a Linked List?
A linked list is a linear data structure that consists of a series of nodes connected by 
pointers (in C or C++) or references (in Java, Python and JavaScript). Each node contains data 
and a pointer/reference to the next node in the list. Unlike arrays, linked lists allow for 
efficient insertion or removal of elements from any position in the list, as the nodes are 
not stored contiguously in memory.

    Operation	        Time Complexity	Space	Explanation
Insertion at Beginning	O(1)	        O(1)	Constant-time pointer updates.
Insertion at End	    O(n)	        O(1)	Traversal required to find the last node.
Insertion at Position	O(n)	        O(1)	Traversal to the desired position, then constant-time pointer updates.
Deletion at Beginning	O(1)	        O(1)	Constant-time pointer update.
Deletion at End		    O(n)	        O(1)    Traversal required to find the second last node.
Deletion at Position	O(n)	        O(1)	Traversal to the desired position, then constant-time pointer updates.
Searching in Linkedlist O(n)	        O(1)	Traversal through the list to find the desired value.
'''
class Node:
    def __init__(self, data):
        self.data = data  # Data
        self.next = None  # Pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty