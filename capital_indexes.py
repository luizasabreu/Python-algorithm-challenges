def capital_indexes(word):
    result = []
    for i in range (len(word)):
        if word[i].isupper():
            result.append(i)

    return result

print(capital_indexes('HeLlO'))
