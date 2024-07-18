def single_root_words(root_word,*other_words):
    same_words = []
    lower_words = []
    root_word = root_word.lower()
    for word_1 in other_words:
        word_1 = word_1.lower()
        lower_words.append(word_1)
    for word in lower_words:
        if root_word in word or word in root_word:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
