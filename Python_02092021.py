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
    
    
    
if __name__ == "__main__": main()    
    