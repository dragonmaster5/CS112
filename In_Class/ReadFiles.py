
def frequentWords(sentence):
    d = {}
    l = sentence.split()
    for i in l:
        if i.lower() not in d:
            d[i.lower()] = 1
        else:
            d[i.lower()] = d[i.lower()] + 1
    l = []
    maxa = ("", 0)
    for word, count in d.items():
        l.append((word, count))
        if count > maxa[-1]:
            maxa = (word, count)
    for i in range(0, len(l)):
        temp = l.pop(0)
        if temp[-1] == maxa[-1]:
            l.append(temp[0])
    return l
with open("sampleText.txt", "rt") as file:
    content = str(file.read())
    print(frequentWords(content))
