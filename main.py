import sys
from stats import get_count_words, get_counts_characters

def get_book_txt(path_to_file):
    with open(path_to_file, 'r') as file:
        text = file.read()
    get_count_words(text)
    get_counts_characters(text)

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    path_to_file = sys.argv[1]

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path_to_file}...')
    return get_book_txt(path_to_file)

if __name__ == '__main__':
    main()