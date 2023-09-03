import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self,isEnd):
        self.isEnd = isEnd
        self.childNode = {}

class Trie():
    def __init__(self):
        self.parent = Node(None)
    
    def insert(self,string):
        now_node = self.parent
        temp_length = 0

        for char in string:
            if char not in now_node.childNode:
                now_node.childNode[char] = Node(char)
            
            temp_length += 1
            now_node = now_node.childNode[char]

            if temp_length == len(string):
                now_node.isEnd = True
    
    def search(self,string):
        now_node = self.parent
        temp_length = 0

        for char in string:
            if char in now_node.childNode:
                temp_length += 1
                now_node = now_node.childNode[char]

                if now_node.isEnd == True and temp_length == len(string):
                    return True
            else:
                return False
            
n,m = map(int,input().split())

trie = Trie()
for _ in range(n):
    word = input().strip()
    trie.insert(word)

answer = 0
for _ in range(m):
    word = input().strip()
    if trie.search(word):
        answer += 1

print(answer)