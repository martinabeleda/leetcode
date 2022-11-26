from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Node:
    children: dict[str, "Node"] = field(default_factory=dict)
    end: bool = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = Node()
            node = node.children[character]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.search_node(word)
        return node.end if isinstance(node, Node) else False

    def starts_with(self, prefix: str) -> bool:
        node = self.search_node(prefix)
        return isinstance(node, Node)

    def search_node(self, word: str) -> Optional[Node]:
        node = self.root
        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                return None
        return node
