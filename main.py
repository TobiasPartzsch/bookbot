import sys

from stats import get_book_text, count_letters_without_case, sort_by_count


def main():
    # input checks
    argv = sys.argv
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = argv[1]
    txt_body = get_book_text(book_path)
    num_words = len(txt_body.split())
    # print(f"{num_words} words found in the document")
    letter_count = count_letters_without_case(txt_body)
    # print(f"{letter_count}")
    letter_by_count = sort_by_count(letter_count)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{'\n'.join(f"{l[0]}: {l[1]}" for l in letter_by_count if l[0].isalpha())}
============= END ===============""")

main()