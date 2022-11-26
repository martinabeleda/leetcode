"""Implement Trie II

Approach:
    - Trie insert
        - Iterate over the characters of a word
        - If node doesn't, exist for this character, create one.
        - If the node exists, increment the count and continue to the next node.
    - Count words equal to
        - Search the trie until you get to a terminal node
        - Return the count stored at the node
    - Count words starting with
        - Traverse the tree for a prefix
        - Return the number of children

Data structures:
    - Node:
        - `value`: The count of the word instances that this node belongs to.
        - `children`: Hashmap where the key is a a character and value is a `Node`.
        - `is_termial`: A boolean indicating if the node is the end of a word.

Example:
    Insert Apple
        a = 1
        p = 1
        p = 1
        l = 1
        e = 1 1

    Insert Apple
    
        a = 2
        p = 2
        p = 2
        l = 2
        e = 2 2

    Count words starting with "app"
        - Traverse nodes a, p, p.
        - Return value = 2

    Erase apple:
        - Traverse nodes a, p, p, l, e
        - Decrement count at each node
        - If decremented to 0, remove node

Source - [leetcode](https://leetcode.com/problems/implement-trie-ii-prefix-tree/)
"""
from dataclasses import dataclass, field


@dataclass
class Node:
    children: dict[str, "Node"] = field(default_factory=dict)
    count: int = field(default=0)
    end_count: int = field(default=0)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = Node()
            node = node.children[character]
            node.count += 1
        node.end_count += 1

    def count_words_equal_to(self, word: str) -> int:
        node = self.root
        for character in word:
            if character not in node.children:
                return 0
            node = node.children[character]
        return node.end_count

    def count_words_starting_with(self, prefix: str) -> int:
        node = self.root
        for character in prefix:
            if character not in node.children:
                return 0
            node = node.children[character]
        return node.count

    def erase(self, word: str) -> None:
        node = self.root
        for character in word:
            temp = node.children[character]
            temp.count -= 1
            if temp.count == 0:
                del node.children[character]
            node = temp
        temp.end_count -= 1
