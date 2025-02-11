"""
Trie는 문자열이나 연관된 데이터를 효율적으로 저장하고 검색하기 위한 트리기반의 자료구조이다.
Prefix Tree "접두사 트리" 라고도 불리며, 문자열의 검색과 연산이 효율적.
특히 자동완성, 사전검색, 와일드 카등 검색등에 자주 사용된다.

노드(node)
각 node들은 특정 문자/데이터단위 를 저장한다.
하위 노드들은 연결된 다른 문자/데이터 노드들을 저장한다.
종결표시(isEndOftheWord)해당 노드에서 단어가 끝나는지여부를 확인 가능

루트 Root : 시작노드, 빈문자열 표기도 병행한다.
경로 Path : 루트에서 노드로가능 하나의 문자열을 나타낸다.

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count=0
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.isEndOfWord = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True