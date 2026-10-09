# section::TrieNode::start
# Note: Not binary tree, root node with no letter
class TrieNode:
    def __init__(self, children = None, eow = False):
        self.isEndOfWord = eow
        self.children = children if children is not None else {} # dict
        """
        example: 
        root.children = {
            'A': TrieNode(),
            'B': TrieNode(),
            'C': TrieNode(),
            ...
        }
        """
# section::TrieNode::end


class Solution:
    # section::Trie-basic::start
    def __init__(self, words=''):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word): # ⭐
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word):
        curr_node = self.root
        for w in word:
            if w in curr_node.children:
                curr_node = curr_node.children[w]
            else: return False

        return True if curr_node.isEndOfWord else False
        #return curr_node.isEndOfWord

    def starts_with(self, prefix): # same as above, only return statement is different
        curr_node = self.root
        for w in prefix:
            if w in curr_node.children:
                curr_node = curr_node.children[w]
            else: return False

        return True
    # section::Trie-basic::end

    # section::suggest-prefixed-word::start
    # Return a list of all words in the trie that start with the given prefix.
    # ✔️ solved
    def prefix(self, prefix):
        # Step-1 : reach/traverse to prefix  === search
        curr_node = self.root
        for w in prefix:
            if w in curr_node.children:
                curr_node = curr_node.children[w]
            else: return []

        # Step-2 : from there, form words | recursively ⭐
        res = []
        def word(pre, node: TrieNode):
            for k,v in node.children.items():
                word(pre+k, v)
            if node.isEndOfWord: res.append(pre)

        word(prefix,curr_node)
        return res
    # section::suggest-prefixed-word::end

    # section::delete::start
    # --- Check helloI solution --- 👈
    def delete(self, word):
        curr_node = self.root
        for w in word:
            if w in curr_node.children:
                curr_node = curr_node.children[w]
            else: return

        curr_node.isEndOfWord = False
        if curr_node.children == {}:
            del curr_node
    # section::delete::end
