
def movement(direction,location):
    direction.lower()
    if direction == 'e':
        location += 10
    elif direction == 'w':
        location -= 10
    elif direction == 'n':
        location += 1
    elif direction == 's':
        location -= 1
    return location
    

## Function wich tells you where you can go and you input where to go
## return error if direction is not valid
def where_to_go(location):
    north = '(N)orth'
    east = '(E)ast'
    south = '(S)outh'
    west = '(W)est'
    o = ' or '
    direction = 'xx'
    cardinal_direction = ''
    while cardinal_direction.find(direction) == -1:
        if direction != 'xx':
            print('Not a valid direction!')

        if location == 11 or location == 21 or location == 31:
            cardinal_direction = 'n'
            print('You can travel: {}.'.format(north))
        elif location == 12:
            cardinal_direction = 'nes'
            print('You can travel: {}.'.format(north + o + east + o + south))
        elif location == 13:
            cardinal_direction = 'es'
            print('You can travel: {}.'.format(east + o + south))
        elif location == 22 or location == 33:
            cardinal_direction = 'sw'
            print('You can travel: {}.'.format(south + o + west))
        elif location == 23:
            cardinal_direction = 'ew'
            print('You can travel: {}.'.format(east + o + west))
        elif location == 32:
            cardinal_direction = 'ns'
            print('You can travel: {}.'.format(north + o + south))
        direction = (input('Direction: ')).lower()
    return direction

location = 11
while location != 31:
    direction = where_to_go(location)
    location = movement(direction,location)
print('Victory!')

