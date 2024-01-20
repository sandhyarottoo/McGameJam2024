# list of variables to return
global_vars = {'width': 1300, 'height': 750, 'dt': 0.01,'playervelocity':5,'jumpvel':300, 
        'obstacle_speed': -130, 'g_obs_dims': (60, 120), 'game_name': "Chasing the Contraption",
        'playerheight':211,'playerwidth':60}

vars = global_vars.copy()


def getVars(listOfNames):
    '''
    takes a list of strings as input. The names should 
    match the vars you want from the below dictionary
    '''
    global vars
    returned = []

    for name in listOfNames:
        returned.append(vars[name.lower()]) # .lower() ensures that the variables are not case sensitive

    return returned

def changeValue(key, value):
    '''
    Change the value of a global variable
    '''
    global vars
    vars[key] = value
    
def resetValues():
    global global_vars
    global vars
    
    vars = global_vars.copy()
    
    
print(vars)
changeValue("playervelocity", 1)
print(vars)
resetValues()
print(vars)