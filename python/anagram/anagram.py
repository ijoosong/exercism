from collections import Counter

def detect_anagrams(match, input):
    """for given word match, see if anagram exists in input."""
    d = {}
    li = []
    matching = Counter(match.lower())
    for word in input:
        d = {word: Counter(word.lower())}
        if d[word] == matching and word.lower() != match.lower():
            li.append(word)
    return li

def is_anagram(original, candidate):
    original, candidate = original.lower(), candidate.lower()
    return original != candidate and Counter(original) == Counter(candidate)

def detect_anagrams(match, word_list):
    return [word for word in word_list if is_anagram(match, word)]
