import numpy as np
import pandas as pd

def remove_outliers(incsv_filename, outcsv_filename):

    dataset = pd.read_csv(incsv_filename)	
    dataset = dataset.iloc[:,1:]  

    for i, row in d.iterrows():
        threshold = 3
        mean = np.mean(row)
        std = np.std(row)
        for value in row:
            z_score = (value-mean)/std
            if np.abs(z_score)>threshold:
                dataset = dataset.drop(d.index[i])
                break
            
    dataset.to_csv(outcsv_filename, index=False)
    print ('The no of rows removed:',len(d) - len(dataset))
