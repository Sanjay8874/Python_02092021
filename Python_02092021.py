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
         
        
    
if __name__ == "__main__": main()    
    