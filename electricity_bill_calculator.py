bill = 'LearnFactory Electricity Bill for November 2024'
tenant_name = input('Enter your name: ')
number_of_units = float(input('Enter the number of units consumed: '))

if number_of_units < 0:
    print(f'Hi, {tenant_name}.\n{number_of_units} is invalid!')

elif number_of_units <= 100:
    unit_cost = 0.50 * number_of_units
    print(f'Your unit cost is ${unit_cost}')

elif number_of_units >100 and number_of_units <=300:
    unit_cost = 0.75 * number_of_units
    print(f'Your unit cost is ${unit_cost:.2f}')

elif number_of_units > 300:
    unit_cost = 1.20 * number_of_units
    print(f'Your unit cost is ${unit_cost:.2f}')

print(f'Hello {tenant_name}, a fixed meter charge of $50 will be added to your bill')
print(f'Your total electricity bill is {unit_cost + 50}')