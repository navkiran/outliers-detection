# Library for removing outliers from pandas dataframe

## Update in 1.1.0 - command line script method changed, supports calling from both windows and linux terminal 
Takes two inputs - filename of input csv, intended filename of output csv. 

Two optional arguments - which must be provided together or left out.
Third argument is threshold, by default it's 1.5. Fourth argument is method - z_score or IQR.

Output is the number of rows removed from the input dataset. Resulting csv is saved as output.csv. 


## Installation
`pip install outliers_navkiran`

*Recommended - test in a virtual environment.* 

## Use via command line
`outliers_navkiran_cli in.csv out.csv`

Defaults are 1.5 threshold and IQR.

When providing custom threshold and method:
 
`outliers_navkiran_cli in.csv out.csv 3 z_score`
`outliers_navkiran_cli in.csv out.csv 3 IQR`

First argument after outcli is the input csv filename from which the dataset is extracted. The second argument is for storing the final dataset after processing.

## Use in .py script
```
from outliers_navkiran import remove_outliers_z,remove_outliers_iqr
# for using z-score
remove_outliers_z('input.csv', 'output.csv',1.5)
# for using IQR
remove_outliers_iqr('input.csv', 'output.csv',1.5)
```

