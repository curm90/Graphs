from util import Queue

# Build your graph
# Do a BFS from start word to end word

# Load word list
f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    '''Return all word from word_list that are one letter different '''
    # Change one letter to another letter in the alphabet incrementally
    # Search the graph for that
    # Then reqpeat for each in the word
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    neighbors = []
    # For each letter in the word
    for i in range(len(word)):
        # For each letter in the alphabet
        for letter in alphabet:
            # Change the word letter to the alphabet letter
            list_word = list(word)
            list_word[i] = letter
            w = "".join(list_word)
            # If the new word is in the word_set
            if w != word and w in word_set:
                # Add it to neighbors
                neighbors.append(w)
    return neighbors


def find_ladders(begin_word, end_word):
    # Create a queue
    qq = Queue()
    # Enqueue a path to the starting word
    qq.enqueue([begin_word])
    # Create a visited set
    visited = set()
    # While the queue is not empty
    while qq.size() > 0:
        # Dequeue the next path
        path = qq.dequeue()
        # Grab the last word from the path
        v = path[-1]
        # If its not been visited
        if v not in visited:
            # Check if the word is our end word, if true return path
            if v == end_word:
                return path
            # Mark as visited
            visited.add(v)
            # Enqueue a path to each neighbor
            for neighbor in get_neighbors(v):
                path_copy = path[:]
                path_copy.append(neighbor)
                qq.enqueue(path_copy)


print(find_ladders('happy', 'hungry'))
