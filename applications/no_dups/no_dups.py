def no_dups(s):
    # Your code here
    out_string = ""
    if s == "":
        return ""
    else:
        split_string = s.split()
        out = {word:split_string.count(word) for word in split_string}
    for ind, words in enumerate(out.keys()):
        if ind == len(out.keys()) - 1:
            out_string += words
        else:
            out_string += f"{words} "
    return out_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))