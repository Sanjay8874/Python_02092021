#variable
def main():
    a=10
    b=2.4
    c="sanjay"
    d=10/3
    print(type(a),a,id(a))
    print(type(b),b,id(b))
    print(type(c),c,id(c))
    print(type(d),d,id(d))
    
#List,tuple
    x=(1,2,3)
    y=[1,2,3,4,5]
    y.append(4)
    y.insert(5,6)
    print(type(x),x,id(x))
    print(type(y),y,id(y))
    
    s="string"
    for i in s:
        print(i)
    
    
#conditional

    a,b =4,5
    if a>b:
         print("a is greater than b")
    elif a<b:
         print("a is less than b or b is grater than a")
    else:
         print("a is equal to b")
         
        
#Loop
#While
#Simple fibonacci serise

    a = 0
    b = 1
    while b<10:
        print(b, end=" ")
        a,b=b,a+b
        
#For 
    print("\n")
    for i in range(1,10):
        print(i, end=" ")

#continue and break statements
#continue

    s="this is string"
    for i in s:
         if i == 's':
             continue
         print(i, end="")
 #break        
    s="this is string"
    for i in s:
         if i == 's':
             break
         print(i, end="")     
if __name__ == "__main__": main()


#Regex-Extract some perticular word or sentance from 

import re
print("\n")
def Regex():
    file = open('regex.txt')
    for i in file:
        match = re.search('\w{7}',i)
        if match:
            print(match.group())
            
if __name__ == "__main__": Regex()

#Function

def add(a,b):
    c = a+b
    print(c)
    
def deff(a,b):
    c = a-b
    print(c)
    if c>0:
        print("positive values")
    elif c == 0:
        print("Zero")
    else:
        print("Negative values")
  
def division(a,b):
    c = a/b
    print(c)

def Mult(a,b):
    c = a*b
    print(c)
               
add(5, 5)
deff(5,5)
division(10,5)
Mult(5,5)


#greater no


def max(a,b):
    if a>b:
        print("a is grater then b")
    else:
        print("b is grater then a")
        
max(10,11)        















 
    