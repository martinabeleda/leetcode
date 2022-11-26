from leetcode.tree.trie_ii import Trie


def test_trie_1():
    trie = Trie()
    trie.insert("apple")
    trie.insert("apple")
    assert trie.count_words_equal_to("apple") == 2
    assert trie.count_words_starting_with("app") == 2
    trie.erase("apple")
    assert trie.count_words_starting_with("app") == 1
    trie.erase("apple")
    assert trie.count_words_starting_with("app") == 0


def test_trie_empty():
    trie = Trie()
    assert trie.count_words_starting_with("foo") == 0
    assert trie.count_words_starting_with("bar") == 0
