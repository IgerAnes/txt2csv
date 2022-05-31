import pandas as pd
import os

path = r"C:\Users\z5259\OneDrive\2022_論文撰寫檔案夾\network-test-v2\toCN"
filename = r"\p1024-c1000-i1"

filePath = path + filename
file1 = open(filePath + r".txt", "r")

file2 = open(filePath + r"-ll.txt", "w+")

for position, line_value in enumerate(file1):
    if position > 0 and position <= 1000:
        raw_list = line_value.split()
        raw_list2 = raw_list[6].split("=")
        add_value = raw_list2[1] + "\n"
        file2.writelines(add_value)
file1.close()
file2.close()

read_file = pd.read_csv(filePath + r"-ll.txt", delimiter=" ", header=None)
filenameSplit = filename.split("\\")
columnName = ""
for i in filenameSplit:
    columnName = columnName + i + " "
read_file.columns = [columnName]
read_file.to_csv(filePath + r".csv", index=None)

os.remove(filePath + r"-ll.txt")

