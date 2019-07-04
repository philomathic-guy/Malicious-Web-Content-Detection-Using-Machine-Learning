# Purpose - To print the training data and check the parsing logic for it.
# Note: This file is not a part of the codepath which is used by the Chrome extension for making a decision.

import numpy as np
from features_extraction import DIRECTORY_NAME, LOCALHOST_PATH

with open(LOCALHOST_PATH + DIRECTORY_NAME + '/dataset/Training Dataset.arff') as f:
    file = f.read()
data_list = file.split('\n')

print(data_list)
print("/////////////////////////////////")

data = np.array(data_list)
data1 = [i.split(',') for i in data]

print("Data1 before indexing - ", data1)
print ("Length of data1 - ", len(data1))
print ("////////////////////////////////")

data1 = data1[0:-1]

print ("Data1 after indexing - ", data1)
print ("Length of data1 - ", len(data1))

# for i in data1:
#    labels.append(i[30])
data1 = np.array(data1)

print ("Converted to np array - ", data1)
print ("Number of columns in a row - ", len(data1[0]))
print ("Shape of data1 - ", data1.shape)
print ("////////////////////////////////")

features = data1[:, :-1]

print ("Features array - ", features)
print ("Number of columns in a row - ", len(features[0]))
