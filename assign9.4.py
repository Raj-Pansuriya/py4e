"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.

The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

fname = input("Enter file:")
count={}
if(len(fname) < 1):
    fname = "mbox-short.txt"
fhandle = open(fname)
for line in fhandle:
    if line.startswith("From "):
        count[line.split()[1]]=count.get(line.split()[1],0)+1
slist=sorted([(v,k) for k,v in count.items()],reverse=True)
print(slist[0][1],slist[0][0])