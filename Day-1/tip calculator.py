print('Welcome to tip calculator')

bill = float(input("What was the total bill amount?\n$"))

tip = int(input('What percentage tip would you like to give? 10, 12 or 15\n'))
people = int(input('How many people to split the bill'))

Total = f"Each person have to pay ${(bill/people)*tip/100 + bill}"
print(Total)