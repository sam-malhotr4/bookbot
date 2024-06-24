def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    count_words(text)
    print()
    print_alphabet_occurences_asc(count_characters(text))
    print("--- End report ---")

def count_words(book_contents):
    words = book_contents.split()
    print(f"{len(words)} words found in the document")

def count_characters(book_contents):
    character_count = dict()
    for character in book_contents:
        lowered = character.lower()
        if character in character_count.keys():
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def print_alphabet_occurences_asc(character_count_dict):
    alphabet_occur_list = []
    for key in character_count_dict.keys():
        if key.isalpha() and len(key) == 1:
            alphabet_occur_list.append({"character":key, "num": character_count_dict[key]})
    alphabet_occur_list.sort(reverse=True, key=sort_on)
    for alph_occ in alphabet_occur_list:
        print(f"The '{alph_occ.character}' character was found {alph_occ.num} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()