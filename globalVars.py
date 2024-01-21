# list of variables to return
global_vars = {'width': 1300, 'height': 750, 'dt': 0.01,'playervelocity':5,'jumpvel':300, 
        'obstacle_speed': -130, 'g_obs_dims': (60, 120), 'game_name': "Chasing the Contraption",
        'playerheight':111,'playerwidth':60, 'g': 220}

vars = global_vars.copy()


def getVars(listOfNames=None):
    '''
    takes a list of strings as input. The names should 
    match the vars you want from the below dictionary. If None, returns the whole dictionary.
    '''
    global vars
    
    if listOfNames is None:
        return vars
    
    returned = []

    for name in listOfNames:
        returned.append(vars[name.lower()]) # .lower() ensures that the variables are not case sensitive

    return returned

def changeValue(key, value):
    '''
    Change the value of a specified global variable.
    '''
    global vars
    vars[key] = value
    
def resetValues():
    '''
    Resets global variables.
    '''
    global global_vars
    global vars
    
    vars = global_vars.copy()