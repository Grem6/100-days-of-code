print("""
      
8888888b.                   888                                     
888   Y88b                  888                                     
888    888                  888                                     
888   d88P .d88b.   .d8888b 888  888                                
8888888P" d88""88b d88P"    888 .88P                                
888 T88b  888  888 888      888888K                                 
888  T88b Y88..88P Y88b.    888 "88b                                
888   T88b "Y88P"   "Y8888P 888  888                                
                                                                    
                                                                    
                                                                    
8888888b.                                                           
888   Y88b                                                          
888    888                                                          
888   d88P 8888b.  88888b.   .d88b.  888d888                        
8888888P"     "88b 888 "88b d8P  Y8b 888P"                          
888       .d888888 888  888 88888888 888                            
888       888  888 888 d88P Y8b.     888                            
888       "Y888888 88888P"   "Y8888  888                            
                   888                                              
                   888                                              
                   888                                              
 .d8888b.           d8b                                             
d88P  Y88b          Y8P                                             
Y88b.                                                               
 "Y888b.    .d8888b 888 .d8888b  .d8888b   .d88b.  888d888 .d8888b  
    "Y88b. d88P"    888 88K      88K      d88""88b 888P"   88K      
      "888 888      888 "Y8888b. "Y8888b. 888  888 888     "Y8888b. 
Y88b  d88P Y88b.    888      X88      X88 Y88..88P 888          X88 
 "Y8888P"   "Y8888P 888  88888P'  88888P'  "Y88P"  888      88888P' 
                                                                                                                          
      
      """)


import random as random

Start =True
while Start:
     player = int(input('what do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors \n'))
     
     rock = '''
     _______
     ---'   ____)
          (_____)
          (_____)
          (____)
     ---.__(___)
     '''

     paper = '''
     _______
     ---'   ____)____
               ______)
               _______)
          _______)
     ---.__________)
     '''

     scissors = '''
     _______
     ---'   ____)____
               ______)
          __________)
          (____)
     ---.__(___)
     '''

     game =[rock, paper, scissors]


     if player >= 3 or player <0:
          print('Not a valid option')
          
     else:
          print(f'You chose ==> {game[player]}')
          print('\n')
          
          
          computer = random.randint(0,2)
          print(f'Computer chose ==> {game[computer]}')
          print('\n')
               
               
               
          if player == 0 and computer ==2:
               print('You win!')
          elif player == 2 and computer ==0:
               print('You lost!')
          elif computer > player:
               print('you lost')
          elif player > computer:
               print('you won')
          elif computer == player:
               print('Match Draw')
               
     Quit = input('Do yoy want to quit?\n')
     if Quit.lower()=='yes':
          Start = False
     
