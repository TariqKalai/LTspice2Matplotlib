import numpy as np

def data_to_floats(String_data):

    time = np.array(String_data.split("\n")[1:])
    time = [element.split("\t")[0] for element in time if element.split("\t")[0] != '']
    time = np.array(time).astype(float)

    Data = String_data.split("\n")[1:-1]
    Data = np.array([thing.split("\t")[1] for thing in Data if thing.split("\t")[1] != '']).astype(float)
    
    return (time, Data)
