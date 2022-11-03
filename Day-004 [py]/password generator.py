
## 28/10/2022

print("""
      
8888888b.                                                               888  
888   Y88b                                                              888  
888    888                                                              888  
888   d88P 8888b.  .d8888b  .d8888b  888  888  888  .d88b.  888d888 .d88888  
8888888P"     "88b 88K      88K      888  888  888 d88""88b 888P"  d88" 888  
888       .d888888 "Y8888b. "Y8888b. 888  888  888 888  888 888    888  888  
888       888  888      X88      X88 Y88b 888 d88P Y88..88P 888    Y88b 888  
888       "Y888888  88888P'  88888P'  "Y8888888P"   "Y88P"  888     "Y88888  
                                                                             
                                                                             
                                                                             
 .d8888b.                                             888                    
d88P  Y88b                                            888                    
888    888                                            888                    
888         .d88b.  88888b.   .d88b.  888d888 8888b.  888888 .d88b.  888d888 
888  88888 d8P  Y8b 888 "88b d8P  Y8b 888P"      "88b 888   d88""88b 888P"   
888    888 88888888 888  888 88888888 888    .d888888 888   888  888 888     
Y88b  d88P Y8b.     888  888 Y8b.     888    888  888 Y88b. Y88..88P 888     
 "Y8888P88  "Y8888  888  888  "Y8888  888    "Y888888  "Y888 "Y88P"  888     
                                                                              
      
      """)




import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []

for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''
for char in password_list:
    password += char
print(password)
