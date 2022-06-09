import random
lst = ['Rock','Scissor','Paper']
while True:
    user_count = 0
    com_count = 0
    user = int(input('''Game start
                        1. Yes
                        2. No
                        '''))


    if user == 1:
        for a in range(1,6):
            user_input = int(input('''Enter your choice:-
                                       1. Rock
                                       2. Scissor
                                       3. Paper
                                       '''))
            if user_input ==1:
                user_choice = 'Rock'
            elif user_input ==2:
                user_choice = 'Scissor'
            elif user_input ==3:
                user_choice ='Paper'

            com = random.choice(lst)
            print("Computer",com)
            print("user ", user_choice)

            if com == user_choice:
                print("Game draw")
                com_count +=1
                user_count +=1

            elif  (user_choice == 'Paper' and com == '"Rock') or (user_choice == "Scissor" and com == "Paper"):
                print("You win")
                user_count +=1

            else:
                print("Computer Win")
                com_count +=1
    else:
        break