import random
win_conditions = {'paper': ['scissors', 'fire', 'snake', 'human', 'tree', 'wolf', 'sponge'],\
                  'scissors': ['rock', 'fire', "water", "dragon", "devil", "lightning", "gun"],\
                  'rock': ['paper', "air", "water", "dragon", "devil", "lightning", "gun"],\
                  'gun': ['sponge', 'paper', "air", "water", "dragon", "devil", "lightning"],\
                  'lightning': ['wolf', 'sponge', 'paper', "air", "water", "dragon", "devil"],\
                  'devil': ['tree', 'wolf', 'sponge', 'paper', "air", "water", "dragon"],\
                  'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', "air", "water"],\
                  'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', "air"],\
                  'air': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],\
                  'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],\
                  'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],\
                  'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],\
                  'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],\
                  "snake": ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],\
                  'fire': ['water', 'air', 'dragon', 'devil', 'lightning', 'gun', 'rock']}
lose_conditions = {'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],\
                   'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],\
                   'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],\
                   'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],\
                   'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],\
                   'air': ['rock', 'fire', "water", "dragon", "devil", "lightning", "gun"],\
                   'paper': ['water', 'air', 'dragon', 'devil', 'lightning', 'gun', 'rock'],\
                   'sponge': ['paper', "air", "water", "dragon", "devil", "lightning", "gun"],\
                   'wolf': ['sponge', 'paper', "air", "water", "dragon", "devil", "lightning"],\
                   'tree': ['wolf', 'sponge', 'paper', "air", "water", "dragon", "devil"],\
                   'human': ['tree', 'wolf', 'sponge', 'paper', "air", "water", "dragon"],\
                   'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', "air", "water"],\
                   'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', "air"],\
                   'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],\
                   'rock': ['scissors', 'fire', 'snake', 'human', 'tree', 'wolf', 'sponge']}
variants = []
name = input('Enter your name: ')
print(f'Hello, {name}')
var = input()
if var:
    variants = var.split(',')
else:
    variants = ['rock', 'paper', 'scissors']
print("Okay, let's start")
score = open('rating.txt', 'r')
score_list = []
rating = 0
for line in score:
    score_list.append(line.split())
for i in range(len(score_list)):
    if name in score_list[i]:
        rating = int(score_list[i][1])
while True:
    choice = input()
    computer_choice = random.choice(variants)
    if choice in lose_conditions[computer_choice]:
        print(f'Sorry, but the computer chose {computer_choice}')
    elif choice in win_conditions[computer_choice]:
        print(f'Well done. The computer chose {computer_choice} and failed')
        rating += 100
    elif choice == computer_choice:
        print(f'There is a draw ({choice})')
        rating += 50
    elif choice == '!rating':
        print(f'Your rating: {rating}')
    elif choice == '!exit':
        print('Bye!')
        break
    else:
        print('Invalid input')
