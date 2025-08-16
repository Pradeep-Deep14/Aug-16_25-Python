def func():
    a,*b=["Harry","Precious","Peter"]
    names = b
    return "Peter" in [names] 
print(func())