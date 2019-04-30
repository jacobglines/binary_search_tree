# cstree.py
# Jacob Glines
# 2019.04.22
# This file defines an Tree class with the usual behaviors
# of a binary tree: traverse and insert
#
# Usage:
# from cstree import Tree

from cstree_node import TreeNode


class Tree:
    """ Implement a Tree object.

    The Tree class knows it's root. It also supports traversing
    and then a recursive insert.
    """

    def __init__(self):
        self.root = None

    def traverse(self, pointer):
        """Print the tree in order.

        Variables:
            pointer  :  TreeNode in memory. We need left and right, and print
                        from it
        """

        if pointer is not None:
            self.traverse(pointer.left)
            pointer.print()
            self.traverse(pointer.right)

    def insert(self, value):
        """Start the insert recursion.

        Variables:
            value: string to add to the list
        """

        self.insert_bst(self.root, value)

    def insert_bst(self, ptr, value):
        """Recursion of insert.

        Variables:
            ptr    :  Use this address in memory to access it's node
            value  :  the string we are using to compare to pointer
        """

        if self.root is None:
            self.root = TreeNode(value)

        # We don't want the same word to print twice so we just
        # add to the counter.
        elif ptr.name == value:
            ptr.counter += 1

        # Do the left side of the node we are looking at first.
        elif value < ptr.name:
            if ptr.left is None:
                ptr.left = TreeNode(value)
            else:
                self.insert_bst(ptr.left, value)

        # then do the right side of the node we are looking at.
        elif value > ptr.name:
            if ptr.right is None:
                ptr.right = TreeNode(value)
            else:
                self.insert_bst(ptr.right, value)
