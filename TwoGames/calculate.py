
import random
  
def random_operation(min_num,max_num):
    random_num = random.randint(min_num, max_num)
    number_found = True  

    while number_found:
        user_num = int(input('Your turn, add number:  '))
        print()

        if user_num == random_num:
            print('Good!! You Find Number')
            print()
            number_found = False

        elif user_num < min_num or user_num > max_num:
            print('No, The values is out range') 
                    
        elif user_num > random_num:
            print('No, The value is more little than ' + str(user_num))
        
        elif user_num < random_num:
            print('No, The value is more bigger than '+ str(user_num))

    

    
    