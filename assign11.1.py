import re

nums=[]
tot=0
fname=input("Please enter the filename: ")
if(len(fname)<1):
    fname="regex.txt"
file=open(fname)
for line in file:
    nums=nums+re.findall("[0-9]+",line)

for num in nums:
    tot=tot+int(num)
print(tot)