import sys
from stats import get_num_words, letter_appearances, sorted_char_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_num_words(sys.argv[1])
        letter_dict = letter_appearances(sys.argv[1])
        sorted_char_list(letter_dict)
main()
