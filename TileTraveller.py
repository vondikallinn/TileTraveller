#player positions
x = 1
y = 1

#Directions for the player to choose from

n = 1
s = -1
e = 1
w = -1

direction = 'n' 's' 'e' 'w'
tile1 == (x = 1 and y == 1)

def player_position():

print(f'You can travel {direction}')
player_direction = str(input('Direction: ').lower)

return player_position


print(f'You can travel {direction}')
player_direction = str(input('Direction: ').lower)
