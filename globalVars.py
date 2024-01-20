

def getVars(listOfNames):
    '''
    takes a list of strings as input. The names should 
    match the vars you want from the below dictionary
    '''
    
    # list of variables to return

    vars = {'width': 1300, 'height': 750, 'dt': 0.01,'playerVelocity':100,'jumpVel':100, 
            'obstacle_speed': -130, 'g_obs_dims': (60, 120), 'game_name': "Chasing the Contraption"}
    
    returned = []

    for name in listOfNames:
        returned.append(vars[name.lower()]) # .lower() ensures that the variables are not case sensitive

    return returned