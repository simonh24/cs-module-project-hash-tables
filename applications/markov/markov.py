import random

# Read in all the words in one go
with open('c:/Users/defaultuser/Desktop/Lambda/cs-module-project-hash-tables/applications/markov/input.txt') as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

split_words = words.split()
cache = {}

for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in cache:
        cache[word] = [next_word]

    else:
        cache[word].append(next_word)

start_words = []
for key in cache.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)

# TODO: construct 5 random sentences
# Your code here

for _ in range(5):
    stopped = False

    stop_signs = ".?!"

    while not stopped:
        print(word, end=' ')

        if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
            stopped = True

        following_words = cache[word]
        word = random.choice(following_words)
    print(" ")