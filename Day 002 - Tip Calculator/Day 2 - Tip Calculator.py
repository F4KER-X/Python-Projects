print('Welcome to the tip calculator.')
amount = float(input('What was teh total bill? $'))
tip = int(input('What percentage tip would you like to give? 10,12, or 15? '))
people = int(input('How many people to split the bill? '))
total_amount_per_person = round((amount * (1+(tip/100))) / people, 2)
print(f'Each person should pay: {total_amount_per_person:.2f}')
