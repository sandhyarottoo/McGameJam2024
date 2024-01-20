

def getVars(listOfNames):
    '''
    takes a list of strings as input. The names should 
    match the vars you want from the below dictionary
    '''

    vars = {'width': 900, 'height': 700, 'dt': 0.01}
    returned = []

    for name in listOfNames:
        returned.append(vars[name])

    return returned