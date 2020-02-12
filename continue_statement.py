while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) <= 3:
        print('To small string')
        continue
    print('Input is of sufficient length')