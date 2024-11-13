class TrieNode():
    def __init__(self):
        self.children = {} #empty node
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        #initialized an empty root
    def addWord(self, word: str) -> None:
        curr = self.root #initialize to root
        for c in word:
            if c not in curr.children: #check if character is a child of node
                curr.children[c] = TrieNode() #add a new trie node as a children of prefixes
            #else if it is iterate more 
            curr = curr.children[c] #go to next node in trie
        curr.isWord = True #at the end make it a word.

    def search(self, word: str) -> bool:
        #run recursive function 
        def dfs(j,root):
            curr = root #set to root node

            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    #match all child nodes
                    for child in curr.children.values():
                        #recursively search for a solution
                        if dfs(i+1,child): #if one of the pathes is valid then return true
                            return True
                    return False 

                else:
                    #if prefix node found return false
                    if c not in curr.children:
                        return False
                    #else continue iterating
                    curr = curr.children[c] #go to next node
            #after iterating on every character if last character is a a word return it
            return curr.isWord
        return dfs(0,self.root)
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)