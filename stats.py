def get_num_words(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    with open(book) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"Found {num_words} total words")

def letter_appearances(book):
    dict = {}
    with open(book) as f:
        file_contents = f.read()
        array_of_letters = list(file_contents)
        for letter in array_of_letters:
            letter_in_q = letter.lower()
            if letter_in_q in dict:
                dict[letter_in_q] += 1
            elif letter_in_q not in dict:
                dict[letter_in_q] = 1
    return dict

def helper_get_value(dict):
    return list(dict.values())[0]

def sorted_char_list(dict):
    char_list = []
    for keypair in dict:
        if keypair.isalpha():
            char_list.append({keypair: dict[keypair]})
    char_list.sort(reverse=True, key=helper_get_value)
    print("--------- Character Count -------")
    for char_dict in char_list:
        char = list(char_dict.keys())[0]
        count = list(char_dict.values())[0]
        print(f"{char}: {count}")
    print("============= END ===============")