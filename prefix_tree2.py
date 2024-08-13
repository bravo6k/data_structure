class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.setdefault(c, {})
        curr["<END>"] = True

    def search(self, word: str) -> bool:
        def dfs(node, remain):
            if not remain:
                return "<END>" in node
            
            char = remain[0]
            if char == '.':
                return any(dfs(node[key], remain[1:]) for key in node if key != "<END>")
            elif char in node:
                return dfs(node[char], remain[1:])
            
            return False

        return dfs(self.root, word)


import unittest

class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.word_dict = WordDictionary()

    def test_basic_functionality(self):
        self.word_dict.addWord("bad")
        self.word_dict.addWord("dad")
        self.word_dict.addWord("mad")
        self.assertFalse(self.word_dict.search("pad"))
        self.assertTrue(self.word_dict.search("bad"))
        self.assertTrue(self.word_dict.search(".ad"))
        self.assertTrue(self.word_dict.search("b.."))

    def test_empty_word(self):
        self.word_dict.addWord("")
        self.assertTrue(self.word_dict.search(""))
        self.assertFalse(self.word_dict.search("a"))

    def test_single_character(self):
        self.word_dict.addWord("a")
        self.assertTrue(self.word_dict.search("a"))
        self.assertTrue(self.word_dict.search("."))
        self.assertFalse(self.word_dict.search("b"))

    def test_long_word(self):
        long_word = "abcdefghijklmnopqrstuvwxyz"
        self.word_dict.addWord(long_word)
        self.assertTrue(self.word_dict.search(long_word))
        self.assertTrue(self.word_dict.search("abcdefghijklmnopqrstuvwxy."))
        self.assertFalse(self.word_dict.search("abcdefghijklmnopqrstuvwxyz."))

    def test_wildcard_only(self):
        self.word_dict.addWord("abc")
        self.assertTrue(self.word_dict.search("..."))
        self.assertFalse(self.word_dict.search("...."))

    def test_prefix_matching(self):
        self.word_dict.addWord("apple")
        self.assertFalse(self.word_dict.search("app"))
        self.assertTrue(self.word_dict.search("apple"))

    def test_multiple_wildcards(self):
        self.word_dict.addWord("abcde")
        self.assertTrue(self.word_dict.search("a.c.e"))
        self.assertTrue(self.word_dict.search(".b.d."))
        self.assertFalse(self.word_dict.search("a.c.f"))

    def test_case_sensitivity(self):
        self.word_dict.addWord("Hello")
        self.assertTrue(self.word_dict.search("Hello"))
        self.assertFalse(self.word_dict.search("hello"))

    def test_broad_nested_tree(self):
        words = [
            "a", "an", "ant", "anteater", "antelope",
            "b", "be", "bee", "beer", "beeswax",
            "c", "cat", "catch", "catcher", "catchphrase",
            "do", "dog", "dogma", "dogmatic", "dogmatically",
            "e", "ee", "eek", "eel", "eerie"
        ]
        for word in words:
            self.word_dict.addWord(word)

        # Test exact matches
        for word in words:
            self.assertTrue(self.word_dict.search(word), f"Should find exact match: {word}")

        # Test prefix searches (should return False)
        self.assertFalse(self.word_dict.search("anteat"))
        self.assertFalse(self.word_dict.search("beeswa"))
        # self.assertFalse(self.word_dict.search("catch"))  # This is actually in the list, so it should return True
        self.assertFalse(self.word_dict.search("dogmati"))

        # Test wildcard searches
        self.assertTrue(self.word_dict.search("ant....."))  # matches "anteater"
        self.assertTrue(self.word_dict.search("b..."))  # matches "beer"
        self.assertTrue(self.word_dict.search("c....."))  # matches "catcher"
        self.assertTrue(self.word_dict.search("dogma..."))  # matches "dogmatic"
        self.assertTrue(self.word_dict.search("....."))  # matches "eerie"

        # Test complex wildcard patterns
        self.assertTrue(self.word_dict.search("a.t....."))  # matches "anteater"
        self.assertTrue(self.word_dict.search("b....a."))  # matches "beeswax"
        self.assertTrue(self.word_dict.search("c...h.."))  # matches "catcher"
        self.assertTrue(self.word_dict.search("d..m...."))  # matches "dogmatic"
        self.assertTrue(self.word_dict.search(".e."))  # matches "bee" or "eel"

        # Test non-existent patterns
        self.assertFalse(self.word_dict.search("anteatery"))
        self.assertFalse(self.word_dict.search("beehive"))
        self.assertFalse(self.word_dict.search("doghouse"))
        self.assertFalse(self.word_dict.search("f.."))

    def test_overlapping_words(self):
        words = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        for word in words:
            self.word_dict.addWord(word)

        for i in range(1, 6):
            self.assertTrue(self.word_dict.search("a" * i))
        self.assertFalse(self.word_dict.search("a" * 6))

        self.assertTrue(self.word_dict.search("."))
        self.assertTrue(self.word_dict.search(".."))
        self.assertTrue(self.word_dict.search("..."))
        self.assertTrue(self.word_dict.search("...."))
        self.assertTrue(self.word_dict.search("....."))
        self.assertFalse(self.word_dict.search("......"))

if __name__ == '__main__':
    unittest.main()