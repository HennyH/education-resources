from functools import lru_cache
from operator import itemgetter
from typing import List, Iterable, Dict, Tuple
from collections import Counter, defaultdict
from itertools import combinations

def get_word_key(word):
    return tuple(sorted(((l, n) for l, n in Counter(word).items()), key=itemgetter(0)))

@lru_cache(1)
def make_word_key_to_words_lookup(words_filename: str) -> Dict[Tuple[Tuple[str, int]], str]:
    word_key_to_words = defaultdict(set)
    with open(words_filename, "r") as words_fileobj:
        for line in words_fileobj:
            word = line.strip()
            word_key = get_word_key(word)
            word_key_to_words[word_key].add(word)
    return word_key_to_words

def find_all_words(letters: List[str], words_filename: str) -> Iterable[str]:
    """Find all the words which can be formed using the given letters."""
    word_key_to_words = make_word_key_to_words_lookup(words_filename)
    results = []
    for n_letters in range(1, len(letters) + 1):
        for letter_combination in combinations(letters, n_letters):
            word_key = get_word_key(letter_combination)
            if word_key in word_key_to_words:
                for word in word_key_to_words[word_key]:
                    results.append(word)
    return set(results)

# def too_slow_find_all_words(letters: List[str], words_filename: str) -> Iterable[str]:
#     words = []
#     with open(words_filename, "r") as words_fileobj:
#         for line in words_fileobj:
#             words.append(line.strip())
#     allowed_counts = Counter(letters)
#     for word in words:
#         word_counts = Counter(word)
#         if all(allowed_counts.get(l, 0) >= n for l, n in word_counts.items()):
#             yield word

# find_all_words = too_slow_find_all_words
