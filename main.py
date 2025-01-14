def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_num_char(text)
    sorted_dict = dict(sort_list(character_count))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")

    for i in sorted_dict:
        print(f"The {i} character was found {sorted_dict[i]} times")

    print("--- End report ---")


def sort_list(dict):
    sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_dict


def count_num_char(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        elif char.isalpha():
            char_count[char] = 1

    return char_count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()