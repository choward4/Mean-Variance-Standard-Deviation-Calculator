import numpy as np

def calculate(list):

    analysis = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    # Check if list meets standard, otherwise throw error
    
    try: 
        if len(list) != 9:
            raise ValueError
    except ValueError as exp:
        print("List must contain nine numbers.", exp)
        exit()

    # convert list to 3x3 np array
    # TODO
    


    return analysis