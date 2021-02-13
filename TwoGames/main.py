import os
from calculate import random_operation
from ahorcado import random_words, display

#random_num = random_operation(min_num,max_num)
#ahorcado = Ahorcado()

def iniciar():
    
    print('Hola, esto es el Juego de Leo')
    print()
    game_select = str(input('''
            ¿Qué quieres jugar?

            [C]alculate Random Nnumber
            [A]horcado
    '''))

    if game_select == 'C':
        run_calculate()
    if game_select == 'A':
        run_ahorcado()

# Secuencia de numero aleatorio --------------------------------------------------------------------------

def run_calculate():
        print('Hello!! This Game >>>>>  RANDOM NUMBER   <<<<')
        print()
        min_num = int(input('Add initial number:  '))
        max_num = int(input('Add final number:  '))
        print()
        print()
        print('calculate random number....')
        print()
        print()

        random_operation(min_num,max_num)

# Secuencia para el ahorcado --------------------------------------------------------------------------

def run_ahorcado():
        word = random_words()
        #category = category_name()
        '''
        if word in animals_words:
            category = 'The Category is ANIMALS and your word has {} letters'.format(len(word))
        elif word in country_words:
            category = 'The Category is COUNTRIES and your word has {} letters'.format(len(word))
        else:
            category = 'The Category is CLOTHES and your word has {} letters'.format(len(word))
        '''
        hidden_word = ['_'] * len(word)
        tries = 0
        letter_error = []
        
        while True:
            display(hidden_word,tries,letter_error,word)
            current_letter = str(input('Add one letter:  '))

            letter_indexes = []

            os.system('cls')
                        
            #for i in range(len(word)-1):
            for i in range(len(word)):
                if word[i] == current_letter:
                    letter_indexes.append(i)
        
            if len(letter_indexes) == 0:
                if current_letter in letter_error:
                    print('')
                    print('You used letter "{}", try other'.format(current_letter))
                    print('')
                else:
                    letter_error.append(current_letter)
                    tries += 1
            
                if tries == 7:
                    print('')
                    print('')
                    print(' XXXXX ----- GAME OVER  ------ XXXXX ')
                    print('The correct word is: {}'.format(word))
                    print('')
                    break
            else:
                for i in letter_indexes:
                    hidden_word[i] = current_letter

                letter_indexes = []    
          
            try:
                hidden_word.index('_')
            except ValueError:
                print('')
                print('')
                print('******** -----  Congratulations!! You Win  ------  *********')
                print('The Word is: {}'.format(word))
                print('')
                break        

if __name__ == '__main__':
    iniciar()