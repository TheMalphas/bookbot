
def get_count_words(text):
    words = text.split()
    print('----------- Word Count ----------')
    print(f'Found {len(words)} total words')

def get_counts_characters(text):

    characters =  {}

    for word in text.split():
        for char in word.lower():
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1

    print('--------- Character Count -------')

    sorted_characters(characters)

def sorted_characters(characters):
    list_characters = []

    def sort_on(item):
        return item['num']

    for char in characters:
        list_characters.append(
            {
                'name': char,
                'num': characters[char]
                }
            )

    list_characters.sort(reverse=True, key=sort_on)

    for char in list_characters:
        if char['name'].isalpha():
            print(f'{char["name"]}: {char["num"]}')