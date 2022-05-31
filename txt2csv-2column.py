import pandas as pd
import os

path = r"C:\Users\z5259\OneDrive\2022_論文撰寫檔案夾\network-test-v2\package-size"
filename = r"\5gsa\p64-c1000-i1-v3"

filePath = path + filename
file1 = open(filePath + r".txt", "r")

file2 = open(filePath + r"-ll.txt", "w+")

filenameSplit = filename.split("\\")
# columnName = ""
# for i in filenameSplit:
#     columnName = columnName + i + " "
columnName = filenameSplit[1]
tolalLine = 0

for postion, line_value in enumerate(file1):
    tolalLine += 1
file1.close()

file1 = open(filePath + r".txt", "r")
for position, line_value in enumerate(file1):
    if position > 0 and position <= (tolalLine - 5):
        raw_list = line_value.split()
        raw_list2 = raw_list[6].split("=")
        add_value = raw_list[0] + raw_list[1] + " " + raw_list2[1] + "\n"
        file2.writelines(add_value)
file1.close()
file2.close()

read_file = pd.read_csv(filePath + r"-ll.txt", delimiter=" ", header=None)

read_file.columns = ["package-size", columnName]
read_file.to_csv(filePath + r"-2column.csv", index=None)

os.remove(filePath + r"-ll.txt")

