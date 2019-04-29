def merge_the_tools(string, k):
    arr=[]
    next=0
    prev=0
    for i in range(len(string)):
        prev=next
        if((next+k)>len(string)):
            arr.append(string[next:len(string)])
            break
        arr.append(string[next:next+k])
        next=prev+k
    for element in arr:
        if(element!=""):
            result=""
            for char in element:
                if char not in result:
                    result+=char
            print(result)

if __name__ == '__main__':
    print("Sample Input")
    print("     AABCAAADA")
    print("     3")
    print("Expected Output")
    print('''
    AB
    CA
    AD
    
    ''')
    print("Enter a sample String followed by number in the consecutive line")
    string, k = input(), int(input())
    merge_the_tools(string, k)


    '''
    https://www.hackerrank.com/challenges/merge-the-tools/problem
    Given an Input like AABCAAADA and a number like 3

    will output:
    AB
    CA
    AD
    '''