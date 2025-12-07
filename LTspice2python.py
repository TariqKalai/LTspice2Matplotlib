import re
import numpy as np
from matplotlib import pyplot as plt
from Functions import data_to_floats
import sys

Path = input("Path of your data : ")
Param = input("Does your data have parameters (y/n) ? ")
List = []
Name = []

if Param == "y":
    
    file  = open(Path, "r")
    first = file.read().split("Step Information")[1:]
    file.close() 

    pattern = input("Write the name of the parameter in regex style : ")
    

    #Separates each step in A list [step1, step2,....]
    for i in first:
        x = re.findall(pattern, i)[0]
        Name.append(x)
        x = i.split(x)[1].split(")")[1]
        List.append(x)

    for numero, string_data in enumerate(List):

        List[numero] = data_to_floats(string_data)

        time = List[numero][0]
        Data = List[numero][1]

        if len(time) == len(Data):
            plt.plot(time, Data, label=Name[numero])
        else:
            print(f"Skipping {Name[numero]}: X and Y arrays have different lengths ({len(time)} vs {len(Data)})")

if Param =="n":

    file  = open(Path, "r")
    first = file.read().split(")")[1]
    file.close() 

    List.append(data_to_floats(first))
    Name = input("what is the label of you graph : ")

    time = List[0][0]
    Data = List[0][1]

    if len(time) == len(Data):
        plt.plot(time, Data, label=Name)
    else:
        print(f"Skipping {Name}: X and Y arrays have different lengths ({len(time)} vs {len(Data)})")

else:
    print("not y/n anwser, script aborted")
    sys.exit()



y_max = np.max([arr[1].max() for arr in List if arr[1].size > 0]) # Find the maximum Y-value

readable_step = y_max / 10 
plt.yticks(np.arange(0, y_max + readable_step, readable_step))

plt.xlabel("VDD[V]")
plt.ylabel("ID [A]")
plt.title("courbe I-V")
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)

method = input("Do you want to save the graph as svg or see it (save/show) : ")
if method == "show":
    plt.show()

elif method == "save":
    filename = input("Name of your file ") +".svg"
    plt.savefig(filename, format="svg")

else :
    print("Invalid input, the graph won't be saved as svg ")
    plt.show()




    

