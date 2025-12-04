def get_num_words(book_contents):
    words = book_contents.split()
    number_of_words = len(words)

    return number_of_words


def get_chars_dics(words):
    unique_character_count = {}
    for char in words:
        char = char.lower()
        does_character_exist = char in unique_character_count
        if does_character_exist:
            char_count = unique_character_count[char]
            char_count += 1
            unique_character_count[char] = char_count
        else:
            unique_character_count[char] = 1
    return unique_character_count


def sort_items(items):
    return items[1]


def sort_dictionary(character_dict):
    character_list = list(character_dict.items())
    character_list.sort(reverse=True, key=sort_items)
    return character_list
