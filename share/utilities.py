import numpy as np
import pandas as pd

def read_lammps_log(file):
    '''Reads LAMMPS log thermo output into a pandas DataFrame
    Params: (str) filename
    Returns: pandas DataFrame'''

    with open(file, 'r') as f:
        out = f.readlines()
    flag = False
    first_time = True
    for i, val in enumerate(out):
        test = val.split()
        test.append('')
        if test[0] == 'Step':
            if first_time:
                dat = [[] for j in range(len(out[i+1].split()))]
                dat_head = val.split()
                first_time = False
            flag = True
            continue

        if flag:
            try:
                for j, num in enumerate(val.split()):
                    dat[j].append(float(num))
            except:
                flag = 0

    dat = np.array(dat) 
    df = pd.DataFrame(dat[:].T, columns=dat_head[:]) # turn into a DataFrame with header
    df.drop_duplicates(subset=df.columns[-1], inplace=True)
    
    return df