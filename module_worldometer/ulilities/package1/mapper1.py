import sys  



if len(sys.argv) < 2:
    print("Usage: python mapper.py <option>")
    sys.exit(1)

col = sys.argv[1]
if(col==1):
    attrib = 2
if(col==2):
    attrib = 8
if(col==3):
    attrib = 4
if(col==4):
    attrib = 6
if(col==5):
    attrib = 12
if(col==6):
    attrib = 11
if(col==7):
    attrib = 13
if(col==8):
    attrib = 3
if(col==9):
    attrib = 5
if(col==10):
    attrib = 7


with open(sys.argv[1],'r') as f:
    for line in f:
        if(line==""):
            break
        line = line.strip()
        row = line.split("\t")
        print(row[1],row[attrib])
        
        