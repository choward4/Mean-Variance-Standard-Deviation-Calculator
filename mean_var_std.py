import numpy as np

def calculate(list):

    mean = []
    variance = []
    stdDev = []
    max = []
    min = []
    sum = []
    
    analysis = {
        # forEach: [axis1, axis2, flattened]
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    # Check if list meets standard, otherwise throw error
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        
    # convert list to 3x3 np array
    flattenedArr = np.array(list)
    Matrix = flattenedArr.reshape(3,3)


    # add values to dict for axis1 and axis2 
    for x in range(2):
       mean.append(Matrix.mean(axis=x).tolist())
       variance.append(Matrix.var(axis=x).tolist())
       stdDev.append(Matrix.std(axis=x).tolist())
       max.append(Matrix.max(axis=x).tolist())
       min.append(Matrix.min(axis=x).tolist())
       sum.append(Matrix.sum(axis=x).tolist())
    
    # add values to dict for flattened arr
    mean.append(float(flattenedArr.mean()))
    variance.append(float(flattenedArr.var()))
    stdDev.append(float(flattenedArr.std()))
    max.append(float(flattenedArr.max()))
    min.append(float(flattenedArr.min()))
    sum.append(float(flattenedArr.sum()))

    # Update dictionary analysis
    analysis['mean'] = mean
    analysis['variance'] = variance
    analysis['standard deviation'] = stdDev
    analysis['max'] = max
    analysis['min'] = min
    analysis['sum'] = sum

    #print(analysis)

    return analysis