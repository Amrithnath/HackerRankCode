n = int(input())
l = []
for _ in range(n):
    s = input()
    s=s.split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)
'''
https://www.hackerrank.com/challenges/python-lists/problem
given an input of list funcitons will perform the said functions(first input the number of commands)


Sample input:

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print


Sample output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''