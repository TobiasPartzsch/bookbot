from collections import defaultdict, Counter

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_letters_without_case(txt):
    counter = Counter(txt.lower())
    return dict(counter)

def sort_by_count(counter, reverse=True):
    return sorted(counter.items(), key=lambda item: item[1], reverse=reverse)
