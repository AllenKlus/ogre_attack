
# Importing the needed modules

import time
import random

# Defining the game loop variable and the health variable's

done = False

ogre_health = 10

player_health = 6

# Main game loop

while done == False:

    # Prints the current health at the begining of each loop

    print('Ogre health: {0}\nPlayer health: {1}'.format(ogre_health,player_health))

    player_attack = random.randint(1,2)

    # If random number (player_attack) is 2 the player hits the ogre

    if player_attack == 2:

        # Random number from 1-2 that decreases the ogre's health by

        player_damage = random.randint(1,2)

        # Printing out the hit message and decreasing the ogre's health

        print('You hit the ogre for {0} damage!'.format(player_damage))

        ogre_health = ogre_health - player_damage


    # If the variable player_attack is 1, then the player misses the ogre and no damage is dealt

    else:
        print('Oh no! You missed the ogre!')


    # Checks if ogre_health is greater than 0, if so then runs the ogre's turn

    if ogre_health > 0:

        # The ogre has a worse chance of hitting the player, but he can deal more damage

        ogre_attack = random.randint(1,3)

        # If the ogre_attack variable is equal to 3 then the ogre hits the player

        if ogre_attack == 3:

        # Just like the player, the ogre's damage is a random number. It ranges from 1-3 and determines how much damage is dealt to the player and prints out the damage message and decreases the player health

            ogre_damage = random.randint(1,3)

            print('The ogre hit you for {0} damage!'.format(ogre_damage))

            player_health = player_health - ogre_damage

        # If variable oger_attack isn't equal to 3 then the ogre misses it's attack and prints out a missed message

        else:
            print('Whew, close one. The ogre missed it\'s attack!')

    # Once the ogres_health gets to 0 or less than 0, the player wins and a congratulation message is displayed. Done is then set to True and the main game loop ends

    if ogre_health <= 0:
        print('\nCongrats! You killed the evil ogre, here\'s a cookie!')

        done = True

    # Once the players_health gets to 0 or less than 0, the ogre wins and a losing message is displayed. Done is then set to True and the main game loop ends

    if player_health <= 0:
        print('\nAw nuts. The ogre killed you, better luck next time.')
        
        done = True

    # time.sleep is used to slow down the loop so the user has time to read what's going on

    print('\n')
    time.sleep(4)
    

