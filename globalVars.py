

def getVars(listOfNames):
    '''
    takes a list of strings as input. The names should 
    match the vars you want from the below dictionary
    '''

    # variable dictionary
    vars = {'width': 900, 'height': 700, 
            'dt': 0.01, 
            'game_name': "Chasing the Contraption"}
    
    # list of variables to return

    vars = {'width': 1300, 'height': 750, 'dt': 0.01,'playerVelocity':100,'jumpVel':100}
    returned = []

    for name in listOfNames:
        returned.append(vars[name.lower()]) # .lower() ensures that the variables are not case sensitive

    return returned