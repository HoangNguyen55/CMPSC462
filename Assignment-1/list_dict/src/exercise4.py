def word_frequencies(string):
    punctuation = [',', '.', ':', ';', '\'', '"']
    s = "".join(i for i in string if i not in punctuation)
    re = {}
    for i in s.split(" "):
        if re.get(i):
            re[i] += 1
        else:
            re[i] = 1
    return re

s = "Fred fed Ted bread, and Ted fed Fred bread"

print(word_frequencies(s))