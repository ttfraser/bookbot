import sys
from stats import (
    get_book_len,
    get_book_char,
    sort_dictionary,
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        word_count = get_book_len(book)
        book_chars = sort_dictionary(get_book_char(book))
        print(f"============ BOOKBOT ============\nAnalyzing book found at {book}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
        for a in book_chars:
            if a["char"].isalpha() == True:
                print(f"{a["char"]}: {a["num"]}")
        print("============= END ===============")
main()