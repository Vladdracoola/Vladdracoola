import itertools


def all_variants(text):
    for lenght in range(1, len(text) + 1):
        for combintation in itertools.combinations(text, lenght):
            yield ''.join(combintation)


a = all_variants("abc")
for i in a:
    print(i)
