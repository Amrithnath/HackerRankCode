#!/usr/bin/python
import math
def displayPathtoPrincess(n,grid):
    mloc=[0,0]
    pfound=False
    mfound=False
    sameline=False
    j=0
    for element in grid:
        i=0
        for letter in element:
            if letter is 'p':
                #print(i,letter)
                locx=i
                path=element
                pfound=True
            elif letter is 'm':
                mloc[0]=j
                mloc[1]=i
                mfound=True
            i+=1
        j+=1
    if pfound is False or mfound is False:
        print("Princess or Maker is not found, please give the location of both the princess and the maker")      
    else:
        locy=grid.index(path)
        while(sameline==False):
            if((locy+1)>(mloc[0]+1)):
                locy=locy-1
                print("DOWN")
            elif((locy+1)==(mloc[0]+1)):
                sameline=True
            else:
                locy=locy+1
                print("UP")
        samecol=False
        while(samecol==False):
            if((locx+1)>(mloc[1]+1)):
                locx=locx-1
                print("RIGHT")
            elif((locx+1)==(mloc[1]+1)):
                samecol=True
            else:
                locx=locx+1
                print("LEFT")
    
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)