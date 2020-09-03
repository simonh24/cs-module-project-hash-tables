# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open('c:/Users/defaultuser/Desktop/Lambda/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt') as f:
    text = f.read()

frequency = ('E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z')

count = {}
key = {}

decoded_message = ""

ignore = ",.<>?;:'\"/\\|[]{}~!@#$%^&*()-+= \n”â€1234567890"

for char in text:
    if char not in ignore:
        if char not in count:
            count[char] = 0
        count[char] += 1

count = sorted(count.items(), key=lambda x: x[1], reverse=True)

for i in range(len(frequency)):
    key[count[i][0]] = frequency[i]

for char in text:
    if char in key:
        decoded_message += key[char]
    else:
        decoded_message += char
print(decoded_message)