"""
Binary Tree
Data is added to the tree following
a preorder traversal using an ascending order.


Dalice Dieckman


Resources:
    https://www.w3schools.com/python/ref_keyword_nonlocal.asp
    https://leetcode.com/problems/print-binary-tree/solutions/5428295/easy-python-solution/
    https://stackoverflow.com/questions/300935/are-duplicate-keys-allowed-in-the-definition-of-binary-search-trees


Notes:
    Struggle to create get_height(), and print()
         Used some resources above

    Testing:
    Now struggle to get add() to work. I need to manually balance the tree
    as I add values to it. Seems to be a pain.
        I may change tree code to a self-balancing tree.
"""


class Node:
    """
    Represents a node in the tree
    """
    def __init__(self,data):
        """
        Initializes a node in a binary tree
        """
        self.left = None
        self.right = None
        self.data = data



class Tree:
    def __init__(self):
        """
        Initializes the binary tree
        """
        self.root = None
        self.size = 0


    def add_recursive(self, data):
        """
        Adds data to the tree using a recursive nested function.
        """

        def add(data, node):
            if data < node.data:
                if node.left:
                    node = node.left
                    return add(node)

                else:
                    node.left = Node(data)
                    self.size +=1
                    return

            elif data > node.data:
                if node.right:
                    node = node.right
                    return add(node)

                else:
                    node.right = Node(data)
                    self.size +=1
                    return

            else:
                print("Can not add, it duplicate")

        if not self.root:
            self.root = data
            self.size +=1

        else:
            return add(data, self.root)


    def add(self, data):
        """
        Adds a node to the tree with a given value
        Adding values may result in an imbalance.
        TODO: Change add() to organize in the event of data imbalances.
        """

        # If there is no root in the tree
        if not self.root:
            self.root = Node(data)
            self.size +=1
            return

        else:
            current = self.root
            while True:
                # We try to add it to the left first
                if data < current.data:
                    if current.left:
                        current=current.left

                    else:
                        current.left=Node(data)
                        self.size +=1
                        break

                # We try to add it to the right now
                elif data > current.data:
                    if current.right:
                        current = current.right

                    else:
                        current.right = Node(data)
                        self.size +=1
                        break

                # If data is already present we skip it and return an error.
                elif data == current.data:
                    print(f"Error: Cannot add duplicate data. {current.data} already exists. ")
                    break


    def view_tree(self):
        """
        Prints a matrix which contains strings of the tree values.
        TODO: Case of imbalances wrecking view_tree() with incorrect/exaggerated row/col values.

        Tried to write an iterative solution without a nested function.
        I dont know how to implement the r, and c values using while loops.
        I need to be able to place both left and right values in a row
        but to do so would require me to flip the mid + 1 and mid - 1 variable.
            I could use a switch. Change left, flip switch, code checks for flip, change right,
            increment counter and move to the next row.
            Try later. Maybe
        """

        height = self.get_height()

        # Calculate the number of rows and columns used in the tree matrix
        row = height + 1
        # Col val cal by summing the max number of node positions across all
        # levels of the tree. lvl0 = 1 for root, lvl1=2, lvl3=4
        column = 2**height

        # Create the matrix:
        tree_matrix = [["" for x in range(column)] for y in range(row)]

        # Place the root node's data in the middle of the first row
        mid = column // 2
        tree_matrix[0][mid] = str(self.root.data)

        # Recursion used here: Why?
        # We need to change 2 values from the root,
        # and each of those values may hold further values down the tree.
                # Also tree traversal --> Recursion.

        def form_tree_matrix(node, r, c):
            # We can use nonlocal to use a variable within a nested function
            # defined in higher function
            nonlocal tree_matrix
            if node:
                tree_matrix[r][c] = str(node.data)
                form_tree_matrix(node.left, r + 1, c - 1)
                form_tree_matrix(node.right, r + 1, c + 1)

        # Add/Subtract the adjusted column value to find the location of the node based on
        # if its left/right of the middle.
        form_tree_matrix(self.root.left, 1, (mid - 1))
        form_tree_matrix(self.root.right, 1, (mid + 1))

        for x in range(len(tree_matrix)):
            print(tree_matrix[x])

        return tree_matrix


    def get_level_node(self, data):
        """
        Returns the 0-indexed level of a data point in the tree.
        Uses the view_tree() matrix to determine data level.

        Try using a stack based method where we scan each rows data points
        before moving to the next one.
        """

        if data == self.root.data:
            return 0

        tree_matrix = self.view_tree()
        lvl = 0
        for x in range(len(tree_matrix)):
            for y in range(len(tree_matrix[x])):
                if tree_matrix[x][y] == str(data):
                    return lvl

            else:
                lvl +=1


    def get_height(self):
        """
        Returns the height of the binary tree
        AKA The max depth
        I use a nested function as I need my solution to be recursive,
        while still remaining a method within the Tree class.
            Need to traverse the tree to calc height --> Recursion.
                Cant use recursive methods in a class definition.
                So we have to use nested functions
        """

        def calc_height(root):
            # Base Case: We are on a leaf node.
            if not root:
                return 0

            left_depth = calc_height(root.left)
            right_depth = calc_height(root.right)

            return 1 + max(left_depth, right_depth)
        return calc_height(self.root)


    def inorder_traversal(self):
        """
        Returns a list of values following an inorder traversal of the tree.
        I used nested functions here to allow the recursive method to be used in the Tree class.
        The nested function uses an iterative method to traverse
        Order: Left -> Root -> Right
        """

        result = []
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current)
            current = current.right

        return result


    def preorder(self):
        """
        Returns a list of values following an inorder traversal of the tree.
        Order: Root -> Left -> Right
        """

        result = []
        stack = []
        current = self.root

        while current or stack:
            # We check to see if the current node we are on is valid.
            if current:
                result.append(current.data)
                # before we move into the left sub node, we check to see if there is
                # a right sub node. If there is, we push that node onto the stack.
                if current.right:
                    stack.append(current.right)

                current = current.left

            else:
                current = stack.pop()

        return result


    def postoder_2(self):
        """
        Mem if have time, else use postorder()
        """
        r = []  # List to store the result
        s = []  # Stack for iterative traversal
        current = self.root  # Start at the root of the tree

        while current or s:  # Process while there are nodes to visit
            # Traverse to the leftmost node, pushing nodes onto the stack
            if current:
                s.append(current)  # Push current node onto the stack
                current = current.left  # Move to the left child
            else:
                # Look at the top node in the stack without removing it
                temp = s[-1].right  # Check the right child of the top node

                if temp and temp not in r:  # If right child exists and hasn't been visited
                    current = temp  # Move to the right child
                else:
                    # Visit the node and mark it as visited
                    node = s.pop()  # Remove the node from the stack
                    r.append(node)  # Add it to the result list
                    # No need to set `current` here because we are backtracking

        return r



    def postorder(self):
        """
        Returns a list of tree values when gathered from a postorder traversal.
        Order: Left -> Right -> Root
        """

        result = []
        def traverse(root):
            if not root:
                return None

            traverse(root.left)
            traverse(root.right)
            result.append(root.data)

        traverse(self.root)
        return result
