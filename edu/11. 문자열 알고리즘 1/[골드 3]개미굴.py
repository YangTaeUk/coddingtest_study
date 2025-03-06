class TrieNode:
    def __init__(self, parent="root", name="root", count=0, isEndOfWord=False):
        self.parent = parent
        self.name = name
        self.children = {}
        self.count = count
        self.isEndOfWord = isEndOfWord

    def node_print(self):
        st = ""
        for _ in range(self.count - 1 ):
            st += "--"
        if self.name != "root":
            print(st + self.name)

        child_list = sorted(list(self.children.keys()))
        for child in child_list:
            self.children[child].node_print()


class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, wordlist):
        node = self.node
        for word in wordlist:
            if word not in node.children:
                node.children[word] = TrieNode(parent=node.name,name=word,count=node.count + 1)
            node = node.children[word]
        node.isEndOfWord = True

    def node_print(self):
        self.node.node_print()


import sys

data = sys.stdin.readlines()
n = int(data[0])
main = Trie()
for i in range(n):
    row = data[i+1].split()
    cnt = int(row[0])
    ch = list(map(str, row[1:]))
    main.insert(ch)

main.node_print()

