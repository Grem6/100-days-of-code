
## 26/10/2022

print

("""
      
      
      
______               _    _       _____         _               _         _                
|  _  \             | |  | |     /  __ \       | |             | |       | |               
| | | |  ___   __ _ | |_ | |__   | /  \/  __ _ | |  ___  _   _ | |  __ _ | |_   ___   _ __ 
| | | | / _ \ / _` || __|| '_ \  | |     / _` || | / __|| | | || | / _` || __| / _ \ | '__|
| |/ / |  __/| (_| || |_ | | | | | \__/\| (_| || || (__ | |_| || || (_| || |_ | (_) || |   
|___/   \___| \__,_| \__||_| |_|  \____/ \__,_||_| \___| \__,_||_| \__,_| \__| \___/ |_|   
                                                                                           
                                                                                           
                                                                                           
""")
print("\n")
inputAge = int(input('What is your current age?\n'))

years_remaining = 90-inputAge
daysRemaining = years_remaining*365
weeksRemaining = years_remaining*52
monthsRemaining = years_remaining*12

reamainingTime = f"You have {monthsRemaining} months, {weeksRemaining} weeks and {daysRemaining} days remaining"

print(reamainingTime)