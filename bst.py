# binary_search_tree.py
# Jacob Glines
# 2019.04.22
# This file creates a binary search tree, fills it with words, and
# prints them in order
#
# Usage:
# python3 binary_search_tree.py

from cstree import Tree


def add_words(list, filename):
    """Add words to the list.

    Variables:
        list      :  The binary search tree we are wanting to add to
        filename  :  The file that contains the strings to add to the list
    """

    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                list.insert(word)


def create_tree():
    """Create a binary search tree."""

    words_list = Tree()
    add_words(words_list, 'test.txt')
    return words_list


def do_binary_search_tree():
    """Create a list and print it."""

    words_list = create_tree()
    print("\nWORD           COUNTER\n")
    words_list.traverse(words_list.root)


do_binary_search_tree()
