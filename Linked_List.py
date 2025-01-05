"""
A Linked List Implementation

Used to learn Leetcode

Dalice Dieckman

Date: 2024-12-11
"""

class Node:
    def __init__(self, data):
        """
        Initializes a node in the list
        """
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        """
        Initializes the LinkedList class
        """
        self.head = head
        self.count = 0


    def insert_at_start(self, data):
        """
        Inserts a new node at the start of the list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.count +=1
            return new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return new_node


    def insert_at_index(self, data, index):
        """
        Inserts a node at the given index
        """

        if index == 0:
            new_node = self.insert_at_start(data)
            self.count += 1
            return new_node

        position = 0
        current_node = self.head
        while not current_node and position+1 != index:
            # We iterate until we reach the tail (None)
            # or until we are just behind the node where the target index is.
            position += 1
            current_node = current_node.next

            if position == index -1:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                self.count += 1
                return new_node

            else:
                print("Index is not present")



    def insert_at_end(self, data):
        """
        Insert node at the end of the list
        """

        new_node = Node(data)
        # If it is a new list, we insert it at the start
        if self.head is None:
            self.head = new_node
            self.count += 1
            return new_node

        current_node = self.head
        # We iterate until we reach the tail, which is None
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        self.count += 1
        return new_node


    def update_node(self, val, index):
        """
        Changes the value at a given node
        """

        current_node = self.head
        position = 0

        # If our chosen node is at the start of the list
        if index == 0:
            current_node.data = val
            return current_node

        else:
            # we iterate up to but not onto the index.
            # IE) As we choose node 6, it will be at index 5.
            while not index >= position:
                position += 1
                current_node = current_node.next

            # After iterating to the target node, we need to update its value.
                if index == position:
                    current_node.data = val
                    return current_node
            
            print("Index not present")


    def delete_node(self, index):
        """
        Remove a node from the list
        """

        # If the list is empty we can't remove anything.
        if not self.head:
            print("List is empty")

        current_node = self.head
        position = 0
        prev_node = None

        # If we are trying to remove the first node.
        if index == 0:
            self.head = self.head.next
            self.count -= 1
            return

        else:
            # Iterate until the node
            while position <= index:
                prev_node = current_node
                current_node = current_node.next
                current_pos += 1

            if index == position:
                # Remove node when found
                prev_node.next = current_node.next
                self.count -= 1
                return
            
            # If the position is out of range
            print("Index not preset")
        

    def print(self):
        """
        Prints the contents of each node in the list
        """

        current_node = self.head
        list_data = []
        while current_node:
            list_data.append(current_node.data)
            current_node = current_node.next

        return print(list_data)

    def get_data_array(self):
        """
        Returns a list of each node's contents
        """

        current_node = self.head
        list_data = []
        while current_node:
            list_data.append(current_node.data)
            current_node = current_node.next

        return list_data


