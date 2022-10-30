
## 30/10/2022


import random

wordList = ['eggs', 'apple', 'banana', 'watermelon','pineapple']  ## you can add more words here
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
    
    
## Game Logic

restart = True
while restart:
    
    

    print('\n')

    print(""" 
          
___  ___  ________  ________   ________  _____ ______   ________  ________      
|\  \|\  \|\   __  \|\   ___  \|\   ____\|\   _ \  _   \|\   __  \|\   ___  \    
\ \  \\\  \ \  \|\  \ \  \\ \  \ \  \___|\ \  \\\__\ \  \ \  \|\  \ \  \\ \  \   
 \ \   __  \ \   __  \ \  \\ \  \ \  \  __\ \  \\|__| \  \ \   __  \ \  \\ \  \  
  \ \  \ \  \ \  \ \  \ \  \\ \  \ \  \|\  \ \  \    \ \  \ \  \ \  \ \  \\ \  \ 
   \ \__\ \__\ \__\ \__\ \__\\ \__\ \_______\ \__\    \ \__\ \__\ \__\ \__\\ \__\
    \|__|\|__|\|__|\|__|\|__| \|__|\|_______|\|__|     \|__|\|__|\|__|\|__| \|__|
                                                             
                                                             
""")

    print('\n')


    chosenWord = random.choice(wordList)
    lives = 6 ## add more lives here

    display = []

    print('Do you want to enable hints?\nEnabling hints shows the random chosen word.\n')
    hint_1 = input('Do you wish to enable them? yes | no\n').lower()


    if hint_1 == 'yes':
        print(f'It is a {len(chosenWord)} letter word')
            
    for letter in chosenWord:
        display.append('_')
    print('\n')    
    print(f'Start guessing => {display}')
    print('\n')



    all_letters = False
    while not all_letters:
        
            guess = input('Guess a letter => ').lower()
            
            ## displaying letter per word

            for position in range(len(chosenWord)): 
                letter = chosenWord[position]
                if letter == guess:
                    display[position] = letter
                    print(display)

            ## player life logic
            
            if guess not in chosenWord:
                lives -= 1
                print('uh oh!! Wrong guess!\n')
                print(f"Current life: {lives}")
                print(stages[lives])
                if lives == 0:
                    all_letters = True
                    print('You have no more life left!')
                    print('You lost the game!!')
                else:
                    pass
            if lives ==4:
                hint_2 = input('Need more hints? yes | no\n').lower()
                if hint_2 =='yes':
                    print(f'The first word is {chosenWord[0]} and the last word is {chosenWord[-1]}')

            if lives == 0:
                hint_3 = input('Give up and show the word?\nThis takes all your current lives and you will lose instantly. yes | no\n').lower()
                if hint_3 =='yes':
                    print(f'The chosen word is {chosenWord}')
                    print('You lost the game!!')
                else:
                    print('Good Luck!!')

            ## player win logic
            
            if '_' not in display:
                all_letters = True
                print(f"The chosen word is => {display}")

    ## game restart logic
    Quit = input('Do you want to quit? yes| no\n').lower()
    if Quit == 'yes':
        restart = False
    else:
        pass
