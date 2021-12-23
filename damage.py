def attack_player(player, health, damage, num_attacks, armor):

    """
    ##############################################################

    # first compute the total_health by adding health and armor
    # next compute the total_damage by multiplying damage and num_attacks
    # i.e. damage*num_attacks
    # get the remaining_health by subtracting total_health and total_damage
    # now if remaining_health is more than zero it means alive and hence return 
    # player name with remaining_health 
    
    # otherwise return that player name is eliminated
    ##############################################################

    >>> attack_player('Wraith', 100, 10, 5, 0)
    'Wraith has 50 health remaining'
    >>> attack_player('Loba', 50, 25, 4, 50)
    'Loba is eliminated'
    >>> attack_player('Matt', 150, 35, 4, 20)
    'Matt has 30 health remaining'
    >>> attack_player('David',200, 50, 4, 0)
    'David is eliminated'
    >>> attack_player('Michael', 100, 45, 4, 8)
    'Michael is eliminated'
    """
    
    Total_health = health + armor
    
    Total_damage = damage*num_attacks
    
    remaining_health = Total_health - Total_damage
    
    if remaining_health > 0:
        return '{} has {} health remaining'.format(player,remaining_health)
    else:
        return f'{player} is eliminated'