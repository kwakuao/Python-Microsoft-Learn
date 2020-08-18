# celsius = (fahrenheit - 32) * 5/9

fahrenheit_temp = (input('What is the temperature in fahrenheit? '))

if fahrenheit_temp.isnumeric() == False:
    print('Input is not a number.')
    exit()

fahrenheit_temp = float(fahrenheit_temp)

celsius = round(((fahrenheit_temp - 32) * 5/9), 2)
print('The temperature in celsius is ' + str(celsius) + ' degrees.')
