
## 25/10/2022


print("""
      
      

                                                                    
888888888888  88                                                    
     88       ""                                                    
     88                                                             
     88       88  8b,dPPYba,   8b,dPPYba,    ,adPPYba,  8b,dPPYba,  
     88       88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
     88       88  88       d8  88       d8  8PP"""""""  88          
     88       88  88b,   ,a8"  88b,   ,a8"  "8b,   ,aa  88          
     88       88  88`YbbdP"'   88`YbbdP"'    `"Ybbd8"'  88          
                  88           88                                   
                  88           88        
      
      
      """)


print('Welcome to tip calculator')

bill = float(input("What was the total bill amount?\n$"))

tip = int(input('What percentage tip would you like to give? 10, 12 or 15\n'))
people = int(input('How many people to split the bill'))

Total = f"Each person have to pay ${(bill/people)*tip/100 + bill}"
print(Total)

