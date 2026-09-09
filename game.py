import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])
dictionary = {'rock': 0, 'paper': 1, 'scissors': 2}
choose = input("Enter your choice (rock, paper, scissors): ").lower()
if choose not in dictionary:
    print("Invalid choice. Please choose rock, paper, or scissors.")    
elif choose == computer_choice:
    print("Both players selected {choose}. It's a tie!")
elif choose == 'rock' and computer_choice == 'scissors':
    print("Rock smashes scissors! You win!")
elif choose == 'paper' and computer_choice == 'rock':
    print("Paper covers rock! You win!")
elif choose == 'scissors' and computer_choice == 'paper':
    print("Scissors cuts paper! You win!")
elif choose == 'papper' and computer_choice =='scissors':
    print("computer win!")
elif computer_choice == 'rock' and choose == 'scissors':
    print("computer win!")
elif computer_choice == 'paper' and choose == 'rock':
    print("computer win!")
else :
    print("game is over")


          