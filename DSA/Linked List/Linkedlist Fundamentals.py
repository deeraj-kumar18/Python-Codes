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
    
    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node=Node(data) # Create a new node
        new_node.next=self.head # Point new node's next to the current head
        self.head=new_node      # Assigning our new node as Head.
        return 
    
    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node=Node(data) # Create a new node
        if self.head==None: # If the list is empty, the new node becomes the head
            self.head=new_node
            return
        temp=self.head
        while temp.next:     # Traverse to the last node
            temp=temp.next
        temp.next=new_node  # Point the last node's next to the new node

    # 3. Insert after a given node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node does not exist")
            return
        
        new_node = Node(data)
        new_node.next=prev_node.next     # Point the new node's next to the next of prev_node
        prev_node.next=new_node         # Link prev_node to the new node
    
    # 4. Delete a node by value
    def delete_node(self, key):
        temp=self.head          # taking the reference of head node.

        if temp and temp.data==key:
            self.head=temp.next  # making the next element as Head
            temp=None # Free the old head
            return
        
        # Search the key to be deleted.
        prev=None
        while temp and temp.next!=key:
            prev=temp
            temp=temp.next
            
        # If the key was not found in the list
        if temp is None:
            print(f"{key} not found in the list.")
            return
        
        # If found
        prev.next=temp.next   # Unlink the node from the linked list
        temp=None   #Free the head
    
    # 5. Delete the entire list
    def delete_list(self):
        self.head=None    # Removing all references will delete the list
    
    # 6. Search for a node
    def search(self, key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
        
        return False
    
    # 7. Display the linked list
    def display(self):
        nodes=[]
        temp=self.head
        while temp:
            nodes.append(str(temp.data))  # Collect all node data
            temp=temp.next
        
        print(" -> ".join(nodes)) # Print linked list