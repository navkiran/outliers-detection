# Library for removing outliers from pandas dataframe

```
PROJECT 2, UCS633 - Data Analysis and Visualization
Navkiran Singh  
COE17
Roll number: 101703365
```
Takes two inputs - filename of input csv, intended filename of output csv.
Output is the number of rows removed from the input dataset. Resulting csv is saved as output.csv. 
`The no of rows removed: 5`

## Installation
`pip install outliers_navkiran`

*Recommended - test in a virtual environment.* 

## Use via command line
`outliers_navkiran_cli myData.csv newData.csv`

First argument after outcli is the input csv filename from which the dataset is extracted. The second argument is for storing the final dataset after processing.

## Use in .py script
```
from outliers_navkiran import remove_outliers
remove_outliers('input.csv', 'output.csv')
```

