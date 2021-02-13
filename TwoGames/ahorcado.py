import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

category_words = [1,2,3]

animals_words = [
    'lion',
    'dog',
    'cat',
    'elephant',
    'tiger'
]
country_words = [
    'brazil',
    'germany',
    'canada',
    'spain',
    'france'
]
clothes_words = [
    'short',
    'hat',
    'pants',
    'tie',
    'shoes'
]

def random_words():
    idx_category = random.randint(0, len(category_words) - 1)
    
    if idx_category == 1:
        idx = random.randint(0, len(animals_words) - 1)
        word = animals_words[idx]
        #category = 'The Category is ANIMALS and your word has {} letters'.format(len(word))
        #category_name('Animals')
        return animals_words[idx]

    elif idx_category == 2:
        idx = random.randint(0, len(country_words) - 1)
        word = country_words[idx]
        #category = 'The Category is COUNTRIES and your word has {} letters'.format(len(word))
        #category_name('Countries')
        return country_words[idx]

    else:
        idx = random.randint(0, len(clothes_words) - 1)
        word = clothes_words[idx]
        #category = 'The Category is CLOTHES and your word has {} letters'.format(len(word))
        #category_name('Clothes')
        return clothes_words[idx]

    
def display(hidden_word,tries,letter_error,word):
        
    #print(category)
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('__ __ __ __ __ __ __ __ __ __ __ __ __ __')
    print('')
    print("You can't use this letter: {}".format(letter_error))
    print('')

      
                           


    