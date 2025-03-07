# 01_LU_game

import random
import time

total_amount = 0

whole_code_loop = 0

amount_won = 0

items = ['zebra', 'horse', 'unicorn', 'MEGA JACKPOT', 'how']
chances = [0.475, 0.475, 0.0499, 0.000099999, 0.00000001]

loopy_questions1 = 0
loopy_questions2 = 0
loopy_questions3 = 0

print("Would you like to play a game?")
start = input("y/n: ")

start = start.lower()

if start == 'y' or start == 'yes':
    print("Hello, welcome to the gambling sector!")

    while loopy_questions1 != 1:
        
        total_amount = float(input("Enter amount from $1 to $10 for gamble: "))

        if total_amount == 1234567890:
            total_amount = 1000000000

        if total_amount < 1 or total_amount > 10 and not 1000000000:
            print(f"Cannot play game with ${total_amount}")
        
        elif total_amount == 1000000000 or total_amount > 0 or total_amount < 11:
            print(f'Alright lets start with {total_amount}')
            loopy_questions1 = 1
    

    while whole_code_loop != 1:
        while loopy_questions2 != 1:
            
            token = float(input('How many token would you like to buy? '))
            if token > total_amount:
                print(f'Not enough money to buy {token} tokens')
            elif token <= 0:
                print('Buy tokens to start')
            else:
                loopy_questions2 = 1
        
        total_amount -= token
        print(f'Rolling {token}')
        
        rolling = 0
        while rolling != 1:
            if token > 0:
                token -= 1
                random_item = random.choices(items, chances)
                
                print(f'You got {random_item}')
                if random_item == ['zebra']:
                    amount_won += 0.5
                    
                elif random_item == ['horse']:
                    amount_won += 0.5
                    
                elif random_item == ['unicorn']:
                    amount_won += 5
                elif random_item == ['MEGA JACKPOT']:
                    amount_won += 1000000
                elif random_item == ['how']:
                    amount_won += 1.7976931348623157e+308

            else:
                rolling = 1
        whole_code_loop = 1

        total_amount = total_amount + amount_won  

        print(f'You won ${amount_won}')      
        amount_won = 0
        print(f'Your total is ${total_amount}')
        
        if total_amount > 0.5:

            loopy_questions3 = 0

            while loopy_questions3 != 1:
                again = input('Would you like to roll again? ')
                
                again = again.lower()
                
                if again == 'n' or again == 'no':
                    loopy_questions3 = 1
                    whole_code_loop = 1
                    print(f'Your final total money is ${total_amount}')
                    end = input('End game? ')
                    end = end.lower()
                    if end == 'yes' or end == 'y':
                        print('Bye')
                        time.sleep(1)
                        
                    else:
                        print('Nuh uh')
                        time.sleep(1)

                elif again == 'y' or again == 'yes':
                    loopy_questions3 = 1
                    whole_code_loop = 0
                    loopy_questions2 = 0
                    rolling = 0
                else:
                    loopy_questions3 = 0


                

        else:
            print('Cannot play anymore')
            print(f'Your final total money is ${total_amount}')
            whole_code_loop = 1
            end = input('End game? ')
            end = end.lower()
            if end == 'yes' or end == 'y':
                print('Bye')
                time.sleep(1)

            else:
                print('Nuh uh')
                time.sleep(1)

else:
    print('ok')