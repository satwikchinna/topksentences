print "..............................................................................\n\n"
import os.path
print ".......................WELCOME TO TOP K SENTENCE FINDER.......................\n\n\n"
infile = raw_input("ENTER THE DOCUMENT TO BE ALAYSED WITH EXTENSION ")
import math
outfile = "tokenized.txt"
outfile2 = "cleared.txt"
replace_list = ['.', '!' , '?' ,',' ]
tcount=0
scount = 0

 


if(os.path.isfile(infile)):
  print("File Exists!!")
else:
  print("FILE DOESN'T EXIST!!")
  exit()

fin = open(infile) 
fout = open(outfile, "w+")
for line in fin:
    for word in replace_list:
        line = line.replace(word, "\n")
    fout.write(line)
fin.close()
fout.close()
delete_list = [' all ', ' just ', ' being ', ' over ', ' both ', ' through ', ' yourselves ', ' its ', ' before ', ' herself ', ' had ', ' should ', ' to ', ' only ', ' under ', ' ours ', ' has ', ' do ', ' them ', ' his ', ' very ', ' they ', ' not ', ' during ', ' now ', ' him ', ' nor ', ' did ', ' this ', ' she ', ' each ', ' further ', ' where ', ' few ', ' because ', ' doing ', ' some ', ' are ', ' our ', ' ourselves ', ' out ', ' what ', ' for ', ' while ', ' does ', ' above ', ' between ', ' t ', ' be ', ' we ', ' who ', ' were ', ' here ', ' hers ', ' by ', ' on ', ' about ', ' of ', ' against ', ' s ', ' or ', ' own ', ' into ', 'yourself', ' down ', ' your ', ' from ', ' her ', ' their ', ' there ', ' been ', ' whom ', ' too ', 'themselves', ' was ', ' until ', ' more ', ' himself ', ' that ', ' but ', ' don ', ' with ', ' than ', ' those ', ' he ', ' me ', ' myself ', ' these ', ' up ', ' will ', ' below ', ' can ', ' theirs ', ' my ', ' and ', ' then ', ' is ', ' am ', ' it ', ' an ', ' as ', ' itself ', ' at ', ' have ', ' in ', ' any ', ' if ', ' again ', ' no ', ' when ', ' same ', ' how ', ' other ', ' which ', ' you ', ' after ', ' most ', ' such ', ' why ', ' a ', ' off ', ' i ', ' yours ', ' so ', ' the ', ' having ', ' once '

]
fin = open(outfile)
fout = open(outfile2, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, " ")
    fout.write(line)
fin.close()
fout.close() 
"""......................................................................"""

fname = "cleared.txt"
fhand = open(fname)
AllWords = list()      #create new list
ResultList = list()    #create new results list I want to append words to

for line in fhand:
         line.rstrip()   #strip white space
         words = line.split()    #split lines of words and make list
         AllWords.extend(words)   #make the list from 4 lists to 1 list

AllWords.sort()  #sort list

for word in AllWords:   #for each word in line.split()
    if word not in ResultList:    #if a word isn't in line.split            
             ResultList.append(word)   #append it.
count=0
frequency={}
with open('cleared.txt') as infp:
   for line in infp:
      for word in line.split():
           frequency[word] = 0

for i in range(0,len(ResultList)): 
 count=0
  
 with open('cleared.txt') as infp:
   for line in infp:
      for word in line.split():
          
         if ResultList[i] == word:
           frequency[ResultList[i]] = frequency[ResultList[i]] + 1

for i in range(0,len(ResultList)): 
 frequency[ResultList[i]] = float(frequency[ResultList[i]])
 frequency[ResultList[i]] = 1 + math.log10(frequency[ResultList[i]]) 

with open('cleared.txt') as infp:
    for line in infp:
       if line.strip():
          scount += 1
ifreq={}
count = 0
for word in ResultList:
 ifreq[word] = 0
for word in ResultList:
#find occurence of a word
 with open('cleared.txt') as inF:
    for line in inF:
        if word in line:
            ifreq[word] = ifreq[word] + 1

for word in ResultList:
  ifreq[word] = float(ifreq[word])
  ifreq[word] = math.log10(1 + scount/ifreq[word])

tfisf={}
with open('cleared.txt') as infp:
   for line in infp:
     tfisf[line] = 0
with open('cleared.txt') as infp:
   for line in infp:
      for word in line.split():
        tfisf[line] = frequency[word]*ifreq[word] + tfisf[line]



items = [(v, k) for k, v in tfisf.items()]
items.sort()
items.reverse()          
items = [(k) for v, k in items]
k = int(raw_input("ENTER NO OF TOP SENTENCES TO BE PRINTED\n"))
if(( k > scount)):
 print("****PLEASE ENTER VALID NO OF STATEMENT COUNT IT IS EXCEEDING NO OF STATEMENTS PRESENT***")
 
else:
 i=0
 for key in items:
  if (( i < k)):
   print key 
   i = i + 1
  

