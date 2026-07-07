weight = float(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in meters: '))
bmi = weight/(height**2)

print('bmi', format(bmi, '.2f'))
