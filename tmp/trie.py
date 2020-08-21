from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.
    """

    def __init__(self):
        self.root = TrieNode()
        # self.children = collections.defaultdict(Trie)

    def insert(self, word):
        '''@param {string} word
        @return {void}
        Inserts a word into the trie.'''
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word):
        '''@param {string} word
        @return {boolean}
        Returns if the word is in the trie.
        '''
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_end

    def starts_with(self, word):
        '''@param {string} word
        @return {boolean}
        Returns if there is the word in the trie that starts with @word
        '''
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


t = Trie()
t.insert("abcd")
print(t.search("abcde"))
print(t.starts_with("bc"))
