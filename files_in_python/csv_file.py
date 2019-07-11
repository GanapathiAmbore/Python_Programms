import csv
csv_data=[["Name","Age"],["abcd",26],["aws",26],["Hadoop",30],["MachineLearning",30]]
with open("Sample_csv.csv",'w') as file:
    data=csv.writer(file)
    data.writerows(csv_data)