# Complete the friendCircles function below.


def friendCircles(friends):
    # To determine number of friend circles need to determine number of unique connected components
    N = len(friends[0])
    visited = [0]* N
    result = 0
    for i in range(N):
        if visited[i] == 0: # we have found a new friend circle
            result += 1
            DFS(i, friends, N, visited)
    return result
    
def DFS(node, friends, N, visited):
    # Standard recursive implementation of DFS 
    if visited[node] == 1:
        return
    visited[node] = 1
    for i in range(N):
        if friends[node][i] == "Y":
            DFS(i, friends, N, visited)


# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#

def longestChain(words):
    # first we will sort list by length of strings
    words.sort(key=lambda x: len(x))
    lookup = {}
    chain_length = 0
    for word in words:
        lookup[word] = 1
        for i in range(len(word)):
            new_word = remove_character(word, i)
            if new_word in lookup: # check if modification results in a chain at all
                lookup[word] = max(lookup[word], 1 + lookup[new_word]) # check if new modification results in new max chain length
        chain_length = max(chain_length, lookup[word]) # update the max chain length
    return chain_length
                
                    
        
# helper function to remove a character at a desired index
def remove_character(word, index):
    return word[:index] + word[(index+1):]