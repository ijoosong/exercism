def word_count(sentence):
    #counting words
    words = sentence.split()
    uniq_words = set(words)
    word_dict = {}
    for word in uniq_words:
        word_dict.update({word: 0})
    for word in words:
        if word in word_dict:
            word_dict[word]=word_dict[word] + 1

    return word_dict

