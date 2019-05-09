def division():
    x=[100,110,120,130,140,150]
    y=[x%3 for x in x]
    print(y)


def sorted():
    a=["apple","banana","mango"]
    b=["avocado","peach","orange"]
    c=["pineapple","lemon"]
    d=a+b+c

    d.sort()

def divisible_by_three(n): 
    x=range(1,n+1)
    for z in x:
        if z%3==0:
            print(z)
    

def flattens():
    x=[[1,2],[3,4],[5,6]]
    flatlist=[]
    for sublist in x:
        for item in sublist
        flatlist.append(item)
        print(flatlist)


def smallest():
    a=[1,3,6,8,2,4,5.7]
    print(min(a))


def duplicate():
    x=["a","b","a","e","d","b","c","e","f","g","h"]
    

def squares():
    x=range(149,159)
    d={}
    for z in x:
        d[z]=z**2
    print(d)

students=[{"age":19,"name":"Eunice"},{"age":21,"name":"Agnes"},{"age":18,"name":"Teresa"},{"age":22,"name":"Asha"}]
for student in students:
    print("Hello {}, you were born in year {}".format(student["name"],(2019-(student["age"]))