answer = input('Would you like to continue? ')

if answer == 'no' or answer == 'n':
    print('Exiting')
elif answer == 'yes' or answer == 'y':
    print('Continuing ...')
    print('Complete!')
else:
    print('Please try again and respond with yes or no.')
