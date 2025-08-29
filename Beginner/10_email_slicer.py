email = input('Enter your email address: ')

parts = email.split('@')

part1 = parts[0]
part2 = parts[1]

print(f'Username: {part1}\nDomain: {part2}')