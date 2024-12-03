def single_root_words(root_word, *other_words):
    same_words = []
    for x in other_words:
        if root_word.lower() in x.lower() or x.lower() in root_word.lower():
            same_words.append(x)
    return same_words
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))