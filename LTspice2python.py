import re
import numpy as np
from matplotlib import pyplot as plt

file  = open("Data/Labo2_part2.txt", "r") 
first = file.read().split("Step Information")[1:]
file.close() # Good practice to close the file

pattern = r'V_gs=[0-9]+'
List = []
Name = []

#Separates each step in A list [step1, step2,....]
for i in first:
    x = re.findall(pattern, i)[0]
    Name.append(x)
    x = i.split(x)[1].split(")")[1]
    List.append(x)

    
# for each element in the list get the proper value in form of an array, and takes out the last one since it is ""
for number,i in enumerate(List):

    #Gets the time array( at first i tought it was 
    # the same for every data but not really sometimes 
    # it is different like for double redresseur.txt so it does it in the loop)
    time = np.array(List[number].split("\n")[1:])
    time = [element.split("\t")[0] for element in time if element.split("\t")[0] != '']
    time = np.array(time).astype(float)

    Data = i.split("\n")[1:-1]
    Data = np.array([thing.split("\t")[1] for thing in Data if thing.split("\t")[1] != '']).astype(float)
    List[number] = Data

    
    if len(time) == len(Data):
        plt.plot(time, Data, label=Name[number])
    else:
        print(f"Skipping {Name[number]}: X and Y arrays have different lengths ({len(time)} vs {len(Data)})")


y_max = np.max([arr.max() for arr in List if arr.size > 0]) # Find the maximum Y-value

readable_step = y_max / 10 
plt.yticks(np.arange(0, y_max + readable_step, readable_step))



plt.xlabel("VDD[V]")
plt.ylabel("ID [A]")
plt.title("courbe I-V")
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()





    

