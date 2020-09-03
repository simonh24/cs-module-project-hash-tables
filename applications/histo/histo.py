# Your code here
with open('c:/Users/defaultuser/Desktop/Lambda/cs-module-project-hash-tables/applications/histo/robin.txt') as f:
    text = f.read()

def word_count(s):
    out = {}
    s = s.lower()
    trimmed = s.replace("\"", "").replace(":", "").replace(";", "").replace(",", "").replace(".", "").replace("-", "").replace("+", "").replace("=", "").replace("/", "").replace("\\", "").replace("|", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("(", "").replace(")", "").replace("*", "").replace("^", "").replace("&", "")
    if trimmed == "":
        return {}
    else:
        split_string = trimmed.split()
        for word in split_string:
            if word not in out:
                out[word] = 1
            else:
                out[word] += 1
    return out

text_dict = word_count(text)
sorted_dict = sorted(text_dict.items(), key=lambda x: x[1], reverse=True)

max_spaces = 15
for i in sorted_dict:
    print(f"{i[0]}", end="")
    for j in range(max_spaces - len(i[0])):
        print(" ", end="")
    for k in range(i[1]):
        print("#", end="")
    print("")