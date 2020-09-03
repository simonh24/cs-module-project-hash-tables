def word_count(s):
    # Your code here
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

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))