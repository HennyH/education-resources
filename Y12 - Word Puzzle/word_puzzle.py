import unittest
from typing import Iterable, List
from itertools import combinations
from time import monotonic_ns

def find_all_words(letters: List[str], words_filename: str) -> Iterable[str]:
    """Find all the words which can be formed using any combination of the given letters."""
    # hint: use itertools.combination()
    pass

try:
    from word_puzzle_answers import find_all_words
except ImportError:
    pass

class TestFindAllWords(unittest.TestCase):
    def test_eggs(self):
        words = set(find_all_words(list("eggs"), "words.txt"))
        self.assertSetEqual(
            words,
            set(["es", "seg", "egg", "eggs"]))
    
    def test_difference(self):
        words = set(find_all_words(list("difference"), "words.txt"))
        self.assertSetEqual(
            words,
            set(['ne', 'feed', 'fern', 'de', 'fir', 'need', 'ree',
                 'fee', 'dine', 'ere', 'die', 'redefine', 'fine', 'ice',
                 'friend', 'defence', 'fend', 'iff', 'fired', 'cried', 'fen',
                 'fife', 'rin', 'fiend', 'riff', 'fierce', 'if', 'differ',
                 'nerd', 'deer', 're', 'freed', 'den', 'cider', 'dee', 'fer',
                 'rec', 'difference', 'en', 'define', 'fried', 'nice', 'ride',
                 'niece', 'dice', 'rife', 'fin', 'nicer', 'end', 'rid', 'free',
                 'cee', 'rice', 'find', 'decree', 'iced', 'fender', 'id', 'reed',
                 'in', 'diner', 'nee', 'eerie', 'reef', 'finder', 'er', 'dire',
                 'fined', 'creed', 'rein', 'cinder', 'feeder', 'fed', 'red', 'finer',
                 'refined', 'ed', 'fence', 'fire']))
    
    def test_execution_time(self):
        timings = []
        n_trials = 100
        max_avg_time = 5000000
        for _ in range(n_trials):
            start_time = monotonic_ns()
            _ = list(find_all_words(list("difference"), "words.txt"))
            end_time = monotonic_ns()
            timings.append(end_time - start_time)
        avg_time = sum(timings) / n_trials
        self.assertLess(avg_time, max_avg_time, f"Your function took an average of {avg_time}ns but it must execute in less than {max_avg_time}ns.")
