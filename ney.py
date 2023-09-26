alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slcw'}
print("Original x-position: " + str(alien_0['x_position']))
    # Move the alien to the right.
    # Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'sLow'.lower():
    x_increment = 3
elif alien_0['speed'] == 'medium':
    x_increment = 4
else:
    x_increment = 5
    # This must be a fast alien.
    # The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
