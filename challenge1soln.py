first_value = '   FIRST challenge             '
second_value = '-   second challenge   -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

#First challenge
first_value = first_value.strip()
first_value = first_value.title()
first_value = f'{first_value:^30}'

#Second challenge
second_value = second_value.replace('-', ' ')
second_value = second_value.strip()
second_value = second_value.capitalize()

#Third challenge
third_value = third_value.replace(' ', '')
third_value = third_value.replace('-', ' ')
third_value = third_value.swapcase()
third_value = f'{third_value:>30}'

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)

print(fourth_value, fifth_value, sixth_value, sep='#', end='!\n')

# Fifth challenge - use only a single print() function. Create tabs and new lines using f-strings. 

print(f' {fourth_value:^20}\n {fifth_value:^20}\n {sixth_value:^20}')