import string

password = input()

char: str
lower = 0
upper = 0
number = 0

if len(password) > 12 or len(password) < 8:
    print('Invalid')

else:
    for char in password:
        if char.islower() == True:
            lower += 1
        elif char.isupper() == True:
            upper += 1
        elif char.isdigit() == True:
            number += 1

    if lower >=3 and upper >=2 and number >= 1:
        print('Valid')
    else:
        print('Invalid')
