def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)
        count_characters(file_contents)
    print() 

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

main()