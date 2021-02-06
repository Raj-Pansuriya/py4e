"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.

You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fname=input("Enter file:")
if(len(fname) < 1):
    fname = "mbox-short.txt"
counts={}
fhandle = open(fname)
for line in fhandle:
    if line.startswith("From "):
        counts[line.split()[5].split(":")[0]]=counts.get(line.split()[5].split(":")[0],0)+1

slist=sorted([(k,v) for k,v in counts.items()])
for k,v in slist:
    print(k,v)