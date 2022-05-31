import sys
input = sys.stdin.readline


class TrieNode:

    def __init__(self, level):
        self.children = {}
        self.level = level


class Trie:

    def __init__(self):
        self.root = TrieNode(0)

    def insert(self, word):
        cur = self.root

        for lvl, c in enumerate(word):
            if c not in cur.children:
                cur.children[c] = TrieNode(lvl)
                print('--'*lvl + c)
            cur = cur.children[c]


N= int(input())
words = []
for _ in range(N):
    K, *word = input().split()
    words.append(word)

words.sort()
antHouse = Trie()
for word in words:
    antHouse.insert(word)