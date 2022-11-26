from leetcode.tree.trie import Trie


def test_trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.starts_with("app")
    trie.insert("app")
    assert trie.search("app")
