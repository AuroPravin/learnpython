#To check no of  lines in the given file:

'''
fhand=open('/Downloads/Practice/Task_Day01/sam.txt','r')
words=fhand.read()
no_lines=0
for lines in fhand:
    no_lines=no_lines+1
print("Total lines: ",no_lines)
print(len(words))

'''
# Task 2:

'''

hand=open('/Downloads/Practice/Task_Day01/sam.txt','r')
for line in hand:
    line=line.rstrip()
    if line.startswith('Hi:'):
        continue
    print(line) 
'''


'''
fname=input("Enter the file name: ")
fhand=open(fname)
count=0
for line in fhand:
    if line.startswith("Hi"):
        count=count=1
print("There were",count,"subject lines", fhand)

'''
# Task : Read a file and print them in ouppercase
hand=open('/Downloads/Practice/Task_Day01/sam.txt','r')
for line in hand:
    remove=line.rstrip()
    print(remove.upper())
