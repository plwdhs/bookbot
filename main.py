import sys

from stats import get_chars_dics, get_num_words, sort_dictionary


def get_book_text(book_filepath):
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    with open(book_filepath) as book:
        book_contents = book.read()

    number_of_words = get_num_words(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")

    unique_character_dict = get_chars_dics(book_contents)

    sorted_dict = sort_dictionary(unique_character_dict)
    print("--------- Character Count -------")
    for character, amount in sorted_dict:
        if character.isalpha():
            print(f"{character}: {amount}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_book_text(sys.argv[1])


main()
