def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    count_words(text)
    print()
    count_characters(text)
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



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()