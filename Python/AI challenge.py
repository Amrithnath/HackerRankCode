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

'''
https://www.hackerrank.com/challenges/saveprincess/problem
Bot saves princess
Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and
can move one step at a time in any of the four directions. Can you rescue the princess?
Input format
The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an
NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess
position is denoted by 'p'.
Grid is indexed using Matrix Convention
Output format
Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a
newline. The valid moves are LEFT or RIGHT or UP or DOWN.

Sample input

3
---
-m-
p--

Sample output

DOWN
LEFT

Sample input

4
----
--p-
----
-m--

Sample Output

UP
UP
RIGHT

Sample Input

2
--
--

Sample Output
Princess or Maker is not found, please give the location of both the princess and the maker

Task
Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the
character array grid. The grid will be formatted exactly as you see it in the input, so for the sample input
the princess is at grid[2][0]. The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive
lines to rescue/reach the princess. The goal is to reach the princess in as few moves as possible.
The above sample input is just to help you understand the format. The princess ('p') can be in any one of
the four corners.
Scoring
Your score is calculated as follows : (NxN - number of moves made to rescue the princess)/10, where N is
the size of the grid (3x3 in the sample testcase).
'''