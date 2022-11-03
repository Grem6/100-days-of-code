
## 29/10/2022

logo = """   

            
    ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
    `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
            ""             88                                 
                            88                                 
    ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
    `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                88                                             
                88 
                
                            
    """
restart = True

while restart:
    
    print(logo)


    alpahabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    decision = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    text = input("Type the message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def encrypt(text, shift):
        cipher = ""
        for letter in text:
            if letter in alpahabet:
                index = alpahabet.index(letter)
                word = alpahabet[index + shift]
                cipher += word
        print(cipher)


    def decrypt(text, shift):
        decipher =''
        for letter in text:
            if letter in alpahabet:
                index = alpahabet.index(letter)
                word =alpahabet[index - shift]
                decipher += word
        print(decipher)
        

    if decision == 'encode':
        encrypt(text, shift)
    else:
        decrypt(text, shift)

    Quit = input("Do you want to quit? yes | no \n").lower()
    if Quit == 'yes':
        restart = False
    else:
        continue
