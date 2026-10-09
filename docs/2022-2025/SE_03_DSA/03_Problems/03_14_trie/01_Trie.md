# Trie ( Prefix Tree)
## Reference
- https://www.hellointerview.com/learn/code/trie/overview

## Overview
-  stores a set of strings in a tree-like data structure. 
- Strings with a common prefix share the same nodes in the trie
- A trie is commonly used to implement features like **spell checkers and auto-complete.**
- Each node also has a boolean value that indicates whether the node represents the **end of a word**
- 3 main operations: 
  - `search(word)`, `O(L)` | L -> length of the word being searched
  - `insert(word)`, `O(L)` 
    - We traverse the trie until we reach the last character of the **search** term.
    - From there, we add the nodes that don't exist already in the trie, 
    - and mark the last node as the end of a word
  - `delete(word)`, `O(L)`

[01_tries-1.excalidraw](../../draw/03/rest/01_tries-1.excalidraw)

@[code:section::TrieNode,Trie](../../../../../src/leetcode/hellointerview/trie/Exercise-1.py)

