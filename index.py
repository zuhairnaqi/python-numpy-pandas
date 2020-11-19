import pandas as p
import numpy as np

# Creating a data frame
dataFrame = p.DataFrame(np.random.randn(4,3), index=['a', 'c', 'd', 'f'], columns=['One', 'Two', 'Three'])
print(dataFrame)
print("---------------- Line Break ---------------------")

# Data frame 2
#Adding null values to d f
newFrame =  dataFrame.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
print(newFrame)
print("---------------- Line Break ---------------------")


# Check if value of coloum is null
print(newFrame['Two'].isnull())
print(newFrame[newFrame['Two'].isnull()])

print("---------------- Line Break ---------------------")

# Replace missing data
print(newFrame['Two'].fillna("Zuhair"))

print("---------------- Line Break ---------------------")

#Drop missing data
print(newFrame['One'].dropna())

print("---------------- Line Break ---------------------")

#Fill the null data in columns with specific value
for col in newFrame:
    newFrame[col] = newFrame[col].fillna('filled')
    
print("new Frame", newFrame)






