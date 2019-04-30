# cstree_node.py
# Jacob Glines
# 2019.04.22
# This file defines a Tree node class with the usual behaviors
# of a node: name, left and right pointers, and a counter
#
# Usage:
# from cstree_node import TreeNode


class TreeNode:
    """ Implement a TreeNode object.

    The TreeNode class supports a name, left, right, and counter. It also
    can print itself.
    """

    def __init__(self, value):
        self.name = value
        self.left = None
        self.right = None
        self.counter = 1

    def print(self):
        """Print the name and counter."""

        print("{0:15}{1:4}".format(self.name, self.counter))
