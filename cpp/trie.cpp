#include <iostream> 

const int ALPHABET_SIZE = 26;

// trie node
struct TrieNode {
  struct TrieNode *children[ALPHABET_SIZE];
  bool is_leaf;
};

// Returns new trie node (initialized to NULLs)
struct TrieNode *create_node(void) {
  struct TrieNode *root = new TrieNode;

  root->is_leaf = false;

  for (int i = 0; i < ALPHABET_SIZE; i++)
    root->children[i] = nullptr;

  return root;
}

// If not present, inserts key into trie
// If the key is prefix of trie node, just
// marks leaf node
void insert(struct TrieNode *root, string key) {
  struct TrieNode *pCrawl = root;

  for (int i = 0; i < key.length(); i++) {
    int index = key[i] - 'a';
    if (!pCrawl->children[index])
      pCrawl->children[index] = create_node();

    pCrawl = pCrawl->children[index];
  }

  // mark last node as leaf
  pCrawl->is_leaf = true;
}

// Returns true if key presents in trie, else false
bool search(struct TrieNode *root, string key) {
  struct TrieNode *pCrawl = root;

  for (int i = 0; i < key.length(); i++) {
    int index = key[i] - 'a';
    if (!pCrawl->children[index])
      return false;

    pCrawl = pCrawl->children[index];
  }

  return (pCrawl != nullptr && pCrawl->is_leaf);
}
