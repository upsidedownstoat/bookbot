import sys
from stats import get_word_count, get_char_frequency, sort_char_frequency

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = read_text_file(file_path)
    
    total_word_count = get_word_count(book_text)
    char_frequency = get_char_frequency(book_text)
    sorted_frequency = sort_char_frequency(char_frequency)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_word_count} total words")
    print("--------- Character Count -------")
    
    for char, count in sorted_frequency.items():
        if char.isalpha() or char in ['æ', 'â', 'ê', 'ë', 'ô']:  # include accented chars
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
