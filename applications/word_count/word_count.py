def word_count(s):
    # Your code here
    out = {}
    s = s.lower()
    trimmed = s.replace("\"", "").replace(":", "").replace(";", "").replace(",", "").replace(".", "").replace("-", "").replace("+", "").replace("=", "").replace("/", "").replace("\\", "").replace("|", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("(", "").replace(")", "").replace("*", "").replace("^", "").replace("&", "")
    if trimmed == "":
        return {}
    else:
        split_string = trimmed.split()
        out = {word:split_string.count(word) for word in split_string}
    return out

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))