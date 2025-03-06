class TrieNode():
    def __init__(self, parent="root", name="root", length=0, isEnd=False):
        self.parent = parent
        self.name = name
        self.child = {}
        self.length = length
        self.isEnd = isEnd


class Trie():
    def __init__(self):
        self.rootnode = TrieNode()

    def insert(self, word):
        node = self.rootnode
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode(parent=node.name, name=char,
                                            length=node.length+1, isEnd=False)
            node = node.child[char]
        node.isEnd = True

    def write_time(self, word):
        time = 0
        node = self.rootnode
        for char in word:
            if char in node.child:
                if 1 < len(node.child):
                    time += 1
                    #print(char, 1)
                elif len(node.child) == 1 and (node.isEnd or node.name == "root"):
                    time += 1
                    #print(char, 2)
                    #print(node.name, node.parent)
                node = node.child[char]
            else:
                return "error"
        #print(word, time)
        return time

def solutions(wordlist, list_len):
    trie = Trie()
    for word in wordlist:
        trie.insert(word)
    return sum([trie.write_time(word) for word in wordlist]) / list_len

import sys
data = sys.stdin.readlines()
l = len(data)
i = 0
while i < l:
    n = int(data[i])
    wordlist = [str(d.strip()) for d in data[i+1:i+1+n]]
    print("{:.2f}".format(solutions(wordlist, n)))
    i += n+1
