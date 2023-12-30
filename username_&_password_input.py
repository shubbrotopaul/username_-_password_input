username = input('What is your username?')
password = input('What is your password?')

password_length = len(password)

hidding_password = '*' * password_length

print(f'{username} , your password {hidding_password}, is {password_length} letters long') 