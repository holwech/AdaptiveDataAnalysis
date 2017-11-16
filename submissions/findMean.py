import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

data1 = pd.read_csv("neural_network.csv").values
data2 = pd.read_csv("xgboost.csv").values
data3 = pd.read_csv("SVM_standard_params.csv").values

f = open('avg_submission.csv', 'w')
f.write('id,is_iceberg' + '\n')
for i in range(len(data1)): #range(0,5):
	#print(data1[i][0], data1[i][1])
	#print(data1[i][1])
	if str(data1[i][0]) != str(data2[i][0]):
		print('oioioioioio')
	
	a = 0.5*data1[i][1] + 0.4*data2[i][1] + 0.1 * data3[i][1]
	f.write(str(data1[i][0]) + ',' + str(a) + '\n')


f.close()
