

def getVars(listOfNames):
    '''
    takes a list of strings as input. The names should 
    match the vars you want from the below dictionary
    '''

    vars = {'width': 1300, 'height': 750, 'dt': 0.01}
    returned = []

    for name in listOfNames:
        returned.append(vars[name])

    return returned