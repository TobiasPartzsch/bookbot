import operator


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    chars: dict[str, int] = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(num_chars_dict.items(), key=operator.itemgetter(1), reverse=True)
