def all_variants(text):
    for n in range(1, len(text) + 1):
        for i in range(len(text) - n + 1):
            yield text[i:i + n]


a = all_variants("abcde")
for i in a:
    print(i)
