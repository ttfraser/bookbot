def get_book_text(filepath):
    f = open(filepath)
    return f.read()

def get_book_len(filepath):
    book_text = get_book_text(filepath)
    return len(book_text.split())

def get_book_char(filepath):
    book_text = get_book_text(filepath).lower()
    char_set = set(book_text)
    char_count = dict.fromkeys(char_set, 0)
    for char1 in char_set:
        for char2 in book_text:
            if char1 == char2:
                char_count[char1] += 1
    return char_count

def sort_dictionary(dictionary):
    dictlist = []
    char_nums = dictionary.items()
    for char, num in char_nums:
        dictlist.append({"char": char, "num": num})
    sorted_dictlist = sorted(dictlist, key=lambda x: x['num'], reverse=True)
    return sorted_dictlist