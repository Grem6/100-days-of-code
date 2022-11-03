
## 1/11/2022

NATO = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike",
        "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}




print("""
                                                                                                  
NNNNNNNN        NNNNNNNN               AAA         TTTTTTTTTTTTTTTTTTTTTTT     OOOOOOOOO     
N:::::::N       N::::::N              A:::A        T:::::::::::::::::::::T   OO:::::::::OO   
N::::::::N      N::::::N             A:::::A       T:::::::::::::::::::::T OO:::::::::::::OO 
N:::::::::N     N::::::N            A:::::::A      T:::::TT:::::::TT:::::TO:::::::OOO:::::::O
N::::::::::N    N::::::N           A:::::::::A     TTTTTT  T:::::T  TTTTTTO::::::O   O::::::O
N:::::::::::N   N::::::N          A:::::A:::::A            T:::::T        O:::::O     O:::::O
N:::::::N::::N  N::::::N         A:::::A A:::::A           T:::::T        O:::::O     O:::::O
N::::::N N::::N N::::::N        A:::::A   A:::::A          T:::::T        O:::::O     O:::::O
N::::::N  N::::N:::::::N       A:::::A     A:::::A         T:::::T        O:::::O     O:::::O
N::::::N   N:::::::::::N      A:::::AAAAAAAAA:::::A        T:::::T        O:::::O     O:::::O
N::::::N    N::::::::::N     A:::::::::::::::::::::A       T:::::T        O:::::O     O:::::O
N::::::N     N:::::::::N    A:::::AAAAAAAAAAAAA:::::A      T:::::T        O::::::O   O::::::O
N::::::N      N::::::::N   A:::::A             A:::::A   TT:::::::TT      O:::::::OOO:::::::O
N::::::N       N:::::::N  A:::::A               A:::::A  T:::::::::T       OO:::::::::::::OO 
N::::::N        N::::::N A:::::A                 A:::::A T:::::::::T         OO:::::::::OO   
NNNNNNNN         NNNNNNNAAAAAAA                   AAAAAAATTTTTTTTTTT           OOOOOOOOO     
                                                                                        
      
""")


restart = True

while restart:
    print('\n')
    userName = input("Enter your name: \n").upper()
    print('\n')
    print('Your NATO call is:\n')
    for letter in userName:
        NatoCall = NATO[letter]
        print(NatoCall, end=',')
    print('\n')
    quit = input('Do you want to quit? yes | no\n').lower()
    if quit == 'yes':
        restart = False
    else:
        continue
