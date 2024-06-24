def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words(text)
    count_characters(text)

def count_words(book_contents):
    words = book_contents.split()
    print(f"Word count of book: {len(words)}")

def count_characters(book_contents):
    character_count = dict()
    for character in book_contents:
        lowered = character.lower()
        if character in character_count.keys():
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1
    print(f"Character count, by character, of book: {character_count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()